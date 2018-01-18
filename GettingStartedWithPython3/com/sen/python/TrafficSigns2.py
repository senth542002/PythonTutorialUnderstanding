'''
Created on 08-Jan-2018

@author: senthilkumar
'''

import os
import skimage.data
from numpy.random.mtrand import np
import matplotlib.pyplot as plt 

class TrafficSigns2(object):
    '''
    classdocs
    '''



    def __init__(self, params):
        '''
        Constructor
        '''
    def load_data(self, data_directory):
        directories = [d for d in os.listdir(data_directory)
                       if os.path.isdir(os.path.join(data_directory,d))]
        
        labels = []
        images = []
        
        for d in directories:
            label_directory = os.path.join(data_directory, d)
            file_names = [os.path.join(label_directory, f)
                          for f in os.listdir(label_directory)
                          if f.endswith(".ppm")]
            
            for f in file_names:
                images.append(skimage.data.imread(f))
                labels.append(int(d))
        return images, labels
    
ROOT_PATH = "/Users/senthilkumar/Documents/workspace/Python"
train_data_directory = os.path.join(ROOT_PATH, "TrafficSigns/Training")
test_data_directory = os.path.join(ROOT_PATH, "TrafficSigns/Testing")
  
if __name__ == '__main__':
    trafficSigns = TrafficSigns2("TrafficSigns")
      
    images, labels = trafficSigns.load_data(train_data_directory)

    # Determine the (random) indexes of the images that you want to see 
    traffic_signs = [500, 2500, 3500, 4000]

    # Get the unique labels 
    unique_labels = set(labels)

    # Initialize the figure
    plt.figure(figsize=(15, 15))

    # Set a counter
    i = 1

    # For each unique label,
    for label in unique_labels:
        # You pick the first image for each label
        image = images[labels.index(label)]
        # Define 64 subplots 
        plt.subplot(8, 8, i)
        # Don't include axes
        plt.axis('off')
        # Add a title to each subplot 
        plt.title("Label {0} ({1})".format(label, labels.count(label)))
        # Add 1 to the counter
        i += 1
        # And you plot this first image 
        plt.imshow(image)
    
    # Show the plot
    plt.show()