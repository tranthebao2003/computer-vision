from PIL import Image
from imgTool import *
from IPython.display import display

path = 'D:/khac/nam_3/computer vision/img/1.jpg'
img = loadImage(path)

# xoay ảnh: nó vẫn giữa nguyên tỉ lệ ban đầu và chỉ xoay ảnh nên sẽ có những khoảng đen
# resize((a,b))
# img2 = img.resize((500,500))
rotatedImg = img.rotate(90)
rotatedImg.show()

#transpose (flip)(lật ảnh): thay đổi tỉ lệ ban đầu: vd: từ 16:9 sang 9;16
# chỉ có 3 giá trị lật Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270
transposeImg = img.transpose(Image.ROTATE_90)
transposeImg.show()