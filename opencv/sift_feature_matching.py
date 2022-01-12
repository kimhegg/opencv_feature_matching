
import numpy as np
import cv2 as cv
import os


class Sift_detector:

    def findID(img, desList):
        MIN_MATCH_COUNT = 5
        matchList=[]
        finalVal = -1
        sift = cv.SIFT_create()
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv.FlannBasedMatcher(index_params, search_params)
        kp2, des2 = sift.detectAndCompute(img, None)
        try:
            for des in desList:
                matches = flann.knnMatch(des, des2, k=2)
                # Lowe's ratio test.
                good = []
                for m, n in matches:
                    if m.distance < 0.5 * n.distance:
                        good.append(m)
                matchList.append(len(good))
        except:
            pass

        if len(matchList) != 0:
            if max(matchList) >= MIN_MATCH_COUNT:
                finalVal = matchList.index(max(matchList))
        return finalVal



    def findDescriptor(images):
        sift = cv.SIFT_create()
        desList=[]
        for img in images:
            kp, des = sift.detectAndCompute(img, None)
            desList.append(des)
        return desList


    def run(img):
        path = 'imagesTrain'
        images = []
        classNames = []
        myList = os.listdir(path)
        print("Total classed detected", len(myList))

        for cl in myList:
            imgCur = cv.imread(f'{path}/{cl}', 0)
            images.append(imgCur)
            classNames.append(os.path.splitext(cl)[0])
        desList = Sift_detector.findDescriptor(images)
        id = Sift_detector.findID(img, desList)
        if id != -1:
            cv.putText(img,classNames[id],(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
        cv.imshow("sad", img)










    def alt_run(img):
        MIN_MATCH_COUNT = 10
        img1 = cv.imread('imagesTrain/vendanor.png',0)  # queryImage
        img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Initiate SIFT detector
        sift = cv.SIFT_create()
        # find the keypoints and descriptors with SIFT
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1, des2, k=2)

        #Lowe's ratio test.
        good = []
        for m, n in matches:
            if m.distance < 0.5 * n.distance:
                good.append(m)

        if len(good) > MIN_MATCH_COUNT:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()
            h, w = img1.shape
            pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
            dst = cv.perspectiveTransform(pts, M)
            img2 = cv.polylines(img2, [np.int32(dst)], True, 255, 3, cv.LINE_AA)
        else:
            print("Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
            matchesMask = None

        draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                           singlePointColor=None,
                           matchesMask=matchesMask,  # draw only inliers
                           flags=2)
        img3 = cv.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
        if len(good) >= MIN_MATCH_COUNT:
            cv.putText(img3, "Vendanor", (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        cv.imshow("sad",img3)