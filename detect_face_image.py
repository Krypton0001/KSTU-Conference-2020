import cv2
from detectgui import *

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')



img = cv2.imread('our.jpg')
#img = cv2.imread('ya.jpg')
#img = cv2.imread('katkova.jpg')
#img = cv2.imread('ramatov.jpg')
#img = cv2.imread('saliev.jpg')
#img = cv2.imread('tsoi.jpg')
#img = cv2.imread('musina.jpg')
#img = cv2.imread('ten.jpg')
print(textImg)
#img = cv2.imread('egypt.jpg')
# Convert into grayscale
gray = cv2.cvtColor(cv2.UMat(img), cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 5)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 32, 250), 2)


# Display the output
# cv2.imshow('img', img)
# q = cv2.waitKey()
# if q == 27:
#     exit()

# import cv2 as cv
#
# cvNet = cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'graph.pbtxt')
#
# img = cv.imread('example.jpg')
# rows = img.shape[0]
# cols = img.shape[1]
# cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
# cvOut = cvNet.forward()
#
# for detection in cvOut[0,0,:,:]:
#     score = float(detection[2])
#     if score > 0.3:
#         left = detection[3] * cols
#         top = detection[4] * rows
#         right = detection[5] * cols
#         bottom = detection[6] * rows
#         cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)
#
# cv.imshow('img', img)
# q = cv.waitKey()
# if q == 27:
#     exit()