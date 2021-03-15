import cv2
import numpy as np

# reading image
img = cv2.imread("C:\\Users\\hrtripathi\\Desktop\\cycle.JPG")
img_half = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
# Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 1)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 11)
e_half = cv2.resize(edges, (0, 0), fx = 0.5, fy = 0.5)
# Cartoonization
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)
half = cv2.resize(cartoon, (0, 0), fx = 0.5, fy = 0.5)


cv2.imshow("Image", img_half)
cv2.imshow("edges", e_half)
cv2.imshow("Cartoon", half)
cv2.waitKey(0)
cv2.destroyAllWindows()