#file = open("G:\\4063.jpg","rb")
import cv2
img = cv2.imread('G:\\4063.jpg', flags=cv2.IMREAD_COLOR)
print(type(img))
print(img)
