"""
- Đường biên của 1 ảnh (được hiểu là 1 ma trận hoặc 1 mảng số
) là 1 tập hợp các điểm biên giới của các đối tượng hoặc
các khu vực trong ảnh
- Đường biên xác định ranh giới giữa các đối tượng và nền trong ảnh
- Điều này thường là quan trọng trong xử lí ảnh và phân đoạn
hình ảnh, khi bạn muốn tách các đối tượng trong ảnh or phát hiện
biên của chúng
"""
import matplotlib.pyplot as plt
from PIL import Image


path = 'D:/khac/nam_3/computer vision/img/anhNguoi.jpg'
img = Image.open(path)
imgGray = img.convert('L')
# tạo 1 hình vẽ mới
plt.figure()
# đặt ảnh thành màu xám
plt.gray()
# vẽ biểu đồ đường biên (contour) của ảnh
plt.contour(imgGray, origin = 'image')
plt.axis('equal') # tỉ lệ trục x và y ngang nhau
plt.show()
