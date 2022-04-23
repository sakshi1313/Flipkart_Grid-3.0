import cv2
import numpy as np
import requests

urlarray = [['192.168.0.106'],['192.168.0.9'],['192.168.0.8'],['192.168.0.10']]

# img1 = cv2.VideoCapture(1)
# def countour_count():
#   ret, frame = img1.read()
#   img0 = frame[-300:0,:]


p1 = []  # the list which stores the clicked points
p2 = []
p3 = []
p4 = []
i = 0
for i in range(4):

    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, (x, y), 10, (0, 0, 0), -1)
            cv2.circle(img, (x, y), 5, (255, 255, 255), -1)
            if (i == 0):
                p1.append([x, y])
                arr = np.array(p1)
                # print(p1)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)
            elif (i == 1):
                p2.append([x, y])
                arr = np.array(p2)
                # print(p2)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)

            elif (i == 2):
                p3.append([x, y])
                arr = np.array(p3)
                # print(p3)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)
            elif (i == 3):
                p4.append([x, y])
                arr = np.array(p4)
                # print(p4)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)


    if __name__ == "__main__":
        img = cv2.imread("path.png")
        img = img[0:(int(img.shape[0])-300),0:int(img.shape[1])]
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image", img)
        cv2.setMouseCallback('image', click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

print(p1)
print(p2)
print(p3)
print(p4)


origin1=[]
origin2=[]
origin3=[]
origin4=[]

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
capture = cv.VideoCapture(0)
URL = "http://192.168.0.106/Flip"

while True:
     
    
    istrue, frame = capture.read()

    hsv_frame = cv.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_green=np.array([25,52,72])
    high_green=np.array([102,255,255])
    green_mask=cv.inRange(hsv_frame,low_green,high_green)
    green=cv.bitwise_and(frame,frame,mask=green_mask)

    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv2.erode(green_mask, kernel, iterations=2)

    contours, hierarchy = cv2.findContours(img_erosion,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 200):
            approx = cv2.approxPolyDP(contour, 0.009 * cv2.arcLength(contour, True), True)
            cv2.drawContours(new_img, [approx], 0, (0, 0, 255), 5)
            n = approx.ravel()
            x_cor,y_cor=cordinate(n)
            print(x_cor,y_cor)
            cv2.circle(new_img, (int(x_cor), int(y_cor)), 3, (0, 0, 255), 3, cv2.FILLED)
            arr.append([int(x_cor), int(y_cor)])

    value = sorted(arr, key=lambda k: k[0])
    #print(values)
    bot4=value[0] 
    bot3=value[1]
    bot2=value[2]
    bot1=value[3]

    i=0
    for i in range(4):
#  ************************************************************************************************************************************************
# X-Coor
        while (p1[0][1]-bot1[1]>200):
            diff=p1[0][0]-bot1[0]
            if (diff>0):
                if (diff>200):
                    r = requests.get(url = "http://" + urlarray[z]+"/sleft")
            elif (diff<0):
                if (abs(diff)>200):
                    r = requests.get(url = "http://" + urlarray[z]+"/sright")
# TRUN
    turn()
    while (p1[1][0]-bot1[0]>10):
        diff=p1[0][1]-bot1[1]
        if (diff>0):
            if (diff>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
            elif (diff<0):
                if (abs(diff)>200):
                    r = requests.get(url = "http://" + urlarray[z]+"/sleft")
    r = requests.get(url = "http://"+urlarray[z]+"/Flip")
# Y-Coor   
    while (p1[0][0]-bot1[0]>10):
        diff=p1[0][1]-bot1[1]
        if (diff>0):
            if (diff>200):
              #anti
              r = requests.get(url = "http://" + urlarray[z]+"/sright")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
              r = requests.get(url = "http://" + urlarray[z]+"/sleft")

    turn()
    while (origin1[1]-bot1[1]>200):
        diff=origin1[0]-bot1[0]
        if (diff>0):
            if (diff>200):
              #anti
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
                r = requests.get(url = "http://" + urlarray[z]+"/sright")


#    *****************************************************************************************************************************************************************************


    i=i+1

    while (p2[0][1]-bot2[1]>200):

        diff=p2[0][0]-bot2[0]
        if (diff>0):
            if (diff>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")
        elif (diff<0):
            if (abs(diff)>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sright")  
    turn()
    while (p2[1][0]-bot2[0]>10):
        diff=p2[0][1]-bot2[1]
        if (diff>0):
            if (diff>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
        elif (diff<0):
            if (abs(diff)>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")

    # - - ERROR CHECK - -
    r = requests.get(url = "http://"+urlarray[z]+"/Flip")  

    while (p2[0][0]-bot2[0]>10):
        diff=p2[0][1]-bot2[1]
        if (diff>0):
            if (diff>200):
              #anti
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")

    turn()
    while (origin2[1]-bot2[1]>200):
        diff=origin2[0]-bot2[0]
        if (diff>0):
            if (diff>200):
              #anti
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
    
#  **********************************************************************************************************************************************************************************

    i=i+1

    while (p3[0][1]-bot3[1]>200):

        diff=p3[0][0]-bot3[0]
        if (diff>0):
            if (diff>200):
              r = requests.get(url = "http://" + urlarray[z]+"/sleft")
        elif (diff<0):
            if (abs(diff)>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
    turn()
    while (p3[1][0]-bot3[0]>10):
        diff=p3[0][1]-bot3[1]
        if (diff>0):
            if (diff>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
        elif (diff<0):
            if (abs(diff)>200):
              r = requests.get(url = "http://" + urlarray[z]+"/sleft")
    r = requests.get(url = "http://"+urlarray[z]+"/Flip")     


    while (p3[0][0]-bot3[0]>10):
        diff=p3[0][1]-bot3[1]
        if (diff>0):
            if (diff>200):
              #anti
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")

    turn()
    while (origin3[1]-bot3[1]>200):

        diff=origin3[0]-bot3[0]
        if (diff>0):
            if (diff>200):
              #anti
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
                r = requests.get(url = "http://" + urlarray[z]+"/sright")

#    ******************************************************************************************************************************************************************************

    i=i+1

    while (p4[0][1]-bot4[1]>200):

        diff=p4[0][0]-bot4[0]
        if (diff>0):
            if (diff>200):
              r = requests.get(url = "http://" + urlarray[z]+"/sleft")
        elif (diff<0):
            if (abs(diff)>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sright") 
    turn()
    while (p4[1][0]-bot4[0]>10):
        diff=p4[0][1]-bot4[1]
        if (diff>0):
            if (diff>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
        elif (diff<0):
            if (abs(diff)>200):
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")
    r = requests.get(url = "http://"+urlarray[z]+"/Flip") 

    while (p4[0][0]-bot4[0]>10):
        diff=p4[0][1]-bot4[1]
        if (diff>0):
            if (diff>200):
              #anti
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")

    turn()
    while (origin4[1]-bot4[1]>200):

        diff=origin4[0]-bot4[0]
        if (diff>0):
            if (diff>200):
              #anti
                r = requests.get(url = "http://" + urlarray[z]+"/sleft")
        elif (diff<0):
            if (abs(diff)>200):
              #clock
                r = requests.get(url = "http://" + urlarray[z]+"/sright")
                 
# ***********************************************************************************************************************************************************************************
            

    cv2.imshow("Video", frame)
    cv2.imshow("Bots", red)
    r = requests.get(url=URL)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()