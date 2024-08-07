"""
- Derivatives Image: là phần q trọng của nhiều ứng dụng, bao gồm xác định biên, xác định cạnh,
và nhiềm nhiệm vụ khác
- Các bộ lọc đạo hàm (derivative filters) là các mặt nạ đc sử dụng trong xử lí aảnh. Chúng
thường được áp dụng để tìm sự biến đổi của cường độ màu sắc tại mỗi điểm ảnh

- Bộ lọc Sobel: sử dụng 2 mặt nạ (mặt nạ sobel x và mặt nạ sobel y) để tính đạo hàm riêng theo
hướng ngang và dọc. Chúng thường đc sử dụng để phát hiện ra cạnh của ảnh
- Bộ lọc Prewitt
"""

from convertImgtoArray import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
imgArray = imgToArray2d('./img/anhNguoi.jpg')


# bộ lọc sobel
# Tính gradient theo hướng x : axis=0
gradientX = ndimage.sobel(imgArray, axis=0, mode='constant')
# Tính gradient theo hướng y : axis=1
gradienty = ndimage.sobel(imgArray, axis=1, mode='constant')


# bộ lọc Prewitt
# Tính gradient theo hướng x
gradientXPre = ndimage.convolve(imgArray, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]), mode='reflect')
# Tính gradient theo hướng y
gradientYPre = ndimage.convolve(imgArray, np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]), mode='reflect')
# Tính biên độ gradient
gradientMagnitude = np.sqrt(gradientXPre**2 + gradientYPre**2)

fig, axs = plt.subplots(2, 2, figsize = (10, 10))
plt.subplot(2,2,1)
plt.imshow(imgArray, cmap='gray')
plt.title('Ảnh gốc')

plt.subplot(2,2,2)
plt.imshow(gradientX, cmap='gray')
plt.title('gradientX sobel')

plt.subplot(2,2,3)
plt.imshow(gradienty, cmap='gray')
plt.title('gradientY sobel')

plt.subplot(2,2,4)
plt.imshow(gradientMagnitude, cmap='gray')
plt.title('gradient Prewitt')

plt.show()