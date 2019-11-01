import cv2

from datetime import datetime

cam = cv2.VideoCapture(0) #selecting camera feed
cam.set (cv2.CAP_PROP_FPS, 60) #set frame rate
cam.set(3, 1280) # set x resolution
cam.set(4, 720) # set y resolution

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX # set font

fourcc = cv2.VideoWriter_fourcc(*'XVID') # set codec (*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, 15, (1280, 720))
while True:
    ret, img = cam.read() # set camera read

    img = cv2.flip(img, 1) # flip image

    cv2.putText(img, "You are being recorded", (200, 300), font, 1.5, (150, 100, 10), 2, cv2.LINE_AA)
    cv2.putText(img, str(datetime.now()), (900, 650), font, .5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Security', img) # Display window

    out.write(img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # wait for ESC key to end loop
        break

cam.release() #
cv2.destroyAllWindows()