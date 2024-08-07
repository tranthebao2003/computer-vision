import matplotlib_inline
from PIL import Image
from imgTool import *
from IPython.display import display

path = 'D:/khac/nam_3/computer vision/img/1.jpg'
img = loadImage(path)
# img.show()

# chuyển từ ảnh màu sang ảnh xám
# dùng hàm convert và chuyển sang xám là chữ L
grayImg = img.convert('L')
# grayImg.show()

# phần rgb thành 3 tầng màu khác nhau
# nó trả về 3 ảnh vs 3 tầng màu thì mik cần 3 biến để lưu
red, green, blue = img.split()
# red.show()
# green.show()
# blue.show()

# trộn 3 tấm ảnh lại
# merged rgb thì phải có đủ 3 tấm, ở đây mik merged 2 tấm only green và 1 only red
mergedImg = Image.merge('RGB', (red,green,green))
mergedImg.show()