import cv2


img = cv2.imread(r'assets\poland.png')
img = cv2.copyMakeBorder(src=img, top=20, bottom=20, left=20, right=20, borderType=cv2.BORDER_CONSTANT, value=(255,255,255))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)[1]

conturs = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] Libacz wszystkich konturów: {len(conturs)}')

img = cv2.drawContours(image=img, contours=[conturs[0]], contourIdx=-1, color=(0,255,0), thickness=2)
# cv2.imshow('conturs', img)

contur = conturs[0]
leftmost = contur[contur[:, :, 0].argmin()][0]
rightmost = contur[contur[:, :, 0].argmax()][0]
topmost = contur[contur[:, :, 1].argmin()][0]
bottommost = contur[contur[:, :, 1].argmax()][0]


for point in [leftmost, rightmost, topmost, bottommost]:
    cv2.circle(img, center=tuple(point), radius=10, color=(0,0,255), thickness=-1)

cv2.imshow('extreme_Points', img)
cv2.waitKey(0)