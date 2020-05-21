import numpy as np
import cv2

img = cv2.imread('shapes.PNG')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
