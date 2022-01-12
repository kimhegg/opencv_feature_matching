import time

import cv2

class ORB_featureMatching:

    def runMatch(img):
        img1 = cv2.imread()
        img2 = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)

        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        # imgKp1 = cv2.drawKeypoints(img1,kp1,None)
        # imgKp2 = cv2.drawKeypoints(img2,kp2,None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key = lambda x:x.distance)


        img3=cv2.drawMatches(img1, kp1, img2, kp2, matches[:5], None, flags=2)
        cv2.putText(img3, "Vender", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        cv2.imshow("live",img3)

       # time.sleep(0.5)




