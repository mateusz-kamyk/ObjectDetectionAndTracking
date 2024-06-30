#!/usr/bin/env python3

import cv2

mouse = cv2.imread('./../image/black_mouse.png', 0)
camera = "/dev/video1"                     ####/dev/videoX

def mouse_detection_and_tracking():

    while True:
        image = cv2.VideoCapture(camera)           
        image.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        image.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        temp_w, temp_h = mouse.shape[::-1]

        print("""To close the "Video" window please press ESC.""")

        while True:
            ret, frame = image.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(gray, mouse, cv2.TM_CCOEFF_NORMED)
            frame_per_second = image.get(cv2.CAP_PROP_FPS)  
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            top_left = max_loc
            bottom_right = (top_left[0] + temp_w, top_left[1] + temp_h)
            detected = cv2.rectangle(gray, top_left, bottom_right, (255,0,0), 2)

            cv2.imshow('Video', detected)
            key = cv2.waitKey(1)
            if key == 27:
                cv2.destroyAllWindows()
                break

        break

if __name__=="__main__":
    mouse_detection_and_tracking()
