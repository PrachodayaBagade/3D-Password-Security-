
import dlib,cv2
import numpy as np
from facePoints import facePoints


def take_image(User_name):

    frontalFaceDetector = dlib.get_frontal_face_detector()
    faceLandmarkDetector = dlib.shape_predictor("facial_landmarks.dat")
    cap = cv2.VideoCapture(0)
    itr = 0

    while True:
        ret, img = cap.read()

        imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        allFaces = frontalFaceDetector(imageRGB, 0)

##        print("Number of Faces found : ",len(allFaces))

        if(len(allFaces) == 1):
            itr += 1
            if itr == 20:
                cv2.imwrite('./data/' + User_name + '.png',img)

                allFacesLandmark = []

                for k in range(0, len(allFaces)):
                    faceRectangleDlib = dlib.rectangle(int(allFaces[k].left()),int(allFaces[k].top()),int(allFaces[k].right()),int(allFaces[k].bottom()))
                    detectedLandmarks = faceLandmarkDetector(imageRGB, faceRectangleDlib)
                    facePoints(img, detectedLandmarks)
                cv2.imshow("Face Detection Result", img)
                cv2.waitKey(1000)
                break

        allFacesLandmark = []

        for k in range(0, len(allFaces)):
          faceRectangleDlib = dlib.rectangle(int(allFaces[k].left()),int(allFaces[k].top()),
              int(allFaces[k].right()),int(allFaces[k].bottom()))

          detectedLandmarks = faceLandmarkDetector(imageRGB, faceRectangleDlib)

          # Now finally we drawing landmarks on face
          facePoints(img, detectedLandmarks)
        cv2.imshow("Face Detection Result", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break


    cap.release()
    cv2.destroyAllWindows()

##take_image('dm')
