from PIL import Image
from imgTool import *
from IPython.display import display

#đường dẫn
path = 'D:/khac/nam_3/computer vision/img/1.jpg'

#đọc ảnh
img = loadImage(path)
# print(img.size)
# img.show()

# thay đổi kích thước
newSize = (600,600)
print(type(newSize))
newImage = img.resize(newSize)
newImage.save('D:/khac/nam_3/computer vision/img/newImg3.jpg')
newImage.show()

# ngoài ra còn hàm img.thumbnail nó cũng nhận vào 1 tuple và làm thay đổi kích thước
# nhưng nó sẽ thay đổi kích thước ảnh gốc lun, còn resize thì nó sẽ cho ra tấm
# ảnh mới có kích thước thay đổi còn ảnh gốc vẫn giữ nguyên