import cv2

def pixel(x1,y1,x2,y2,image):
    start = [x1,y1] #upper left bound
    end = [x2,y2] #lower right bound
    size = 20 #pixel sized
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


image = cv2.imread('download.jpg')
x1 = 50
y1 = 130
x2 = image.shape[1]
y2 = image.shape[0]
image = pixel(x1,y1,x2,y2,image)
cv2.imshow('Image', image)

