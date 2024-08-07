# import thư viện openCv
import cv2

img = cv2.imread('./img/1.jpg')
# in thông tin ảnh
# print(img)

#lấy kích thước của ảnh: width, height, số chiều
# print(img.shape)

#hiển thị ảnh
# cv2.imshow('Image', img)
# # chờ 1 khoảng (ms) tg
# cv2.waitKey(2000)
# # đóng window
# cv2.destroyWindow('Image')

# tách và chuyển đổi hệ mau
# blue, green, red = cv2.split(img)
# cv2.imshow('Img original', img)
# cv2.imshow('Img only Blue', blue)
# cv2.imshow('Img only Green', green)
# cv2.imshow('Img only Red', red)
# # waitKey(0): nếu như vầy thì nó sẽ hiển thị cho đến khi mình ấn bất kì 1 phím nào đó
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# grayImg1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ImgChange = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('Img original', img)
# cv2.imshow('grayImg1', grayImg1)
# cv2.imshow('ImgChange', ImgChange)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# thay đổi thông sớ của điểm aảnh
height, width, z = img.shape
quaterH = height / 2
quaterW = width / 2

#green color
greenColor = (0, 255, 0)
img2 = img.copy()

#thay đổi màu của góc 1/4 bên trái trên: bản chất là thay đổi từng pixel dựa vào 2 vòng for
#duyệt từ trái sang phải từ trên xuống dưới
for y in range(int(quaterH)):
    for x in range(int(quaterW)):
        img2[y, x] = greenColor

cv2.imshow('Img original', img)
cv2.imshow('Img quater top left green', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()