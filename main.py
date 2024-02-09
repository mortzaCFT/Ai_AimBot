#  Simple Aimbot source code, for train apps for detection.
#  This code will work with yolov5 and opencv for detection and when the trained object is detected, it's move the mouse on center of the object and clikcs.
# This shit, is my base idea of my own peremium cheat... it's has a lot of other things that make it best undetect cheat on the world!
# Wati for it...
#__Creator mortzaCFT for public using.__ 

import cv2
import numpy as np
import win32gui
import pyautogui
    
# Get the handle of the application window
# Use this function to get overall.
hwnd = win32gui.FindWindow(None, '____Application Window Title____')

# Define the object detection algorithm
net = cv2.dnn.readNetFromDarknet("path/to/yolov5.cfg", "path/to/yolov5.weights")

# Define the window size
window_size = (416, 416)


class_id = 0  

while True:
    # Get the dimensions of the application window
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    # Capture the screen of the application window
    screenshot = np.array(cv2.cvtColor(np.array(ImageGrab.grab(bbox=(left, top, right, bottom))), cv2.COLOR_RGB2BGR))

    screenshot = cv2.resize(screenshot, window_size)

    # Detect objects in the screenshot
    blob = cv2.dnn.blobFromImage(screenshot, 1.0, window_size, (0, 0, 0), True, False)
    net.setInput(blob)
    detections = net.forward()

    for detection in detections:
        class_id = detection[5]
        if class_id == class_id:

            x, y, w, h = detection[0:4] * np.array([width, height, width, height])
            center_x = x + w // 2
            center_y = y + h // 2

            # Simulate a mouse click at the center of the object(I mean center of the head... or rather part of body.)
            pyautogui.moveTo(center_x, center_y)
            pyautogui.click()

    if cv2.waitKey(1) == 27:  
        break

cv2.destroyAllWindows()
