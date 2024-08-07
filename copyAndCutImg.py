from PIL import Image
from imgTool import *
from IPython.display import display

path = 'D:/khac/nam_3/computer vision/img/1.jpg'
img = loadImage(path)
img.show()

# định vị khu vực cắt
region = (0, 0, 350, 250)
#cắt vùng ảnh
#crop: return regtangular from this img, the box size tupble (left(x), upper(y), right(x), lower(y))
# crop này nó trả về hình chữ nhật hoặc hình vuông (ảnh 2d) thì sẽ luôn có 2 cặp cạnh bằng nhau
# chính vì thế nó chỉ cần chuyền vào 2 cặp số start: (x,y), end: (x1,y1) là có thể cắt đc.
# gốc tọa độ của hình là left upper
croppedImg = img.crop(region)
print(croppedImg.size)
croppedImg.show()

#copy paste
pastePosition = (250, 250)
# paste(ảnh cần paste, vị trí paste)
img.paste(croppedImg, pastePosition)
img.show()