# Imports
from PIL import ImageDraw, Image, ImageFont
import numpy as np


def plot_boxes(img, bboxes,names_, output):  # Write the required arguments
    img = Image.fromarray(np.uint8(img.transpose((1, 2, 0)) * 255))
    # we are doing this because originally we converted image to numpy array and then used img.transpose(2,1,0)/255
    #to convert back to image form transposing to original and multiply by 255
    for i in range(min(3, len(bboxes))): # number of rectangles must be lesser than 5 that to minimum--> if we could spot on 1-3 objects in image
        ImageDraw.Draw(img).rectangle(bboxes[i], outline='red', width=2) # draw rectangles
    for i in range(min(3, len(bboxes))):
        ImageDraw.Draw(img).text(bboxes[i][0], names_[i], fill='white') #labelling the boxes lables same as class names 
    img.save(output)
# The function should plot the predicted boxes on the images and save them.
# Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
