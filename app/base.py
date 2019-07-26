# -*- coding: utf-8 -*-

import cv2

class FaceDetect:

    @staticmethod
    def get_face():

        # 训练集位置
        cascPath = "haarcascade_frontalface_default.xml"

        # 读取训练集
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

            # print("Found {0} Faces! in the Picture".format(len(faces)))

            # 画框
            for (x, y, w, h) in faces:
                pixel_1 = int(w/2+x)
                pixel_2 = int(y-h/5)
                cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)
                cv2.putText(image, "face", (pixel_1,pixel_2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            cv2.imshow("Faces found", cv2.resize(image, (1024, 768)))
            if cv2.waitKey(1) == ord('q'):
                flag = 1
                break;



