"""
Hình thái học (morphology)
Là 1 phần quan trọng của xử lí ảnh, tập trung vào vc xử lí hình dạng và cấu túc của
đối tượng ảnh
Trong hình thái học chúng ta thường làm việc với ảnh nhị phân, trong đó các điểm ảnh
có giá trị 0 (đen) hoắc 1 (trắng)

# Các phép toán hình thái học cơ bản
Erosion (co thắt): Thu nhỏ kích thước của đối tượng trong ảnh
Dilation (co giãn): Mở rộng kích thước của đối tượng trong ảnh
Opening (mở): Thực hiện erosion sau đó dilation, giúp loại bỏ nhiễu và nối các đối tượng
Closing (đóng): Thực hiện dilation sau đó erosion, giúp lấp đầy lỗ và loại bỏ nhiễu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

#Đọc ảnh
image = Image.open('./img/animal.jpg')


#ảnh xám
grayImg = image.convert('L')

imgArray = np.array(grayImg)

#chuyển sang ảnh nhị phân
# Bước này chuyển đổi ảnh xám thành ảnh nhị phân
# dựa trên một ngưỡng (threshold). Trong trường hợp này, nếu giá
# trị pixel nhỏ hơn 200, nó sẽ được coi là màu trắng (1), ngược lại
# là màu đen (0).Điều này tạo ra một ảnh nhị phân với các đối tượng trắng và nền đen
binaryImage = 1 * (imgArray < 225)

#opening để loại bỏ nhiễu và nối các đối tượng với nhau
#structure=np.ones((9,5)): 1 cái mảng 9,5 để chạy
openImg = ndimage.binary_opening(binaryImage, structure=np.ones((9,5)))

# đánh nhãn
# trả về 1 ma trận ảnh đã gán nhãn và số đối tượng đc gán nhãn
labelImg, number = ndimage.label(openImg)

fig, axs = plt.subplots(2, 2, figsize = (10,10))
plt.subplot(2,2,1)
plt.imshow(grayImg, cmap = 'gray')
plt.title('Ảnh xám')

plt.subplot(2,2,2)
plt.imshow(binaryImage, cmap = 'gray')
plt.title('Ảnh nhị phân')

plt.subplot(2,2,4)
plt.imshow(openImg, cmap = 'nipy_spectral')
# để chữ f ở trước nó sẽ hiểu là format để nó biết number là biến và gán giá trị vào đó
plt.title(f'Ảnh chưa gán nhãn sử dụng opening ({number} đối tượng)')

plt.subplot(2,2,3)
plt.imshow(labelImg, cmap = 'nipy_spectral')
# để chữ f ở trước nó sẽ hiểu là format để nó biết number là biến và gán giá trị vào đó
plt.title(f'Ảnh đã gán nhãn sử dụng ({number} đối tượng)')

plt.show()