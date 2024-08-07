import matplotlib.pyplot as plt
from PIL import Image

path = 'D:/khac/nam_3/computer vision/img/1.jpg'

img = Image.open(path)
plt.imshow(img)

# sử dụng hàm ginput để chọn điểm trên ảnh và nó sẽ trả về 1 list
# mà giá trị của 1 list sẽ là 1 cặp tuple. ginput(5) là số điểm tối đa có thể chấm
points = plt.ginput(5)
print(points)
plt.show()
plt.close()

#vẽ lại các điểm đã chọn bằng dấu * màu đỏ
a = []
b = []
# phải hiện thị ảnh trước sau mới vẻ
plt.imshow(img)
for point in points:
    # gán giá trị tuple cho x, y
    x, y = point
    a.append(x)
    b.append(y)

plt.plot(a, b, 'r*-')
plt.show()
