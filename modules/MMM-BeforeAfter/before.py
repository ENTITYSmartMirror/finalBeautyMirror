import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imshow('frame', frame)
cv2.imwrite('/home/pi/Desktop/BeautyMirror/modules/MMM-BeforeAfter/before/before.jpg', frame)

cap.release()
cv2.destroyAllWindows()
print("python success !")
