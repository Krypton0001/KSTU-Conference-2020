import cv2
import numpy

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#face_cascade = 'haarcascade_frontalface_default.xml'

# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')
class DetectFaceCam:
    def runCam():
        while True:
            # Read the frame
            flag, videocv = cap.read()
            videocv = cv2.flip(videocv, 1)
            try:
                # Convert to grayscale
                gray = cv2.cvtColor(videocv, cv2.COLOR_BGR2GRAY)

                # Detect the faces
                faces = face_cascade.detectMultiScale(gray, 1.1, 3)
                # Draw the rectangle around each face
                for (x, y, w, h) in faces:
                    cv2.rectangle(videocv, (x, y), (x + w, y + h), (255, 30, 250), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = videocv[y:y + h, x:x + w]
                    # draw bounding boxes around detected features

                # Display
                cv2.imshow('Detect face', videocv)
            except:
                cap.release()
                raise

            # Stop if escape key is pressed
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break

        # Release the VideoCapture object
        cv2.destroyAllWindows()
        cap.release()


