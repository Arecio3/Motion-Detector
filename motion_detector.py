import cv2
# video obj with method for capturing video (0,1,2 = webcam or path to video)
# Trigger camera
video=cv2.VideoCapture(0)


# While Loop through Frame array and use imshow to show each frame in the array
while True:
    # Frame obj for showing window which reads video obj
    # check = bool / frame = 3D numpy array which rep img (first frame vid captures)
    # Reads 1st Frame
    check, frame = video.read()

    print(check)
    print(frame)


    # Converts frame to Grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Created window and showed 1st frame of video
    cv2.imshow("Capturing",gray)
    # Tells the script to wait for 1ms
    key=cv2.waitKey(1)
    # if you press Q key it stops the loop
    if key == ord('q'):
        break

# release camera
video.release()
# Closes window
cv2.destroyAllWindows