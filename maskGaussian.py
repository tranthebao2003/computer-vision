"""
- Mặt nạ Gaussian, là 1 loại mặt nạ đc sử dụng trong xử lí ảnh
để lm mờ hoặc làm trơn ảnh
- Nó dựa trên phân phối gaussian (phân phối chuẩn) đc sử dụng để
tạo  hiệu ứng lm mờ trên ảnh = cách giảm độ biến đổi màu sắc
giữa các điểm ảnh gần nhau
- Mặt nạ Gaussian thường đc áp dụng để xử lí ảnh kĩ thuật số và chúng
thường đc sử dụng trong các ứng dụng như giảm nhiễu hoặc lm mịn ảnh
"""

from scipy import ndimage
from PIL import Image
import matplotlib.pyplot as plt
from convertImgtoArray import *

img = Image.open('./img/1.jpg')
grayImg = img.convert('L')
arrayImg = imgToArray2d('./img/1.jpg')

# làm mờ ảnh xám với bộ lọc gaussian
# mode='constant': Là tham số xác định cách xử lý các điểm ảnh ở biên
# khi áp dụng bộ lọc.Trong trường hợp này, mode được đặt là 'constant',
# nghĩa là giá trị các điểm ảnh nằm ngoài biên của hình ảnh sẽ được giữ nguyên.
# giá trị của sigma càng lớn thì bộ lọc sẽ lm mờ ảnh càng mạnh
blurImg1 = ndimage.gaussian_filter(arrayImg, sigma = 1, mode='constant')
blurImg2 = ndimage.gaussian_filter(arrayImg, sigma = 3, mode='constant')
blurImg3 = ndimage.gaussian_filter(arrayImg, sigma = 5, mode='constant')

# hiển thị ảnh
fig, axs = plt.subplots(2,2, figsize = (10, 10))

# imshow nó tự động chuyển từ array sang ảnh lun
plt.subplot(2, 2, 1)
plt.imshow(grayImg, cmap = 'gray')
plt.title('Ảnh xám gốc')

plt.subplot(2, 2, 2)
plt.imshow(blurImg1, cmap = 'gray')
plt.title('Sigma = 0.5')

plt.subplot(2, 2, 3)
plt.imshow(blurImg2, cmap = 'gray')
plt.title('Sigma = 1')

plt.subplot(2, 2, 4)
plt.imshow(blurImg3, cmap = 'gray')
plt.title('Sigma = 3')

plt.show()

