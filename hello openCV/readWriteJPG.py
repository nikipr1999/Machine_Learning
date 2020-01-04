"""This program reads a JPG file then prints the matrix containing the 
pixels information.
Then writes the same file. 
"""

import cv2
k=cv2.imread('niki.jpg',0)  

""" imread() contains 2 arguments 
first is the JPG file to be read
second is the flag 0/1/-1
for 0 image will be in gray color
for 1 image will be colored
for -1 image is unchanged 

It returns the matrix if file path is correct else returns NONE. """ 

cv2.waitKey(0)
print(k)
#print(k) will print the matrix 

cv2.imshow('image',k)
cv2.waitKey(3000)
cv2.imwrite('niki_copy.png',k)