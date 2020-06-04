#Face Detection Using Opencv and Python
import cv2

#Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img= cv2.imread(r'C:\Users\aayus\Desktop\test.jpg')
img= cv2.resize(img,(500,500))
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detect Faces
faces= face_cascade.detectMultiScale(gray,1.1,4)

#Draw rectangle around faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)

cv2.imshow('image',img)
cv2.waitKeyEx()