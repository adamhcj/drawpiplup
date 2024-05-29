import pyautogui
import math
import random
import numpy as np
import time
from pynput import keyboard

def scan(): # scan points, THINGS TO DO: SET STARTING POINT AND ENDING POINT AND THE SCANRATE
    spots = []
    startingpoint = (626, 217)
    endingpoint = (1150, 898)
    scanrate = 18 #how many pixels apart do you want to scan? 1 is too small
    for i in range(0, endingpoint[0] - startingpoint[0] + scanrate, scanrate): #for pixels within length of scanning, which is scanrate apart
        for j in range(0, endingpoint[1] - startingpoint[1] + scanrate, scanrate):#for pixels within height of scanning, which is scanrate apart
            pointcolour1 = pyautogui.pixel(startingpoint[0] + i, startingpoint[1] + j) #get RGB value of the spot
            percentdonex = i / (endingpoint[0] - startingpoint[0]) * 100 #percent of horizontal pixels done
            percentdoney = j / (endingpoint[1] - startingpoint[1]) * 100 #percent of vertical pixels done
            if percentdoney >= 95: 
                print(percentdonex, "%", percentdoney, "%")
            spots.insert(0, [(startingpoint[0] + i, startingpoint[1] + j), pointcolour1]) # insert the point coordinates, together with the RGB values
            #pyautogui.moveTo(startingpoint[0] + i, startingpoint[1] + j, _pause=0) #testing only, move mouse cursor to the point where the script added the spots values
            """if pointcolour1[0] == pointcolour1[1] == pointcolour1[2]:
                if pointcolour1[0] <= 100:
                    #print(i, j, pointcolour1)
                    spots.insert(0,[startingpoint[0] + i, startingpoint[1] + j])
                    #print(spots[0])"""
    print("scan completed!")
    print(spots)

scan()

