import cv2

array = cv2.imread("image.png")

print(array.shape) 
#it uses bgr and output will be like (3,4,3) first 3 indicates row then 4 indicates column and last 3 indicates 3 color(bgr)

print(array)