import os
import numpy as np
import cv2
import glob

cap = cv2.VideoCapture('2022-06-13_01-11-36.mkv')

img1 = cap.read()[1]
img_height, img_width, _ = img1.shape 
a = 0
print(img_width, img_height)

backboards = []
for filename in os.listdir("./result"):
    frame = int(filename[20:-4])
    #print(filename)
    #print(frame-1)
    f = open("./result/" + filename)
        
    for line in f:
        temp = [float(x) for x in line.split()]
        _, x, y, w, h = temp
        xmin = (int((x - 1/2 * w) * img_width))
        xmax = (int((x + 1/2 * w) * img_width))
        ymin = (int((y - 1/2 * h) * img_height))
        ymax = (int((y + 1/2 * h) * img_height))
        temp = (frame, xmin, ymin, xmax, ymax)
            
            
        backboards.append(temp)
    
a = (100, 3)
b = (99, 2)
aa = [a, b]
backboards.sort( key = lambda x: int(x[0]))

def pixel(x1,y1,x2,y2,image):
    start = [x1,y1] #upper left bound
    end = [x2,y2] #lower right bound
    size = 50 #pixel sized
    for i in range (start[0],end[0],size):
        for j in range (start[1],end[1],size):
            for k in range(size):
                for l in range(size):
                    if j+l+1 < image.shape[0] and i+k+1 < image.shape[1]:
                        if j+size//2+1 < image.shape[0] and i+size//2+1 < image.shape[1]:
                            x = j+size//2
                            y = i+size//2
                        else:
                            x = j
                            y = i
                        image[j+l][i+k] = image[x][y]
    return image

ii = 1
jj = 0
framelist = []
ret, frame = cap.read()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
videowrite = cv2.VideoWriter(r'D:/test.mp4', fourcc , 30.0, (1920, 1080))

while(ret == True):
  
    ii += 1
    while(backboards[jj][0] == ii):
        frame = pixel(backboards[jj][1], backboards[jj][2], backboards[jj][3], backboards[jj][4], frame)
        jj += 1
        
    videowrite.write(frame)
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    ret, frame = cap.read()
    print(ii)
    
videowrite.release()

