import numpy as np
import cv2

img = cv2.imread('shapes.PNG')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
