"""
Haar Cascade Classfier

- Haar Cascade là 1 pp nhận dạng đặc trưng dựa trên máy học
(machine learning)
- Được phát triển bởi các nhà nghiên cứu Viola và Jones vào năm 2021
- Dựa trên việc sử dụng các "Haar-like features" (các đặc trưng giống như
Haar), là các kích thước và hình dạng khác nhau
- Haar-like features có thể được sử dụng để nhận dạng các đối tượng cụ thể
trong hình ảnh
"""


"""Nhận diện 1 tấm ảnh trước"""

import cv2
import time

def display(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyWindow(title)


def detect(img):
    # khởi tạo object Haar Cascade Classifier cho nhận diện khuôn mặt
    faceCascade = cv2.CascadeClassifier('./identifyFace/HaarCascades/haarcascade_frontalface_default.xml')
    # khởi tạo object Haar Cascade Classifier cho nhận diện mắt
    eyeCascade = cv2.CascadeClassifier('./identifyFace/HaarCascades/haarcascade_eye_tree_eyeglasses.xml')
    # chuyển sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # nhận diện
    """
    - scaleFactor: càng lớn thì tính tốc độ tính toán càng nhanh nhưng độ chính xác giảm
    Ngược lại thì độ chính xác sẽ cao nhưng tốc độ giảm. 1.1 là giá trị default
    - MinNeighbors: việc tăng giá trị của minNeighbors có thể làm giảm số 
    lượng phát hiện và tăng độ chính xác,nhưng cũng có thể làm mất mát một số đối tượng nhỏ
    - MinSize=(30,30): Đây là kích thước tối thiểu của một khuôn mặt. 
    Bất kỳ khuôn mặt nhỏ hơn kích thước này sẽ không được xem xét. 
    Điều này giúp loại bỏ các đối tượng nhỏ không phải là khuôn mặt
    
    Trả về (x,y, width, height) của 1 rectangle
    """
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 5, minSize=(30,30))
    eyes = eyeCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors= 1, minSize=(5,30))

    # vẽ hộp chứa khuôn mặt
    # Vòng lặp for (x, y, w, h) in faces:: Vòng lặp này lặp qua danh sách
    # các khuôn mặt được phát hiện trong biến faces. Mỗi phần tử trong danh sách là một bộ 4 giá trị,
    # tương ứng với tọa độ và kích thước của mỗi khuôn mặt được phát hiện.
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    # vẽ hộp chứa khuôn mặt
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

    return img

camera = cv2.VideoCapture(0)
# tạo 1 cửa sổ để hiển thị
cv2.namedWindow('Video player', cv2.WINDOW_NORMAL)

# cứ 200 frame thì mình sẽ save 1 frame
interval = 10
count = 0

# hiển thị ra số fps
font = cv2.FONT_HERSHEY_SIMPLEX
fontColor = (255, 255, 255)
fontThickness = 2

# hiển thị từng khung ảnh
while True:
    # thời gian trước khi đọc 1 frame
    startTime = time.time()

    # Gọi method read của object myVideo để đọc từng frame
    # read() nó sẽ trả về 2 giá trị 1 là boolean nếu đọc thành công nó trả về true ngược lại trả về false
    # trả về 1 mảng (ảnh) numpy mỗi giá trị đại diện cho 1 pixel
    ret, frame = camera.read()

    #Thoát khi ko thể đọc được frame
    if not ret:
       break

    # tăng count
    count = count+1
    if(count % interval == 0):
        cv2.imwrite(f'./imgIdentifyFace/image_{count}.jpg', frame)

    # thời gian sau khi đọc
    endTime = time.time()

    # Tính fps
    # vd: đọc 1 frame thì mất 0.1s thì ta lấy 1/0.1 thì 1s ta đọc đc 10 frame
    fps = 1/(endTime - startTime)

    #detect face + eys
    frame = detect(frame)

    #ghi số lượng fps
    cv2.putText(frame, f'FPS: {fps:.2f}', (10,30), font, 1, fontColor, fontThickness)

    # hiển thị
    cv2.imshow('Video player', frame)

    if(cv2.waitKey(10) == ord('q')):
        break

# dùng để giải phóng tài nguyên sau khi kết thúc vc sử dụng nó
camera.release()
cv2.destroyAllWindows()