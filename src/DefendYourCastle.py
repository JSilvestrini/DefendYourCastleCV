import cv2 # computer vision
import numpy as np # will be used for training later
import pyautogui as pg # will be used to input controls
import pywinctl as gw # will focus the window
import os # used to access the game
import sys
import time # used for delay for the os
import win32gui # used to get the size of the client in the window

WINDOW = 'Defend Your Castle Game Files - Crazy Games — Mozilla Firefox'
current_dir = os.getcwd()
stickClassifier = cv2.CascadeClassifier(current_dir + "\\cascade.xml")

def main():
    show_image = False
    if sys.argv[1].capitalize() == 'True':
        show_image = True
    # Get the Window
    time.sleep(1)
    game_window = gw.getWindowsWithTitle(WINDOW)[0]

    if not game_window:
        return 0
    time.sleep(1)

    # Resize Window, Make it Main
    game_window.activate()
    game_window.moveTo(0,0)
    game_window.resizeTo(1080, 1080)

    # Grab Some X and Y Info
    handle = game_window.getHandle()
    rectC = win32gui.GetClientRect(handle)
    rect = win32gui.GetWindowRect(handle)
    x = abs(rectC[2] - rect[2]) // 2
    y = abs(rectC[3] - rect[3]) - x + 400
    halfPointY = y / 2
    w = rectC[2]
    h = int(rectC[3] / 2)

    while game_window.isAlive:
        # Screenshot and Use Classifier
        frame = pg.screenshot(region=(x, y, w, h))

        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stick = stickClassifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=24, minSize=(12,12))

        # For Stick Figure in Classifier
        for (xx, yx, wx, hx) in stick:
            if yx > halfPointY:
                nx = xx + wx
                ny = yx + (hx / 2) + 400
                pg.moveTo(x = nx, y = ny)
                pg.dragRel(yOffset = -500)
                pg.moveTo(x = nx, y = ny)

        # Show the Frame
        if show_image:
            cv2.imshow('Computer Vision', frame)
            cv2_window = gw.getWindowsWithTitle('Computer Vision')
            cv2_window[0].moveTo(w, 0)

            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break

if __name__ == "__main__":
    main()