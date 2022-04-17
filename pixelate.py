import cv2

def pixel(x1,y1,x2,y2,image):
    start = [x1,y1] #upper left bound
    end = [x2,y2] #lower right bound
    size = 15 #pixel sized
    end[0] = end[0]-((end[0]-start[0]) % size)#adjusting so that pixel is in the image.
    end[1] = end[1]-((end[1]-start[1]) % size)
    for i in range (start[0],end[0],size):
        for j in range (start[1],end[1],size):
            for k in range(size):
                for l in range(size):
                    image[i+k][j+l] = image[i+size//2][j+size//2]
    return image

'''
image = cv2.imread('download.jpg')
x1 = 0
y1 = 0
x2 = image.shape[0]
y2 = image.shape[1]
image = pixel(x1,y1,x2,y2,image)
cv2.imshow('Image', image)
'''
