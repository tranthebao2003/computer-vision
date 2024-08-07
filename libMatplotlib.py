import matplotlib.pyplot as plt
from PIL import Image

path = 'D:/khac/nam_3/computer vision/img/1.jpg'
img = Image.open(path)
# # hai hàm này phải đi kèm với nhau để hiển thị 1 tấm ảnh có trục oxy
# plt.imshow(img)
# plt.show() #show ảnh

# # vẽ đồ thị cơ bản
# x = [1, 2, 3, 4, 5]
# y = [10, 16, 20, 30, 25]
# plt.plot(x, y, color = "red")
# plt.title("ví dụ về biểu đồ")
# plt.axis("off") # tắt hệ trục tọa đồ
# plt.show()

img2 = Image.open(path)
x = [100, 100, 400, 400]
y = [200, 300, 200, 300]
plt.imshow(img2)
plt.plot(x,y, 'b*:') #'r*': đánh dấu các điểm
plt.show()
