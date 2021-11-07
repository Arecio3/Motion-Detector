import cv2
# sets first frame = none to use it later
first_frame = None

# video obj with method for capturing video (0,1,2 = webcam or path to video)
# Trigger camera
video=cv2.VideoCapture(0)


# While Loop through Frame array and use imshow to show each frame in the array
while True:
    # Reads 1st Frame
    check, frame = video.read()

    # Converts color frame to Grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # make img blurry to remove noise (width,height of Gaussian kernel), standard deviation
    gray=cv2.GaussianBlur(gray,(21,21), 0)

    if first_frame is None:
        # sets first frame = to gray frame being rendered in loop
        first_frame = gray
        # makes python go to the beginning of the loop
        continue
    # compare background img with current frame / gives another img
    delta_frame=cv2.absdiff(first_frame,gray)
    # if pixel is less then 30 gets changed to white, Threshold Method returns a tuple we need 2nd item which is the frame
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # Smooth threshold frame
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)
    # Find Contours of thresh copy and store in cnts, draw extranal obj that will be finding in img, approx method CV applies for retrieving contours 
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Filter contour to only keep obj that has a contour area more then 1000px
    for contour in cnts:
        # if contour ares is less than 1000px go to next one
        if cv2.contourArea(contour) < 1000:
            continue
        # If greater than 1000px create rectangle x,y,w,h = rectangle params 
        (x,y,w,h) = cv2.boundingRect(contour)
        # Draw rectangle on color frame, (coord of upper left of rect), (coord of lower right of rect), (color), (width)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    # Created window and showed 1st frame of video
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Sniper Frame",frame)
    # Tells the script to wait for 1ms
    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame)
    print(thresh_frame)
    # if you press Q you quit
    if key == ord('q'):
        break

# release camera
video.release()
# Closes window
cv2.destroyAllWindows