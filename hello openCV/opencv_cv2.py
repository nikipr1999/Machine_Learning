import cv2
cap =cv2.VideoCapture(0)
while True:
	ret, frame=cap.read()    
	# The read() function returns the frame and the bool that is stored in ret 
	# ret contains true if frame is read else false
	
	if not ret:
		continue
	cv2.imshow("Feed",frame)
	# imshow() will show the frame in window named as Feed

	key=cv2.waitKey(0)
	# waitkey contains the milliseconds to hold each frame
	# if waitkey is 0 then it will close manually only
	# the word contained in ord() can also be used to shut that window

	if(key) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
# release will release the camera
# distroyAllWindows will destroy the window , which is not necessary but preferred
# generally the windows get destroyed itself as soon as the program terminates

