import cv2

first_frame = None

# video obj with method for capturing video (0,1,2 = webcam or path to video)
# Trigger camera
video=cv2.VideoCapture(0)


# While Loop through Frame array and use imshow to show each frame in the array
while True:
    # Frame obj for showing window which reads video obj
    # check = bool / frame = 3D numpy array which rep img (first frame vid captures)
    # Reads 1st Frame
    check, frame = video.read()

    # Converts frame to Grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # make img blurry to remove noise (width,height of Gaussian kernel), standard deviation
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        # sets first frame = to gray frame being rendered in loop
        first_frame = gray
        # makes python go to the beginning of the loop
        continue
    # compare background img with current frame / gives another img
    delta_frame=cv2.absdiff(first_frame,gray)

    # Created window and showed 1st frame of video
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    # Tells the script to wait for 1ms
    key=cv2.waitKey(1)
    print(gray)
    # if you press Q key it stops the loop
    if key == ord('q'):
        break

# release camera
video.release()
# Closes window
cv2.destroyAllWindows