import numpy as np
import cv2
import time
import os
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox


video_capture_1 = cv2.VideoCapture(1)
video_capture_2 = cv2.VideoCapture(2)

img_counter2 = 0
img_counter = 0

 
def cam1():
    
    ret1, frame1 = video_capture_1.read()
    if (ret1):
        # Display the resulting frame
        cv2.imshow('Cam 0', frame1)
    
    
        # SPACE pressed
        img_name1 = "img{}.jpg".format(img_counter)
        path = r'C:\Users\Vaibhav Neharkar\Documents\opencv\cam_1'
        cv2.imwrite(os.path.join(path , img_name1), frame1)
        print("{} written!".format(img_name1))
       # cv2.imshow('pic',frame1)
        
       
       #detection and calculation algorithm
        im = cv2.imread(os.path.join(path , img_name1))
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        plt.imshow(output_image)
        plt.show()
        print('Number of cars in the image1 is  '+ str(label.count('car')))


def cam2():
    
   
    ret2, frame2 = video_capture_2.read()
    if (ret2):
        # Display the resulting frame
        cv2.imshow('Cam2 ', frame2)
        
    
        # SPACE pressed
        img_name2 = "img1{}.jpg".format(img_counter2)
        path = r'C:\Users\Vaibhav Neharkar\Documents\opencv\cam_2'
        cv2.imwrite(os.path.join(path , img_name2), frame2)
        print("{} written!".format(img_name2))
        #cv2.imshow('pc', frame2)
        
       # detection and calculation algorithm
        im = cv2.imread(os.path.join(path , img_name2))
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        plt.imshow(output_image)
        plt.show()
        print('Number of cars in the image 2 is '+ str(label.count('car')))

i =0
while i < 3:
    

    cam1()
    cam2()
    img_counter+= 1
    img_counter2 += 1
    time.sleep(3)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break
    i+=1
# When everything is done, release the capture
video_capture_1.release()
video_capture_2.release()
cv2.destroyAllWindows()