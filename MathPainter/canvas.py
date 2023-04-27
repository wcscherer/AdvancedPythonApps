from PIL import Image
import numpy as np

class Canvas(object):
    """
    Image object created from the requested shape.

    Parameters
    ------------
    width : int
        Pixel horizontal width of the image to be saved
    height : int
        Pixel vertical height of the image to be saved
    color : array
        1-dimensional array of RGB color of image [R(0-255), B(0-255), G(0-255)]
    data : array[numpy]
        3-dimensional numpy array of image where x-dim is the width, y-dim is the height,
        and the z values of the array are the RGB colors of the rectangle
    
    Methods
    -------------
    draw()
        Draws canvas object based off of the shape definitions and image size and save to file name
    """

    def __init__(self, width:int, height:int, color:tuple):
        self.width = width
        self.height = height
        self.color = color
        
        # create colored image array for canvas
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # fill all dimensions with the solid color of choice
        self.data[:] = self.color

    def make(self, imagePath:str):
        """
        Save canvas as PNG
        """
        #convert numpy image array into RGB Image obj
        im = Image.fromarray(self.data, 'RGB')
        im.save(imagePath+'.png')
        return