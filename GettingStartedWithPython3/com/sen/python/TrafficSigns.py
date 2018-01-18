'''
Created on 30-Dec-2017

@author: senthilkumar
'''
import os
import skimage.data
from numpy.random.mtrand import np
import matplotlib.pyplot as plt 

class TrafficSigns(object):
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
    trafficSigns = TrafficSigns("TrafficSigns")
      
    images, labels = trafficSigns.load_data(train_data_directory)
    #print(np.array(images).ndim)
    #print(len(images))
    #images[0]
    # Print the `labels` dimensions
    #print(np.array(labels).ndim)
    # Print the number of `labels`'s elements
    #print(len(labels))
    # Count the number of labels
    #print(len(set(labels)))
    # Make a histogram with 62 bins of the `labels` data
    #plt.hist(labels, 62)
    # Show the plot
    #plt.show()
    
    # Determine the (random) indexes of the images that you want to see 
    traffic_signs = [500, 2500, 3500, 4000]
    # Fill out the subplots with the random images that you defined 
    for i in range(len(traffic_signs)):
        plt.subplot(1, 4, i+1)
        plt.axis('on')
        plt.imshow(images[traffic_signs[i]])
        plt.subplots_adjust(wspace=0.5)

        plt.show()
        print("shape: {0}, min: {1}, max: {2}".format(images[traffic_signs[i]].shape, 
                                                   images[traffic_signs[i]].min(), 
                                                   images[traffic_signs[i]].max()))

    
    
    
    