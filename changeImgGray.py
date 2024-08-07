import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

path = './img/1.jpg'
img = Image.open(path)

imgGray = img.convert('L')

imgArrayG = np.array(imgGray)

# biến đổi ảnh xám theo yêu cầu
reverseImg = 255 - imgArrayG # reverse ảnh bằng cách lấy giá trị 255 - giá trị pixel (sáng thành tối
# tối thành sáng)

# #img init
# plt.imshow(imgGray, cmap='gray')
# plt.show()
#
# #img reverse
# plt.imshow(reverseImg, cmap='gray')
# plt.show()

squareImg = imgArrayG ** 2  # bình phương giá trị pixel
clampImg = np.clip(imgArrayG, 100, 200) #giới hạn giá trị pixel trong khoảng 100 - 200
# nghĩa là nếu nó dưới min thì nó về min nó lớn hơn max thì nó thành max


# hiển thị hình ảnh gốc và hình ảnh đã biến đổi với khoảng trắng\

# tạo 1 khung ảnh 2 dòng, 2 cột kích thước 10, 10 (inch)
# Hàm này trả về một đối tượng Figure và một mảng các đối
# tượng Axes tương ứng với các ô trong bố cục. Sau đó gán đối tượng Figure vào biến fig
# và mảng các đối tượng Axes vào biến axs
fig, axs = plt.subplots(2, 2, figsize = (10, 10))

# Điều chỉnh khoảng cách giữa các ô trong hình. Trong trường hợp này, wspace=0.2 và hspace=0.2
# xác định khoảng cách theo chiều ngang và dọc giữa các ô, tương ứng là 0.2 inch
fig.subplots_adjust(wspace = 0.2, hspace = 0.2)


# Sau khi thực hiện các dòng mã trên, ta sẽ có một khung hình với lưới
# 2x2 các ô (tổng cộng 4 ô), mỗi ô có một đối tượng Axes tương ứng.
# Các ô này có thể được sử dụng để vẽ đồ thị
# hoặc biểu đồ khác nhau và có thể được quản lý và tùy chỉnh độc lập với nhau.
axs[0, 0].imshow(imgArrayG, cmap='gray')
axs[0, 0].set_title('Hình ảnh gốc')

axs[0, 1].imshow(reverseImg, cmap='gray')
axs[0, 1].set_title('Reverse image')

axs[1, 0].imshow(squareImg, cmap='gray')
axs[1, 0].set_title('Square image')

axs[1, 1].imshow(clampImg, cmap='gray')
axs[1, 1].set_title('Clapm imgae')

plt.show()