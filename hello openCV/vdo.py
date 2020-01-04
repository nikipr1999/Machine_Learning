"""
This program activates the camera then shows two windows one in actual color
and other in gray color 
It also writes the video which is read in file named output.avi
"""

import cv2
cap=cv2.VideoCapture(0)  # opening camera

"""VideoCapture() takes input as 0 to activate the default camera, if we have 
multiple camera second camera will be 1 and so on"""

fourcc=cv2.VideoWriter_fourcc(*'XVID')  #??
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #writing the video

print(cap.isOpened())   # isOpened() returns true or false
while(cap.isOpened()):
	ret,frame=cap.read()
	if(ret==True):
		print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #prints width of frame 640
		print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  #prints height of frame 480
		out.write(frame)
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #convert color
		cv2.imshow('frame',gray)
		cv2.imshow('frame2',frame)
# two windows are shown one in actual color and one in gray color

		if cv2.waitKey(1)&0xFF==ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()