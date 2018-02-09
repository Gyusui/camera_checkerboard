# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:05:33 2017

@author: 牛帥
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def readCamera():
    cap = cv2.VideoCapture(0) #Videoを利用する
    cap.grab()
    while(cap.isOpened()):
	    ret, frame = cap.read()
	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
              cv2.imwrite("frame.png", frame)
              break

    cap.release()
    #cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    readCamera()
    image = cv2.imread("frame.png")
    ret, corners = cv2.findChessboardCorners(image, (10, 7))
    #ret, corners = cv2.findChessboardCorners(image, (5, 9))
    #ret, centers = cv2.findCirclesGrid(image, (12, 8))
    cv2.drawChessboardCorners(image,(10, 7),corners,ret)
    #cv2.drawChessboardCorners(image, (12, 8), centers, ret)
    cv2.imshow("corners",image)
    cv2.imwrite("picture.png", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()