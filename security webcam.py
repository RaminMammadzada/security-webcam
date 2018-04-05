#if opencv was installed through home-brew on mac
#sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time
import datetime

from sendEmail import sendThroughEmail
from stringToImage import convertToImage

def rgb2gray(rgb_image):
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    return gray_image

def rgb2gray1(rgb_image):
    row,col,ch = rgb_image.shape

    gray_image = np.zeros((row, col))

    for i in range(row) :
        for j in range(col):
            gray_image[i,j] = ( rgb_image[i,j,0]*0.02989 + rgb_image[i,j,1]*0.5870 + rgb_image[i,j,2] *0.1140 ) #the algorithm i used id , G =  B*0.07 + G*0.72 + R* 0.21
                                                                               #I found it online
    return gray_image


def difference(img1_gray, img2_gray, row, column):
    print("row = ", row)
    print("column = ", column)
    local_difference = 0

    img1_gray = img1_gray/255
    img2_gray = img2_gray/255

    counter = 0

    for i in range(0, row, 10):
        for j in range(0, column, 10):
            local_difference = abs( np.sum(np.sum(img1_gray[i,j] - img2_gray[i,j])) )
            if(local_difference>0.17):
                counter = counter + 1
    return counter

def add_timestamp():
    time_now = str ( datetime.datetime.now() )

    convertToImage(time_now)

    simple_image = Image.open("simple_image.jpg")
    pix_simple_image = simple_image.load()

    date_image = Image.open("date_image.png") 
    pix_date_image = date_image.load()

    row_of_simple_image, col_of_simple_image = simple_image.size
    row_of_date_image, col_of_date_image = date_image.size

    for a in range( (row_of_simple_image - row_of_date_image), row_of_simple_image, 1):
        for b in range( (col_of_simple_image - col_of_date_image), col_of_simple_image, 1):
            if (pix_date_image[a-(row_of_simple_image - row_of_date_image),b-(col_of_simple_image - col_of_date_image)])[1] > 230:
                pix_simple_image[a,b] = pix_date_image[a-(row_of_simple_image - row_of_date_image),b-(col_of_simple_image - col_of_date_image)]
    

    simple_image.save("main_image.jpg")
    

    

def mainFunction():
    cam = cv2.VideoCapture(0)
    diff = 0
    while True:
        img1 = cam.read()[1]
        img1_gray = rgb2gray(img1)

        time.sleep(1)

        img2 = cam.read()[1]
        img2_gray = rgb2gray(img2)

        #cv2.imshow("Window",img2)

        row, column = img2_gray.shape
        diff = np.abs(difference(img1_gray, img2_gray, row, column))
        print("counter: ", diff)
        if diff > 10:
            print(diff)
            cv2.imwrite("simple_image.jpg", img1)
            add_timestamp()
            plt.imshow(img2_gray)
            sendThroughEmail()
            plt.show()
            break

mainFunction()