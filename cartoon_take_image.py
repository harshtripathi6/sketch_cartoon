# importing libraries
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# reading image
while cap.isOpened():
    ret, back = cap.read()                      #this is what the webcam is reading. ret is basically a bool variable used for testing truth

    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5) == ord('q'):

            cv2.imwrite('image.jpg',back)
            img = cv2.imread("C:\\Users\\hrtripathi\\PycharmProjects\\rubixcube\\image.jpg")
            break

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 1)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)



cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()