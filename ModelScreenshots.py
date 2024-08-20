import cv2 # used to grant the computer vision
import numpy as np # will be used for training later
import pyautogui as pg # will be used to input controls
import pywinctl as gw # will focus the window
import os, shutil # used to access the game
import time # used for delay for the os
import win32gui
import keyboard

parent_pid = os.getpid()
WINDOW = 'Defend Your Castle Game Files - Crazy Games — Mozilla Firefox'
current_dir = os.getcwd()
positive_path = current_dir + "\\positive\\"
negative_path = current_dir + "\\negative\\"

def pressKey(key_to_press):
    for keys in key_to_press:
        pg.keyDown(keys)
    time.sleep(0.1)
    for keys in key_to_press:
        pg.keyUp(keys)

def clearDir(directory):
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    os.mkdir(current_dir + "\\" + directory)

flip = False

if __name__ == "__main__":
    game_window = gw.getWindowsWithTitle(WINDOW)[0]

    if game_window:
        time.sleep(1)
        game_window.activate()
        game_window.moveTo(0,0)

        handle = game_window.getHandle()
        rectC = win32gui.GetClientRect(handle)
        rect = win32gui.GetWindowRect(handle)
        x = abs(rectC[2] - rect[2]) // 2
        y = abs(rectC[3] - rect[3]) - x
        w = rectC[2]
        h = rectC[3]

        start_time = time.time()
        frames_processed = 0
        while game_window.isAlive:
            curr_time = time.time()
            frame = pg.screenshot(region=(x, y, w, h))
            frame = np.array(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            cv2.imshow('Computer Vision', frame)
            cv2_window = gw.getWindowsWithTitle('Computer Vision')
            cv2_window[0].moveTo(w, 0)

            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN and event.name == 'f':
                cv2.imwrite(positive_path + str(curr_time) + '.jpg', frame)
            if event.event_type == keyboard.KEY_DOWN and event.name == 'g':
                cv2.imwrite(negative_path + str(curr_time) + '.jpg', frame)
            if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
                cv2.destroyAllWindows()
                break
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break