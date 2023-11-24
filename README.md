## Project Description
This is the codebase for the autonomous gardening robot that I built and oversaw for the 2022-2023 academic year. The gardening robot is actuated by stepper motors and pumps, which are controlled by an Arduino Uno, and uses a webcam to detect plants, which is controlled by a Raspberry Pi. For more information about and photos of the project, see my [portfolio here](https://casperwong.weebly.com/interdisciplinary-projects.html)!

### How to run
For this code to be useful, you will need to build a robot gantry! If interested, the CAD files can be found in the repo, and all parts are either ordered from Amazon / McMaster-Carr or 3D printed. You can contact me for wiring schematics - we used TB6600 stepper drivers. 

1. Upload `_stepper/example.ino` to Arduino Uno
2. Run `imagge_detection/main.py` on Raspberry Pi
