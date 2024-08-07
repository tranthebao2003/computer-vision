"""
Tăng cường độ tương phản, bằng cách tái phân bổ giá trị pixel trên toàn bức ảnh.
Cân bằng lược đồ xám có thể làm cho các chi tiết trong hình ảnh dễ nhận biết hơn
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def histogamEqualization(image, nbrBins = 256):
    # Đảm bảo hình ảnh đầu vào là ảnh xám
    # image.mode : nếu là ảnh màu nó sẽ trả về RGB, nếu là ảnh xám thì nó trả vè L
    if (image.mode != 'L'):
        image = image.convert('L')

    #chuyển img thành array
    imageArray = np.array(image)

    # tính toán histogram của ảnh
    # np.histogram(arrat, numberStacksHistogram, rangeValue (trog TH này nó sẽ tính toán từ 0 đến 255),
    # return tuple (arrayHistogram, arrayBins)
    histogram, bins = np.histogram(imageArray, bins=nbrBins, range=(0, 256), density=True)

    # tính toán hàm phân phối tích lũy (CDF - cumulative distribution function)
    cdf = histogram.cumsum()
    cdf = 255 * cdf / cdf[-1]

    # lấy giá trị mới cho từng pixel dựa trên CDF
    imageEqualized = np.interp(imageArray, bins[:-1], cdf)

    # chuyển đồi mảng kết quả thành hình ảnh
    equalizedImage = Image.fromarray(imageEqualized.astype('uint8'))

    return equalizedImage

path = './img/1.jpg'
#img ban đầu
img = Image.open(path)

#img sau khi đã cân bằng histogram
equalizedImg = histogamEqualization(img)

fig, axs = plt.subplots(2, 2, figsize = (10, 10))

fig.subplots_adjust(wspace = 0.2, hspace = 0.2)

axs[0, 0].imshow(img.convert('L'), cmap='gray')
axs[0, 0].set_title('Hình ảnh gốc')

axs[0, 1].hist(np.array(img.convert('L')).flatten(), bins = 128)
axs[0, 1].set_title('Biểu đồ histogram - hình ảnh gốc')

axs[1, 0].imshow(equalizedImg, cmap='gray')
axs[1, 0].set_title('Hình ảnh đã cân bằng')

axs[1, 1].hist(np.array(equalizedImg).flatten(), bins = 128)
axs[1, 1].set_title('Biểu đồ histogram - hình ảnh đã cân bằng')

plt.show()