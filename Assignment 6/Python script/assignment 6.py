import cv2
print('IOT IBM ASSIGNMENT 6')
print('By Aditya Jaganath - 18BLC1057')

src1 = 'cars.xml'
src2 = 'Bus_front.xml'

video1 = 'cars 1.mp4'
video2 = 'busss.mp4'
cap1 = cv2.VideoCapture(video1)
cap2 = cv2.VideoCapture(video2)

car_cascade = cv2.CascadeClassifier(src1)
bus_cascade = cv2.CascadeClassifier(src2)


while True:
    ret1, img1 = cap1.read()
    ret2, img2 = cap2.read()
   
    if (type(img1) == type(None) and type(img2) == type(None)):
        break
    
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray1, 1.16, 1)
    bus = bus_cascade.detectMultiScale(gray2, 1.16, 1)
    
    
    for (x,y,w,h) in cars:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('video1', img1)
        
    for (x,y,w,h) in bus:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(-25,0,255),2)
        cv2.imshow('video2', img2)
    
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
