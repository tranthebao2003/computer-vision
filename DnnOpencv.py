"""
Deep neural network (DNN)
Ứng dụng của bài toán phát hiện khuôn mặt rất đa dạng, từ việc phát định khuôn mặt
trong ảnh chân dung, ghi dấu vùng khuôn mặt để tạo hiệu ứng mặt đẹp trên các ứng
dụng chỉnh sửa ảnh, đến việc xác định khuôn mặt để kiểm tra nhân tính, an ninh hoặc
điểm danh trong hệ thống nhận diện khuôn mặt

Deep lerning
Là 1 lĩnh vực trong trí tuệ nhân tạo và máy tính, tập trung vào việc sử dụng mạng
nơ-ron sâu để học và áp dụng kiến thức từ dữ liệu. Deep learning đc gọi là "sâu"
bởi vì nó sử dụng nhiều lớp nơ-ron hoặc các tầng ẩn để biểu diễn dữ liệu và học các
đặc trưng phức tạp và trừu tượng từ dữ liệu đầu vào

feature extraction (triết xuất đặc trưng)

Một số đặc điểm qtrog của deep learning:
- Học biểu diễn dữ liệu: deep learning cho phép mô hình học tự động các biểu diễn cấu trúc từ
dữ liệu, giúp tạo ra các đặc trưng phức tạp và trừu tượng từ dữ liệu đầu vào.
- Sử dụng mạng nơ-ron: deep learning thường sử dụng mạng nơ-ron, bào gồm mạng nơ-ron tích chập (CNN)
mạng nơ ron tái khám phá (RNN), và các kiến trúc khác, để thực hiện học và dự đoán
- Tích hợp lớp ẩn: Deep Learning sử dụng nhiều lớp nơ-ron ẩn liên tiếp để biểu diễn dữ liệu. Điều
này tạo ra sự phức tạp và linh hoạt trong vc học và áp dụng kiến thức

- opencv Deep Neural Network (DNN) là 1 phần mở rộng của Opencv cho phép tích hợp và sử dụng mạng nơ-ron
học sâu (deep learing) trong các ứng dụng thị giác máy tính
- opencv là 1 thư viện phổ biến trong lĩnh vực xử lý hình ảnh và thị giác máy tính, trong khi DNN module
cho phép bạn sử dụng các mô hình Deep Learning như mạng nơ-ron tích chập (CNN) để thực hiện nhìu nhiệm
vụ liên quan đến thị giác máy tính, chẳng hạn như phát hiện khuôn mặt, phân loại đối tượng, và thậm
chí là phát hiện đối tượng trog tg thực

4 thư viện qtrong: Caffe, TensorFlow(google), PyTorch(meta), Darknet

Các pp xác định face
-Haar Cascades: sử dụng các phân lớp AdaBoost và bộ lọc Haar để phát hiện khuôn mặt. Đây là 1 pp truyền
thống nhưng vẫn được sử dụng rộng rãi trog ứng dụng thời gian thực
-Mạng nơ-ron tích chập (CNN): sử dụng CNN để học đặc trưng khuôn mặt và dự đoán vị trí của chúng trong
hình ảnh. Một số kiến trúc CNN nổi tiếng như Viola-Jones, Single Shot MultiBox Detector (SSD), và Faster
R-Cnn đã đc sử dụng cho bài toán này
-Mạng học sâu (Deep learning): Sử dụng Deep learning như CNN, Mạng phát triển (DNN), hoặc các mô hình
đặc biệt như Mạng thần kinh đa mục tiêu (Milti-task Neural Networks) để tăng cường khả năng phát
hiện khuôn mặt
"""

import cv2
import numpy as np

img = cv2.imread('./img/face.png')


# tải mô hình đã đc huấn luyện từ trước
net = cv2.dnn.readNetFromCaffe(
    './identifyFace/DNN/deploy.prototxt.txt',
    './identifyFace/DNN/res10_300x300_ssd_iter_140000_fp16.caffemodel'
)

# nếu có nhìu hình ảnh thì phải bỏ đoạn dưới vào for
#chuẩn bị dữ liệu đầu vào
"""
img: ảnh muốn phát hiện ra khuôn mặt
scalefactor: tỉ lệ co dãn, ảnh sẽ ko bị co dãn
size: đây là kích thước mà mô hình yêu cầu cho đầu vào
mean: màu sắc trung bình
swapRB = false: ko hoán đổi kênh màu red và blue
"""
blob = cv2.dnn.blobFromImage(img, 1.0, (300, 300), (104, 177, 123), swapRB=False)

# đặt dữ liệu đầu vào cho mạng
net.setInput(blob)

# chạy mạng để phát hiện ra khuôn mặt
faces = net.forward()

# lấy kích thước của ảnh đầu vào
h,w,d = img.shape

# # in thông tin
# print(faces.shape[2]) # return (1, 1, 200, 7): lần lượt là số ảnh đầu vào, đầu ra, số faces đc phát hiện, và
# # thông số của từng face đó. Do đó, mỗi phần tử trong mảng faces là một phát hiện khuôn mặt, và mỗi phát hiện
# # có 7 giá trị tương ứng với các thuộc tính hoặc thông tin của khuôn mặt

#in ra thằng đầu tiên
"""
khi in ra thằng đầu tiên thì nó sẽ có 7 thông số bao gồm :
số thứ tự ảnh (ko chắc lắm), class id có value là 0 or 1 nếu là face thì là 1 ko phải là 0,
Confidence Score (độ tin cậy) là 1 float nằm trog khoảng từ 0 đến 1 giá trị này
càng cao thì độ tin cậy càng lớn. Tùy vào bài toán thực tế mà chọn những tấm ảnh
có confidence score phù hợp, x1 (hoành độ left top of rectangle), y1 (tung độ left top of rectangle),
x2 (hoành độ right bottom of rectangle), y2 (tung độ right bottom of rectangle)
"""
# print(faces[0,0,1,3:7])

# duyệt từng khuôn mặt đã đc phát hiện
# faces.shape[2]: 200 số khuôn mặt phát hiện đc
for i in range(0, faces.shape[2]):
    # confidence: độ tin cậy
    # i: thứ tự của khuôn mặt, 2: thứ tự của chỉ số độ tin cậy trong 7 thông số
    confidence = faces[0, 0, i, 2]
    # kiểm tra nếu mặt có độ tin cậy là 0.5 trở lên thì export
    # tùy theo thực tế mà chọn mức độ tin cậy phù hợp
    if confidence > 0.5:
        #Trích xuất tọa độ
        # mỗi face là 1 mảng 4 chiều và mỗi chiều sẽ có 7 phần tử mik chọn từ phần tử có index 0 đến index 6
        # ko hiểu có thể xem bài libNumpy
        # print(faces[0, 0, i, 3:7])

        # lấy những giá trị tọa độ (0 đến 1) nhân cho size của ảnh ban đầu sẽ ra đc tọa độ thật của ảnh (px)
        startX = int(faces[0, 0, i, 3] * w)
        startY = int(faces[0, 0, i, 4] * h)
        endX = int(faces[0, 0, i, 5] * w)
        endY = int(faces[0, 0, i, 6] * h)

        # vẽ hình chữ nhật xung quanh faces detected
        imgFaces = cv2.rectangle(img, (startX, startY), (endX, endY), (0,255,0), 2)
        # :.2f: lấy phần trước dấu , và lấy 2 số sau dấu ,
        text = 'Face: {:.2f}%'.format(confidence * 100)
        cv2.putText(imgFaces, text, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

cv2.imshow('Video player', imgFaces)
cv2.waitKey(0)
cv2.destroyAllWindows()