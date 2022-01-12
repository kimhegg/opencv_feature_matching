import threading
import cv2
import time
from initiator import Initiator
from tesseract.ocr import OCR
from opencv.orb_feature_matching import FeatureMatching
from opencv.sift_feature_matching import Sift_detector


if __name__ == '__main__':
    def videoCapture(saveFrames=False):
        capture = cv2.VideoCapture(0)
        capture.set(3, 640)
        capture.set(4, 480)
        interval_sec = 0.01
        start_time = time.time()
        while True:
            ret, frame = capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if time.time() - start_time >= interval_sec: #trick to do operations at a certain interval
                if saveFrames:
                    saveFile(frame)
                    readFromFilesystemStrategy()

                sift_detector(frame)
                start_time = time.time()


    vc = threading.Thread(target=videoCapture)
    vc.start()


    def saveFile(frame):
        now = int(time.time())
        img_name = "data/opencv_frame_{}.png".format(now)
        cv2.imwrite(img_name, frame)


    def ocr_analyze(frame):
        t = threading.Thread(target=OCR.detectCharacters(frame), daemon=True)
        t.start()


    def feature_matching(frame):
        t = threading.Thread(target=FeatureMatching.runMatch(frame), daemon=True)
        t.start()


    def sift_detector(frame):
        t = threading.Thread(target=Sift_detector.run(frame), daemon=True)
        t.start()


    def readFromFilesystemStrategy():
        t = threading.Thread(target=Initiator.file_listener(), daemon=True)
        t.start()










