import cv2 as c
face_cascade=c.CascadeClassifier('haarcascade_frontalface_default.xml')
img=c.imread("PROFILE PHOTO.jpeg")
img=c.resize(img,(480,430))
gray = c.cvtColor(img, c.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5, 1, (30, 15))
for (x,y,h,w) in faces:
    c.rectangle(img, (x, y), (x + h, x + w), (225, 0, 225), 2)
c.imshow("img", img)
c.waitKey()