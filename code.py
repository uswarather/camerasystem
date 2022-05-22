import cv2
videocaptureobject=cv2.VideoCapture(0)
ret,frame=videocaptureobject.read()
cv2.imwrite("new image.jpg",frame)
videocaptureobject.release()
cv2.destroyAllWindows()