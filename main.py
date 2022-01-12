import threading
import cv2
import time
from initiator import Initiator
from tesseract.ocr import OCR
from opencv.orb_feature_matching import ORB_featureMatching
from opencv.sift_feature_matching import Sift_detector


def sift_detector(frame):
    Sift_detector.run(frame)


def saveFile(frame):
    now = int(time.time())
    img_name = "data/opencv_frame_{}.png".format(now)
    cv2.imwrite(img_name, frame)


def ocr_analyze(frame):
    OCR.detectCharacters(frame)


def feature_matching(frame):
    ORB_featureMatching.runMatch(frame)


def readFromFilesystemStrategy():
    t = threading.Thread(target=Initiator.file_listener(), daemon=True)
    t.start()

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
            if time.time() - start_time >= interval_sec:  # trick to do operations at a certain interval
                if saveFrames:
                    saveFile(frame)
                    readFromFilesystemStrategy()

                sift_detector(frame)
                start_time = time.time()


    videoCapture()














