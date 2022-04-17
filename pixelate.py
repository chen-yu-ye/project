import cv2
import numpy as np
image = cv2.imread('download.jpg')
start = [0,0] #upper left bound
end = [image.shape[0],image.shape[1]] #lower right bound
size = 15 #pixel sized
end[0] = end[0]-((end[0]-start[0]) % size)#adjusting so that pixel is in the image.
end[1] = end[1]-((end[1]-start[1]) % size)
for i in range (start[0],end[0],size):
    for j in range (start[1],end[1],size):
        for k in range(size):
            for l in range(size):
                image[i+k][j+l] = image[i+size//2][j+size//2]
cv2.imshow('Image', image)

