import cv2 as cv
import numpy as np 
import requests

def cordinate(n):
    x_arr = n[::2]
    x= sum(x_arr)
    x = x / len(x_arr)

    y_arr = n[1::2]
    y = sum(y_arr)
    y = y / len(y_arr)

    return x,y

# url="http://192.168.0.3:8080/video"
# Put 0 for webcam and link for IP webcam or enter 1 if using Droidcam via USB
capture=cv.VideoCapture(1)
#URL="http://192.168.0.106/Flip"
while True:
    istrue,frame=capture.read()

    arr=[]
    hsv_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    low_green=np.array([60,30,20])
    # low_green=np.array([102,255,51])
    high_green=np.array([95,255,255])
    green_mask=cv.inRange(hsv_frame,low_green,high_green)
    green=cv.bitwise_and(frame,frame,mask=green_mask)
    
    # low_red=np.array([161,155,84])
    # high_red=np.array([179,255,255])
    # red_mask=cv.inRange(hsv_frame,low_red,high_red)
    # red=cv.bitwise_and(frame,frame,mask=red_mask)
    
    # low_blue=np.array([94,80,2])
    # high_blue=np.array([126,255,255])
    # blue_mask=cv.inRange(hsv_frame,low_blue,high_blue)
    # blue=cv.bitwise_and(frame,frame,mask=blue_mask)
    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv.erode(green_mask, kernel, iterations=2)
    img_dilation=cv.dilate(img_erosion,kernel,iterations=1)
    contours, hierarchy = cv.findContours(img_dilation,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if (area<5000):
            approx = cv.approxPolyDP(contour, 0.04 * cv.arcLength(contour, True), True)
            cv.drawContours(frame, [approx], 0, (0, 0, 255), 2)
            # aman=cv.boundingRect(approx)
            # cv.rectangle(frame,(aman[0],aman[1]),(aman[0]+aman[2],aman[1]+aman[3]),(0,255,0),2)
            n = approx.ravel()
            x_cor,y_cor=cordinate(n)
            print(x_cor,y_cor)
            cv.circle(frame, (int(x_cor), int(y_cor)), 1, (0, 0, 255), 3, cv.FILLED)
            arr.append([int(x_cor), int(y_cor)])
    cv.imshow("Video",frame)
    cv.imshow("Bots",green)
    # r=requests.get(url=URL)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()    
