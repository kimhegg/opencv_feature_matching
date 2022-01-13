import sys
import threading
import cv2
import time
from initiator import Initiator
from tesseract.ocr import OCR
from opencv.orb_feature_matching import ORB_featureMatching
from opencv.sift_feature_matching import Sift_detector


def sift_detector(display_camera,frame):
    Sift_detector.run(display_camera,frame)


def saveFile(frame):
    now = int(time.time())
    img_name = "data/opencv_frame_{}.png".format(now)
    cv2.imwrite(img_name, frame)


def ocr_analyze(frame):
    OCR.detectCharacters(frame)


def feature_matching(frame):
    ORB_featureMatching.runMatch(frame)


def readFromFilesystemStrategy():
    ## Initiates OCR on saved images
    t = threading.Thread(target=Initiator.file_listener(), daemon=True)
    t.start()

if __name__ == '__main__':
    open_camera = False
    if sys.argv and sys.argv[0] == 1:
        open_camera = True
    else:
        print("Running no_display_output_mode")
        print("Output will be displayed in console.")
        open_camera = False

    def videoCapture(display_camera=open_camera,saveFrames=False, interval_seconds=0.01):
        capture = cv2.VideoCapture(0)
        capture.set(3, 640)
        capture.set(4, 480)
        interval_sec = interval_seconds
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

                sift_detector(display_camera,frame)
                start_time = time.time()


    videoCapture()














