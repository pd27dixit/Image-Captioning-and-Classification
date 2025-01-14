# Imports
from PIL import ImageFilter


class BlurImage(object):
    """
        Applies Gaussian Blur on the image.
    """

    def __init__(self, radius):
        """
            Arguments:
            radius (int): radius to blur
        """

        self.radius = radius # self similar to this in c++

    def __call__(self, image):
        """
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        """

        return image.filter(ImageFilter.GaussianBlur(radius=self.radius)) # here we are blurring the
    # image numpy array to the radius given in constructor of this class
