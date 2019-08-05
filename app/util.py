import cv2
import sys
import os
from facejudge import FaceDetect


face_id_list = []

class FaceUtil:

    @staticmethod
    def get_face_pixel(faces):
        
        face_pixel = []
        for (x, y, w, h) in faces:
            face_pixel.append(x)
            face_pixel.append(y)
            face_pixel.append(w)
            face_pixel.append(h)
        return face_pixel

    @staticmethod
    def screenshot(frame,face_pixel):
        print(face_pixel)
        saveface = frame[face_pixel[1]:face_pixel[1]+face_pixel[2],face_pixel[0]:face_pixel[0]+face_pixel[2]]
        cv2.imwrite("../image/face.jpg",saveface)
        print("face saved")

    
    @staticmethod
    def lockopen():

        facedetect = FaceDetect()
        face_flag, face_id = facedetect.face_judge()
        face_id_list.append(face_id)

        if face_id not in face_id_list:

            if(face_flag):
                print("人脸识别成功，开始解锁")

        else:

            print("已经识别完成，id为:"+face_id)
            return face_id