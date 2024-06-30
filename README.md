# Object Detection And Tracking

This program is designed to detect the object indicated in the photo on the live video from the camera.

## Prerequisites
- python 3.x
- opencv-python 4.10.x

## How to start
You have to specify which object program has to detect and track. You also have to provide camera path. 
Run the script by executing:

`./src/main.py --filename path_to_object_photo.png --camera path_to_camera`

Example:

`./src/main.py --filename ./../image/black_mouse.png --camera /dev/video2`

To see more, execute:

`./src/main.py --help`
