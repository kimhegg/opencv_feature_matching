import os
import time

from tesseract.ocr import OCR

class Initiator:


    def file_listener(self):
        path_to_watch = "/home/kim/PycharmProjects/realtime_ocr/data"
        print('Your folder path is"', path_to_watch, '"')

        old = os.listdir(path_to_watch)
        print(old)

        while True:
            new = os.listdir(path_to_watch)
            if len(new) > len(old):
                newfile = list(set(new) - set(old))
                print("Found new file: " + newfile[0])
                old = new
                extension = os.path.splitext(path_to_watch + "/" + newfile[0])[1]
                if extension == ".png" or extension == ".jpg":
                    print("Running detection on " + newfile[0])
                    time.sleep(2)
                    OCR.detectCharacters(newfile[0])
                else:
                    continue
            else:
                continue





