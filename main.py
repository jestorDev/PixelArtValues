from PIL import Image
import sys
import numpy as np


import matplotlib.pyplot as plt

import matplotlib.image as mpimg

height  , width =  int(sys.argv[2].split("x")[0] ), int(sys.argv[2].split("x")[1])


img  = Image.open(sys.argv[1])
pix  = img.load()
#print(img.size)

height_step = img.size[0]// 16
width_step = img.size[1]// 16


for i in range (height):
    for j in range(width):
        height_sample =  i*height_step + (height_step //2)
        width_sample = j*width_step + (width_step //2) 
        rgb  =  pix[height_sample ,width_sample]
        hex_rgb = "0x" + hex(rgb[0] )[2:].zfill(2) + hex(rgb[1] )[2:].zfill(2) + hex(rgb[2] )[2:].zfill(2) + " , "

        print(hex_rgb , end  = "")
    print("")

