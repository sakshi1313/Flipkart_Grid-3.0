import cv2
import numpy as np
from pyzbar.pyzbar import decode
def bqcode_scan(img):
    code = decode(img)
    print(code)
    for bqcode in code:
        #print(bqcode.data)
        myData = bqcode.data.decode("utf-8")
        print(myData) # barcode data
        pts = np.array([bqcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 2)
        pts2 = bqcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
path='frobotians/hf.png'
cv2.namedWindow("barcode_scan",cv2.WINDOW_NORMAL)
img_B=cv2.imread(path)
bqcode_scan(img_B)
cv2.imshow("barcode_scan", img_B)
cv2.waitKey(0)