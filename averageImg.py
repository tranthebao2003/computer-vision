# average image chỉ sử dụng đc cho những img có cùng size
# lí do: Tính trung bình từ rất nhìu hình ảnh có cùng kích thước để lm giảm nhiễu hình ảnh
# nâng cao chất lượng hình ảnh
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def averageImgs(imgList):
    # totalArray ban đầu nó là cái ảnh đầu tiên
    totalArray = np.array(Image.open(imgList[0]), 'f')
    count = 1

    # imgList[1:]: lấy từ phần tử thứ 2 trong mảng đến hết
    for imagePath in imgList[1:]:
        try:
            imgArray = np.array(Image.open(imagePath), 'f')
            totalArray += imgArray # cộng 2 ma trận thì size nó phải = nhau
            count += 1
        except:
            print("Skip", imagePath)

    # tính trung bình
    averageArray = totalArray / count

    # chuyển đổi kết quả trung bình thành hình ảnh
    # uint8: unsign int số nguyên ko dấu 2^8 = 256 tương ứng vs 0->255 trong ảnh histogram
    averageImg = Image.fromarray(averageArray.astype('uint8'))

    return averageImg

# sử dụng ví dụ:
path1 = './img/1.jpg'
path2 = './img/2.jpg'

image_list = [path1, path2]
resultImg = averageImgs(image_list)

img1 = np.array(Image.open('./img/1.jpg'), 'f')
img2 = np.array(Image.open('./img/2.jpg'), 'f')
resultImg2 = np.ar([3,2,3])
print(resultImg2)

fig, axs = plt.subplots(2, 2, figsize = (10, 10))

fig.subplots_adjust(wspace = 0.2, hspace = 0.2)

axs[0, 0].imshow(resultImg)
axs[0, 0].set_title('Trung bình hình ảnh tính tay')

# axs[0, 1].imshow(resultImg2)
# axs[0, 1].set_title('Trung bình hình ảnh tính bằng thư viện numpy')


plt.show()
