"""
cv2.line(): vẽ đường thẳng trên hình ảnh
cv2.line(image, startPoint, endPoint, color, thickness)

cv2.rectangle(): vẽ hình chữ nhật trên hình ảnh
cv2.rectangle(image, TopLeftPoint, bottomRightPoint, color, thickness)

cv2.circle(): vẽ hình tròn trên hình ảnh
cv2.circle(image, center, radius, color, thickness)

cv2.ellipse(): vẽ hình elip trên hình ảnh
cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)

cv2.polylines(): vẽ đa giác trên hình ảnh
cv2.polylines(image,[arrayOfPoints], isclosed, color, thickness)
"""

import cv2
import numpy as np

def display(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyWindow(title)

#Tạo 1 ảnh
img = np.zeros((400, 400, 3), dtype=np.uint8)
# display('Image', img)

# # vẽ đường thẳng
# line = cv2.line(img, (50,50), (350, 350), (255, 255, 255), 5)
# display('Image', line)

# # vẽ hình tròn
# # nếu ta để thickness = -1 thì nó sẽ tô toàn bộ nội dung bên trong
# circle = cv2.circle(img, (100,100), 50, (255,255,255), -1)
# display('Image', circle)

# vẽ hình chữ nhật
rectangle = cv2.rectangle(img, (100, 100), (300, 300), (255,255,255), -1)
display('Image', rectangle)


# ghi text trên hình ảnh
content = 'Tran The Bao'
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, content, (10, 400), font, 1, (255,255,255), 2)
display('chữ', img)