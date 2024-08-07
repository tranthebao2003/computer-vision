# bài 3
from PIL import Image
# nó sẽ im port all dữ liệu từ file imgTool

from imgTool import *
from IPython.display import display


"""Bài 1 độc lập"""
# thư mục chứa hình ảnh
# bình thường path là dấu \ này nhưng có thể đổi thành / để tránh bị trùng những kí tự \n, \d ...
dir = 'D:/khac/nam_3/computer vision/img'

# đường dẫn đến hình ảnh
image_path = dir +'/1.JPG'

# sử dụng Image.open() đọc ảnh
img01 = Image.open(image_path)

# hiển thị hình ảnh
img01.show()

# show informations of image
print('Định dạng của ảnh: ', img01.format)
print('Kích thước của ảnh: ', img01.size)
#
# # lưu ảnh
# # ta có thể lưu ảnh vs 1 định dạng khác và nó sẽ biến đổi tính chất của ảnh
# # chứ ko chỉ đơn thuần là đổi đuôi file
# newPath = dir + '/new_01.JPG'
# newPath2 = dir + '/new_01.PNG'
# save(2 phần đường dẫn cần lưu và tên có phần mở rộng
# img01.save(newPath)
# img01.save(newPath2)
#
# #Đóng tập tin (quan trọng)
# img01.close()

"""bài 1 có kết hợp vs bài 2"""
#đọc ảnh từ function từ file khác
# dir2 = 'D:/khac/nam_3/computer vision/img'
# image_path2 = dir2 +'/1.JPG'
# img02 = loadImage(image_path2)
# img02.show()

"""bài 1 có kết hợp vs bài 2 phần 2"""
#đọc folder từ function từ file khác
dir3 = 'D:/khac/nam_3/computer vision/img'
imgs = getImgList(dir3)

#hiển thị toàn bộ ảnh bằng hàm display
for img in imgs:
    img.show()