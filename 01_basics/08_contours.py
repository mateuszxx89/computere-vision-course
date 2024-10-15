import cv2
from matplotlib.pyplot import thetagrids

original_img = cv2.imread(r'assets\python.png')
img = original_img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
#
thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow('theresh', thresh)


contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
# print(f'[INFO] Liczba konturów: ' , len(contours))

img_cnt = cv2.drawContours(img.copy(), [contours[1]], -1, (24,255,142), 2)
# cv2.imshow('img_cnt', img_cnt)



# area = cv2.contourArea(contours[4], True)
# print(area)

max_area = 0
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour, True)
    if area > max_area:
        max_area = area
        idx_flag_area = idx

print(f'[INFO] Indeks konturu o najwiekszym polu: {idx_flag_area}\nPole: {max_area}')

img_cnt_max_area = cv2.drawContours(img.copy(), [contours[idx_flag_area]],
                                    -1,(30, 255, 20), 2)

cv2.imshow('img_cnt_max_area', img_cnt_max_area)
cv2.waitKey(0)

perimiter = cv2.arcLength(contours[idx_flag_area], True)
print(perimiter)