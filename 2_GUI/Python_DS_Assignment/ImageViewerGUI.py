from tkinter import *
from PIL import ImageTk,Image,ImageEnhance
from tkinter import filedialog

from Python_DS_Assignment.main import experiment
from my_package.model import InstanceSegmentationModel
from my_package.model import ObjectDetectionModel
# from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
# from my_package.data.dataset import Dataset
# from my_package.data.dataset import Dataset1
# from my_package.data.transforms.blur import BlurImage
# from my_package.data.transforms.flip import FlipImage
# from my_package.analysis import plot_boxes
# from my_package.data.transforms.rescale import RescaleImage
# from my_package.data.transforms.crop import CropImage
# from my_package.data.transforms.rotate import RotateImage
# import numpy as np
from PIL import Image, ImageDraw
# import matplotlib.pyplot as plt
# import warnings

val=2
process_val=0
def setting_val_for_Seg_or_Boun():
    global val
    if drop_down.get() == "Segmentation": #if drop menu has Segmentation val=1
        # Label(root, text="Chose 1").grid(row=1, column=0)

        # value = "Segmentation"
          val=1
    else: #if drop menu has Bounding box  val=1
        # Label(root, text="Chose 2").grid(row=1, column=0)
        # value="Bounding"
        val=0
def intermediate_step(clicked):
    if e.get()=="": #if input field is empty
        # Label(root,text="some").grid(row=2,column=0)
        print("Select a file first:\n")
    else:
        # Label(root, text="none").grid(row=2, column=0)
        setting_val_for_Seg_or_Boun() # find whether Seg/Bound
        process(clicked) # clicked is number stored
def process(clicked):

    window_new=Toplevel() #new window creation for displaying images
    window_new.title('Displaying images')
    global my_img1
    global my_img2
    global val
    print(val)
    # if(value=="Segmentation"):
    if (val == 1):
        # window_new = Toplevel()
        # window_new.title('Displaying images')
        my_img1 = ImageTk.PhotoImage(Image.open(f"C:/Users/HP/Desktop/My_A/Asg4/Python_DS_Assignment/data/imgs/{clicked}.jpg"))
        my_img2 = ImageTk.PhotoImage(Image.open(f"C:/Users/HP/Desktop/My_A/Asg4/Python_DS_Assignment/output/{clicked}my.jpg"))
        Label(window_new, image=my_img1, text=f"Image{clicked + 1}").grid(row=1, column=0, padx=20, pady=40)
        l2=Label(window_new, image=my_img2,text=f"Image{clicked + 1}")
        l2.grid(row=1, column=1, padx=20, pady=40)
    elif(val==0):

        my_img2 = ImageTk.PhotoImage(Image.open(f"C:/Users/HP/Desktop/My_A/Asg4/Python_DS_Assignment/output/box{clicked}.jpg"))
        my_img1 = ImageTk.PhotoImage(Image.open(f"C:/Users/HP/Desktop/My_A/Asg4/Python_DS_Assignment/data/imgs/{clicked}.jpg"))
        # my_img2 = ImageEnhance.Sharpness(my_img2)
        # my_img2 = my_img2.enhance(2)
        # my_img2 = my_img2.transpose(PIL.Image.FLIP_LEFT_RIGHT)
        Label(window_new,image=my_img1, text=f"Image{clicked + 1}").grid(row=1, column=0, padx=20, pady=40)
        Label(window_new,image=my_img2).grid(row=1, column=1, padx=20, pady=40)
    window_new.mainloop()

def fileClick():
    global my_image
    global my_img1
    global my_img2
    global process_val
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/HP/Desktop/My_A/Asg4/Python_DS_Assignment/data/imgs", title="Select a file ",
                                               filetypes=( ("jpg files", "*.jpg"),("all files", "*.*")))
    # my_label = Label(root, text=root.filename).pack()
    # root.filename has address of the selected image
    my_image = ImageTk.PhotoImage(Image.open(root.filename)) # my_image is image stored at root.filename
    e.delete(0,END)  #input field deletes the last entry
    e.insert(0,root.filename)

    index_found=int(root.filename.find("imgs/"))
    # print(index_found + 5)
    clicked=int(root.filename[index_found+5]) #61 is index of image number in file name
    process_val=clicked;  #process_val has same number
    intermediate_step(clicked)
    # new_Win(i)
    # my_img1 = ImageTk.PhotoImage(Image.open(f"/Users/HP/PycharmProjects/Tkinter/output/box{i}.jpg"))
    # my_img2 = ImageTk.PhotoImage(Image.open(f"/Users/HP/PycharmProjects/Tkinter/output/{i}my.jpg"))
    # Label(image=my_img1, text=f"Image{i + 1}").grid(row=1, column=0,padx=20,pady=400)
    # Label(image=my_img2).grid(row=1, column=1,padx=20,pady=400)
    # Label(image=my_image).grid(row=1,column =1)

if __name__ == '__main__':
    root = Tk()
    root.title('SW Lab | IIT KGP | Image Viewer')

    # segmentor = InstanceSegmentationModel()  // implementing these lines in main.py and importing it to increase running time
    # detector = ObjectDetectionModel()
    #
    # experiment('./data/annotations.jsonl', detector, segmentor,
    #            [], 'output/')

    e = Entry(root, width=70)  # input field used
    e.grid(row=0, column=0)

    my_btn = Button(root, text="...", command=fileClick).grid(row=0, column=1) #first button
    # my_b2=Button(root,text="Segmentation")

    options = ["Segmentation", "Bounding-box"]
    drop_down = StringVar()  #using drop menu
    # root.geometry("400x400")

    drop_down.set(options[0])
    drop = OptionMenu(root, drop_down,options[0],options[1])
    drop.grid(row=0, column=2)
    # show()

    my_b3 = Button(root, text="Process", command=lambda: intermediate_step(process_val)) #middle stage

    my_b3.grid(row=0, column=3)

    root.mainloop()
