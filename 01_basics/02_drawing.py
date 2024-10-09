import cv2
import numpy as np

original_img = cv2.imread(filename=r'assets\python.png')
img = original_img.copy()

# cv2.imshow(winname='logo', mat=img)
# cv2.waitKey(0)

height, width = img.shape[:2]
print(f'Wysokosc: {height}')
print(f'Szerokosc: {width}')

# cv2.line(img=img, pt1=(0,0), pt2=(width, height), color=(0,255,0), thickness=5)

# cv2.rectangle(img=img, pt1=(200, 50),pt2=(400, 230), color=(255,241,23),thickness=3)
# cv2.circle(img=img, center=(300,140), radius=90, color=(124, 70 ,255), thickness=4)
# pts = np.array([[300,180], [200,200], [200, 50], [300, 50], [230, 20]], dtype='int32').reshape((-1,1,2))
# cv2.polylines(img=img, pts=[pts], isClosed=True, color=(42, 245, 215), thickness=3)

cv2.putText(
    img=img,
    text='Elo elo',
    org=(20,40),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1.4,
    color=(241,21,4),
    thickness=3
)

cv2.imshow('logo', img)
cv2.waitKey(0)