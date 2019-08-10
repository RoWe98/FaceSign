# -*- coding: utf-8 -*-

import cv2
from util import FaceUtil
class FaceDetect:

    @staticmethod
    def get_face():

        face_id_list = []

        # get training set file
        cascPath = "haarcascade_frontalface_default.xml"

        # load training set file
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        cap = cv2.VideoCapture(0)
        flag = 0

        while flag is not 1:
            ret, image = cap.read()
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            # print(str(faces))

            # print("Found {0} Faces! in the Picture".format(len(faces)))
            cv2.putText(image, "FaceNum:"+str(len(faces)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(image, "Press 'Ctrl+C' to Quit!", (250,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # draw the square
            for (x, y, w, h) in faces:
                pixel_1 = int(w/2+x)
                pixel_2 = int(y-h/5)
                cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)

                # if len(face_id_list):
                #     cv2.putText(image, "face:"+face_id_list[0], (pixel_1,pixel_2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                # else:
                cv2.putText(image, "face", (pixel_1, pixel_2), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2)
            cv2.imshow("Faces found", cv2.resize(image, (1024, 768)))

            if cv2.waitKey(1) == ord('s'):

                face_pixel = FaceUtil.get_face_pixel(faces)
                FaceUtil.screenshot(image,face_pixel)
                face_id = FaceUtil.lockopen()
                face_id_list.insert(0,face_id)

            # elif cv2.waitKey(1) == ord('q'):
            #     flag = 1
            #     break;


