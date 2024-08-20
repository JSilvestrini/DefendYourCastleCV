# DefendYourCastleCV

This was a quick project that I originally started in April of 2024, but ended up not uploading due to concerns about the FPS and runtime of the project, which I will address within the [Potential Ajustments](#potential-adjustments) section.

This project uses computer vision and a Haar cascade model that was trained using the tools from OpenCV.

## Table of Contents

-   [**Installation**](#installation)
-   [**How To Use**](#how-to-use)
-   [**Potential Adjustments**](#potential-adjustments)

## Installation

To install and use this project you need to make sure that you have the required libraries installed for Python. This project was made to run on a Windows system since some of the pywinctl functionality is OS specific and win32gui is specifically for Microsoft systems.

-   OpenCV
-   numpy
-   pyautogui
-   pywinctl
-   win32gui

Finally, the program currently looks for a specific version of the "Defend Your Castle" window, which I opened using Mozilla's frame opening capabilities.

## How To Use

```bash
python .\ModelScreenshots.py
```

This file is used to collect images for the negative and the positive folders. It will create the directories for you and if you press either f or g, it will take a screenshot of the game window and place it within either the positive folder or negative folder respectively.

To get the most use out of this I would recommend learning how to use [OpenCV](https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html) and their tools to create your own classifier, as this file was for utility purposes.

```bash
python .\FileCleaner.py
```

This file was used to parse the positive and negative folders and ensure that there were no spaces. It also generates the negative file that is used for training a Haar classifier using [OpenCV](https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html).

```bash
python .\DefendYourCastle.py <True | False>
```

This is the main file of the program, and with it is also an already trained Haar classifier. This program will locate the window of the "Defend Your Castle" game, in this case: 'Defend Your Castle Game Files - Crazy Games — Mozilla Firefox'.

To obtain the screen like this, just find the game through some website on Mozilla Firefox, like CrazyGames, right click the game screen, hover over "this frame", then "open frame in new window."

The program will then play the game for you, the only input you need to make is to start the game and advance to the next level after one has been completed.

The optional system argument will show you the OpenCV frame that the computer is using if set to True.

## Potential Adjustments

I personally found the speed of the computer vision to be slow, and it led me to initially not upload it. This also led me down a rabbit hole of ways to solve the framerate issue, such as creating the program again in C/C++, which would do little since OpenCV uses Python wrappers to call code that is already written in C.

In the future I think that there are a few options to speed the program up:

1. Utilize threading for mouse control to separate it from the OpenCV code
2. Build OpenCV using CMake in order to gain access to CUDA support, which may be the best bet for increasing the speed at which the program runs.
3. Rewrite the code in C/C++ since there could be potential speed increases based on the other libraries that are being utilized, but more research would need to be done to see if these libraries are also using Python wrappers on C/C++ code.
