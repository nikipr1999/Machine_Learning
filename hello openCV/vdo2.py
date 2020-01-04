"""This program simply reads the video, shows it in the window "hello" and also 
writes it in output3.avi"""

import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output3.avi',fourcc,20.0,(640,480)) 
# why it doesn't works on different window sizes??

while(cap.isOpened()):
	ret,frame=cap.read()
	cv2.imshow('hello',frame)
	out.write(frame)
	if cv2.waitKey(1)&0xFF==ord('q'):
		break
cap.release()
out.release()
cv2.destroyAllWindows()