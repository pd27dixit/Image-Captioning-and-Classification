# Imports
import numpy as np


class CropImage(object):
    """
        Performs either random cropping or center cropping.
    """

    def __init__(self, shape, crop_type='center'):
        """
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        """

        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        """
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        """
        x, y = image.size   #use width for x and height for y
        if self.crop_type == 'center':
            x = int(x/2)
            y = int(y/2)
            left=int(self.shape[1]/2)
            right=int(self.shape[1]/2)
            top=int(self.shape[0]/2)
            bottom=int(self.shape[0]/2)
            
            final_left = x - left
            final_top = y - top
            final_right = x + right
            final_bottom = y + bottom
            return image.crop((final_left,final_top, final_right, final_bottom))

        else:
            left = np.random.randint(0, x - self.shape[1])
            upper = np.random.randint(0, y - self.shape[0])
            return image.crop((left, upper, left + self.shape[1], upper + self.shape[0]))





