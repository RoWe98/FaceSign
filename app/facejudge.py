import cv2
from aip import AipFace
import base64

class FaceDetect:

    def __init__(self):

        APP_ID_FACE = '15764893'
        API_KEY_FACE = 'rHGwsXanKC4yWj4pXeepDZcc'
        SECRET_KEY_FACE = 'qMONYxM1xTwnQh2q0DsHB7YG5Ht9LOal'
        self.imageType = "BASE64"
        self.groupIdList = "wisdom_class,1"  # 人脸库的名字和id
        # 实例化人脸分析搜索对象
        self.client_baidu_face = AipFace(APP_ID_FACE, API_KEY_FACE, SECRET_KEY_FACE)
        self.face_path = "../image/face.jpg"

    def face_judge(self):
        # try:
        image = base64.b64encode(open(self.face_path, 'rb').read())
        result = self.client_baidu_face.search(image, self.imageType, self.groupIdList);
        face_id = result['result']['user_list'][0]['user_id']  # 对JSON进行分析获取图片ID(学号
        print(face_id)
        return True, face_id
        # except Exception:
        #    pass