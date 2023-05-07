# Home-Automation-using-Hand-Gestures

## Objective
This project is aim towards building a Gesture Based Home automation solution

## About the Project
Gesture based home automation using Arduino, Python, OpenCV, and Mediapipe is a combination of technologies that can be used to create a smart home. Arduino can be used to build a system that can detect and interpret gestures. Python can be used to program the system and OpenCV can be used to recognize gestures. Mediapipe can be used to create a virtual assistant that can respond to gestures and provide feedback. With these technologies, you can create a home automation system that responds to gestures, enabling you to control your home with a wave of your hand.

### How to use?
This repo has two files, one is [HandTackModule](https://github.com/volstice/Home-Automation-using-Hand-Gestures/blob/782379ce0f991535f62b6ce351d6cd277a465b7e/HandTrackModule.py) and the other is [LedHandControl](https://github.com/volstice/Home-Automation-using-Hand-Gestures/blob/782379ce0f991535f62b6ce351d6cd277a465b7e/LedHandControl.py)

[HandTackModule](https://github.com/volstice/Home-Automation-using-Hand-Gestures/blob/782379ce0f991535f62b6ce351d6cd277a465b7e/HandTrackModule.py) is used as a package to actually track the fist by diving the fist into 21 tracking landmarks upon which it can be used in various other project.

[LedHandControl](https://github.com/volstice/Home-Automation-using-Hand-Gestures/blob/782379ce0f991535f62b6ce351d6cd277a465b7e/LedHandControl.py), is the file where [HandTackModule](https://github.com/volstice/Home-Automation-using-Hand-Gestures/blob/782379ce0f991535f62b6ce351d6cd277a465b7e/HandTrackModule.py) is called and the functionality of the gesture recognition is processed. 

And to communicate with the arduino so that the light or any other device which is required to be controlled we use the [TemplateFile](https://github.com/volstice/Home-Automation-using-Hand-Gestures/blob/782379ce0f991535f62b6ce351d6cd277a465b7e/templateFile.ino) which uses [CVZONE](https://github.com/cvzone/cvzone) library. [TemplateFile](https://github.com/volstice/Home-Automation-using-Hand-Gestures/blob/782379ce0f991535f62b6ce351d6cd277a465b7e/templateFile.ino) is uploaded into arduino and the other data is hereafter fetched from python after image processing.


