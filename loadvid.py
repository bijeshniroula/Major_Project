import cv2
import numpy

isValid = True
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('Mouth.xml')

video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("cant open the camera")
while True:
    try:
      ret, frame = video_capture.read()
    except:
     print("error in taking image")
     isValid = False
    if isValid == True:
     try:
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = faceCascade.detectMultiScale(gray, 1.3, 5)
      for (x, y, w, h) in faces:
          cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0, 0),2)
          roi_gray = gray[y:y+h, x:x+w]
          roi_color = frame[y:y+h, x:x+w]

      eyes = eye_cascade.detectMultiScale(roi_gray)
      for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


      mouth = mouth_cascade.detectMultiScale(roi_gray)
      for (ex,ey,ew,eh) in mouth:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('r'):
       break
     except:
      pass
video_capture.release()
cv2.destroyAllWindows()
