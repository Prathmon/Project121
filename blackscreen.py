import numpy as np
import cv2

cap = cv2.VideoCapture(0)

for i in range(60):
  ret,frame = cap.read()

frame = np.flip(frame,axis = 1)
frame = cv2.resize(frame, (640, 480))

while(cap.isOpened()):
  ret, image = cap.read()
  if not ret:
    break

  image = np.flip(image, axis = 1)
  image = cv2.resize(image, (640, 480))

  u_black = np.array([104, 153, 70])
  l_black = np.array([30, 30, 0])

  mask = cv2.inRange(frame, l_black, u_black)
  res = cv2.bitwise_and(frame, frame, mask = mask)

  f = frame-res
  f = np.where(f == 0, image, f)

cap.release()
out.release()
cv2.destroyAllWindows()