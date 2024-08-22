# Imports
import json
from typing import List, Any

from PIL import Image
import numpy as np


class Dataset(object):
    """
        A class for the dataset that will return data items as per the given index
    """

    def __init__(self, annotation_file, transforms=None):
        """
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        """
        self.annotation_file = annotation_file
        self.transforms = transforms
        self.data = []  # empty list
        with open(annotation_file) as f:  #we could also use open(file), close(file) but to handle all exceptions and not to write close() we are using with statement
            for line in f.readlines():  # f.readlines() make each line an item of list  ,for every element in this list
                self.data.append(json.loads(line)) #storing each line as elements of list data



    def __len__(self):
        """
            return the number of data points in the dataset
        """

        return len(self.data) #returns length of list data

    def __getitem__(self, idx):
        """
            return the dataset element for the index: "idx"
            Arguments:
                idx: index of the data element.

            Returns: A dictionary with:
                image: image (in the form of a numpy array) (shape: (3, H, W))
                gt_bboxes: N X 5 array where N is the number of bounding boxes, each
                            consisting of [class, x1, y1, x2, y2]
                            x1 and x2 lie between 0 and width of the image,
                            y1 and y2 lie between 0 and height of the image.

            You need to do the following,
            1. Extract the correct annotation using the idx provided.
            2. Read the image and convert it into a numpy array (wont be necessary
                with some libraries). The shape of the array would be (3, H, W).
            3. Scale the values in the array to be with [0, 1].
            4. Create a dictionary with both the image and annotations
            4. Perform the desired transformations.
            5. Return the transformed image and annotations as specified.
        """
        img = Image.open('./data/' + self.data[idx]['img_fn']) #specifying exact location of annotation file
        for x in self.transforms:
            img = x(img) # transformations on image
        img_array = np.asarray(img).transpose((2, 0, 1))/255 #converting to numpy array of shape(3,H,W)
        #dividing by 255 scales value between 0 and 1

        annotations = []
        for x in self.data[idx]['bboxes']:   
            annotations.append([x['category']] + x['bbox']) # category:' ' bbox:' '

        return {'image': img_array, 'gt_bboxes': annotations} 
