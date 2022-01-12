import os

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/home/linuxbrew/.linuxbrew/bin/tesseract'

class OCR:
    def detectCharacters(img):
        try:
                #path = r'data/' + image;
                #print("imagepath " + path)
                #img = cv2.imread(image,0)

                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                global hImg, wImg, _, boxes, b, x, y, w, h
                config = r'--oem 3 --psm 6 '
                hImg, wImg = img.shape
                text = pytesseract.image_to_string(img)
                print(text)

                boxes = pytesseract.image_to_boxes(img, lang='eng', config=config)
                for b in boxes.splitlines():
                    b = b.split(' ')
                    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
                    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (255, 0, 0), 2)
                    cv2.putText(img, b[0], (x, hImg - y + 25), cv2.QT_FONT_NORMAL, 1, (255, 50, 50), 1)

                cv2.namedWindow("Main")
                cv2.imshow("Main",img)
                cv2.waitKey(0)

        except Exception as e:
                print("Feil har skjedd: " + str(e))
