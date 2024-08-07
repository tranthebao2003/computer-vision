import numpy as np
from PIL import Image

path = 'D:/khac/nam_3/computer vision/img/1.jpg'
img = Image.open(path)

#chuyển hình về array
imgToArray = np.array((img))

#kiểm tra kích thước của array có màu là mảng 3 chiều
print("Kích thước mảng màu")
print(imgToArray.shape)

#chuyển đổi sang ảnh xám
# 'f': để chuyển sang kiểu float
imgToArray2 = np.array(img.convert('L'), 'f')
print("Kích thước mảng xám")
print(imgToArray2.shape)
print(imgToArray2.dtype)
