# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:34:54 2021

@author: Hitesh
"""

import numpy as np
import pyautogui
import cv2
prev_pos="neutral"
def nothing(x):
    pass
vid=cv2.VideoCapture(0);
while True:
    _,frame=vid.read()
    frame=cv2.flip(frame,1)
    frame=cv2.GaussianBlur(frame,(5,5),0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    contours , hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(frame , contours , -1 , (0,0,255) , 2)
    max_contour=max(contours,key=cv2.contourArea)
    epsilon=0.01*cv2.arcLength(max_contour,True)
    approx=cv2.approxPolyDP(max_contour,epsilon,True)
    M=cv2.moments(approx)
    try:
        x=int(M['m10']/M['m00'])
        y=int(M['m01']/M['m00'])
    except ZeroDivisionError:
        continue
    frame=cv2.circle(frame,(x,y),10,(0,255,0),3)
    #frame=cv2.drawContours(frame,[approx],-1,(0,255,0),1)
    
    #cv2.imshow('cont frame',frame)
    frame=cv2.line(frame,(240,0),(240,640),(0,0,255),2)
    frame=cv2.line(frame,(360,0),(360,640),(0,0,255),2)
    frame=cv2.line(frame,(0,200),(640,200),(0,0,255),2)
    frame=cv2.line(frame,(0,250),(640,250),(0,0,255),2)
    cv2.imshow('for controls',frame)
    
    if x<240:
        curr_pos="left"
    elif x>360:
        curr_pos="right"
    elif y<200 and x>240 and x<360:
        curr_pos="up"
    elif y>300 and x>240 and x<360:
        curr_pos="down"
    else:
        curr_pos="neutral"
    if curr_pos!=prev_pos:
        if curr_pos !="neutral":
            pyautogui.press(curr_pos)
        prev_pos=curr_pos
    #cv2.imshow('contour',img)
    #cv2.imshow('frame',frame)
        #if y==1:
         #   img[::]=[b,g,r]
    #cv2.imshow('DIP',mask)
    q=cv2.waitKey(1)
    if q==ord('q'):
       break
vid.release()
cv2.destroyAllWindows()
    
