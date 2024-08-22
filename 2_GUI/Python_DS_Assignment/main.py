# Imports
from my_package.model import ObjectDetectionModel
from my_package.model import InstanceSegmentationModel
from my_package.data import Dataset
from my_package.analysis import plot_boxes
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image,ImageDraw
import PIL
import warnings

warnings.simplefilter("ignore", UserWarning)
def experiment(annotation_file, detector, segmentor, transforms, outputs):
    """
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    """

    My_dataSet = Dataset(annotation_file=annotation_file, transforms=transforms)
    # print(len(My_dataSet))
    # for i in range(len(My_dataSet)):
    #     print(My_dataSet[i]['image'])
    List_for_dataitems=[]
    for i in  range(0,My_dataSet.__len__()):
        List_for_dataitems.append(My_dataSet.__getitem__(i))

    List_for_predictions=[]
    for i in List_for_dataitems:
        List_for_predictions.append(segmentor.__call__(i["image"]))

    for img_idx in range(len(List_for_dataitems)):
        image = List_for_dataitems[img_idx]["image"]
        # mask = seg_store[img_idx][1][1]
        # image = image + mask
        # print(image)

        for index in range(min(5, len(List_for_predictions[img_idx][1]))):
            mask = List_for_predictions[img_idx][1][index]
            # print(type(mask))
            # mask = mask.sum(2)
            image = image + mask
            image2=image
        image = np.rollaxis(image, 2, 0)
        image = np.rollaxis(image, 2, 0)*255
        im = Image.fromarray(np.uint8((image)))
        img3=List_for_dataitems[img_idx]['image']
        img3 = Image.fromarray(np.uint8(img3.transpose((1, 2, 0)) * 255))
        # print(seg_store[img_idx][1][0].shape)

        # for index in range(min(3, len(seg_store[img_idx][1]))):
        #     top_left, bottom_right = seg_store[img_idx][0][index]
        #     # text = seg_store[img_idx][2][index] + \
        #     #     " ("+str(seg_store[img_idx][3][index])+")"
        #     text = seg_store[img_idx][2][index]
        #     draw.rectangle([top_left[0], top_left[1], top_left[0]+bottom_right[0],
        #                     top_left[1]+bottom_right[1]], outline='red', width=3)
        #     # print(text)
        #     draw.text([top_left[0], top_left[1]-10], text, fill="yellow")

        # im.show()
        im.save(f"output/{img_idx}my.jpg")

        for index in range(min(3, len(List_for_predictions[img_idx][1]))):
            top_left, bottom_right = List_for_predictions[img_idx][0][index]
            # text = seg_store[img_idx][2][index] + \
            #     " ("+str(seg_store[img_idx][3][index])+")"
            text = List_for_predictions[img_idx][2][index]
            ImageDraw.Draw(img3).rectangle([top_left[0], top_left[1], top_left[0]+bottom_right[0],top_left[1]+bottom_right[1]], outline='red', width=3)
            # print(text)
            ImageDraw.Draw(img3).text([top_left[0], top_left[1]-10], text, fill="pink")
        img3.save(f"output/box{img_idx}.jpg")
        # My_dataSet = Dataset1(annotation_file, transforms)
        # for i in range(len(My_dataSet)):
        #     pred_boxes, pred_class, pred_score = detector(My_dataSet[i]['image'])
        #     plot_boxes(My_dataSet[i]['image'], pred_boxes, pred_class, outputs + f'1/{i}.jpg')
        # _, my_image_height, my_image_width = My_dataSet[1]['image'].shape
        # Transformation_analysis_part = {'I0': ('Image', []),
        #                                 'I1': ('Flipped', [FlipImage()]),
        #                                 'I2': ('Blur', [BlurImage(4)]),
        #                                 'I3': (
        #                                 'Twice', [RescaleImage((int(2 * my_image_width), int(2 * my_image_height)))]),
        #                                 'I4': (
        #                                 'Half', [RescaleImage((int(my_image_width / 2), int(my_image_height / 2)))]),
        #                                 'I5': ('90 Right', [RotateImage(-90)]),
        #                                 'I6': ('45 Left', [RotateImage(45)])}
        #
        # for ind, item in enumerate(Transformation_analysis_part.items()):
        #     key, val = item
        #     My_dataSet.transforms = val[1]
        #     pred_boxes, pred_class, pred_score = detector(My_dataSet[1]['image'])
        #     plot_boxes(My_dataSet[1]['image'], pred_boxes, pred_class, outputs + f'2/{key}.jpg')
        #     plt.subplot(2, 4, ind + 1, title=val[0])
        #     plt.imshow(Image.open(outputs + f'2/{key}.jpg'))
        #
        # # plt.show()  # showing the combined subplots of an image
        # plt.savefig(outputs + 'subplots.png')  # saving in the .png sublplots
    # Do the required analysis experiments.

def main():
    detector = ObjectDetectionModel()
    segmentor = InstanceSegmentationModel()
    experiment('data/annotations.jsonl', detector, segmentor, [], 'output/')


if __name__ == '__main__':
    print("hello")
    main()
