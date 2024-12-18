import cv2
import imutils

img = cv2.imread(r'assets\guido.jpg')
img = imutils.resize(img, 500)
cv2.imshow('img',img)

# canny = cv2.Canny(img, 250, 250)
# cv2.imshow('canny', canny)

for thresh in [0, 25, 50, 75, 100 ,125, 150, 175, 200, 225, 250]:
    canny = cv2.Canny(img, thresh, thresh)
    cv2.imshow(f'canny: {thresh}', canny)
    cv2.waitKey(2000)
    cv2.destroyWindow(f'canny: {thresh}')

cv2.waitKey(0)