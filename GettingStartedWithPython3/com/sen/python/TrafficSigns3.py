'''
Created on 08-Jan-2018

@author: senthilkumar
'''

import os
import skimage.data
from numpy.random.mtrand import np
from skimage import transform 
import matplotlib.pyplot as plt 
from skimage.color import rgb2gray

class TrafficSigns3(object):
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
    trafficSigns = TrafficSigns3("TrafficSigns")
      
    images, labels = trafficSigns.load_data(train_data_directory)
    
    # Rescale the images in the `images` array
    images28 = [transform.resize(image, (28, 28)) for image in images]
    
    # Convert `images28` to an array
    images28 = np.array(images28)
    
    # Convert `images28` to grayscale
    images28 = rgb2gray(images28)
    
    # Determine the (random) indexes of the images that you want to see 
    traffic_signs = [500, 2500, 3500, 4000]
    # Fill out the subplots with the random images that you defined 
    for i in range(len(traffic_signs)):
        plt.subplot(1, 4, i+1)
        plt.axis('on')
        plt.imshow(images28[traffic_signs[i]], cmap="gray")
        plt.subplots_adjust(wspace=0.5)

        plt.show()
        print("shape: {0}, min: {1}, max: {2}".format(images28[traffic_signs[i]].shape, 
                                                   images28[traffic_signs[i]].min(), 
                                                   images28[traffic_signs[i]].max()))
        