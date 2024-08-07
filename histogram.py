import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
"""
- Lược đồ histogram là 1 biểu đồ thống kê mô tả tần suất xuất
hiện của mỗi mức xám trong hình ảnh
- Hình ảnh xám là hình ảnh ko có màu sắc, chỉ có mức độ
sáng tương ứng với mỗi độ sáng tối của mỗi pixel
- Lược đồ histogram cho phép chúng ta xem xét phân bố pixel
để hiểu rõ cường độ ánh sáng trong hình ảnh
"""
path = 'D:/khac/nam_3/computer vision/img/1.jpg'
img = Image.open(path)
# plt.imshow(img)
# plt.show()

# biến ảnh màu thành trắng đen
imgGray = img.convert('L')
plt.imshow(imgGray, cmap = 'gray')
plt.show()

#biến ảnh trắng đen thành mảng
imgArray = np.array(imgGray)

#tạo 1 hình vẽ mới
# plt.figure(): Tạo một hình (figure) mới. Một hình là nơi chứa tất cả các đối
# tượng đồ thị như đồ thị, biểu đồ, hình ảnh,
plt.figure()
# imgArray.flatten(): biến mảng 2 chiều thành 1 chiều
plt.hist(imgArray.flatten(), bins = 128)
plt.title('Biểu đồ Histogram của ảnh')
plt.xlabel('Giá trị của pixel')
plt.ylabel('Số lượng')
plt.show()