# Imports
from my_package.model import ObjectDetectionModel
from my_package.data import Dataset
from my_package.analysis import plot_boxes
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import matplotlib.pyplot as plt
from PIL import Image
import PIL
import warnings

warnings.simplefilter("ignore", UserWarning)
def experiment(annotation_file, detector, transforms, outputs):
    """
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        detector: The object detector
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    """

    My_dataSet = Dataset(annotation_file, transforms)
    # print(len(My_dataSet))
    # for i in range(len(My_dataSet)):
    #     print(My_dataSet[i]['image'])
    for i in range(len(My_dataSet)):
        # print(My_dataSet[i]['image'])
        # print("1 en")
        # print(detector(My_dataSet[i]['image']))
        # print(" 2 en")
        pred_boxes, pred_class, pred_score = detector(My_dataSet[i]['image'])
        # print(pred_boxes)
        # print("uuu")
        # print(pred_score)
        # print("FFFF")
        # print(pred_class)
        # print("CC")
        plot_boxes(My_dataSet[i]['image'], pred_boxes, pred_class, outputs + f'1/{i}.jpg')

    _, my_image_height, my_image_width = My_dataSet[1]['image'].shape
    Transformation_analysis_part = {'I0': ('Image', []),
                  'I1': ('Flipped', [FlipImage()]),
                  'I2': ('Blur', [BlurImage(4)]),
                  'I3': ('Twice', [RescaleImage((int(2 * my_image_width),int( 2 * my_image_height)))]),
                  'I4': ('Half', [RescaleImage((int(my_image_width / 2), int(my_image_height / 2)))]),
                  'I5': ('90 Right', [RotateImage(-90)]),
                  'I6': ('45 Left', [RotateImage(45)])}

    for ind, item in enumerate(Transformation_analysis_part.items()):
        key, val = item
        My_dataSet.transforms = val[1]
        pred_boxes, pred_class, pred_score = detector(My_dataSet[1]['image'])
        plot_boxes(My_dataSet[1]['image'], pred_boxes, pred_class, outputs + f'2/{key}.jpg')
        plt.subplot(2, 4, ind + 1, title=val[0])
        plt.imshow(Image.open(outputs + f'2/{key}.jpg'))

    plt.show() # showing the combined subplots of an image
    plt.savefig(outputs+'subplots.png') #saving in the .png sublplots


def main():
    detector = ObjectDetectionModel()
    experiment('data/annotations.jsonl', detector, [], 'output/')


if __name__ == '__main__':
    main()
