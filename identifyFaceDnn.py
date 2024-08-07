import cv2

# mở webcam
camera = cv2.VideoCapture(0)
# tải mô hình đã đc huấn luyện từ trước
net = cv2.dnn.readNetFromCaffe(
    './identifyFace/DNN/deploy.prototxt.txt',
    './identifyFace/DNN/res10_300x300_ssd_iter_140000_fp16.caffemodel'
)
while True:
    ret, frame = camera.read()
    # nếu có nhìu hình ảnh thì phải bỏ đoạn dưới vào for
    #chuẩn bị dữ liệu đầu vào

    if not ret:
        break
    """
    img: ảnh muốn phát hiện ra khuôn mặt
    scalefactor: tỉ lệ co dãn, ảnh sẽ ko bị co dãn
    size: đây là kích thước mà mô hình yêu cầu cho đầu vào
    mean: màu sắc trung bình
    swapRB = false: ko hoán đổi kênh màu red và blue
    """
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177, 123), swapRB=False)

    # đặt dữ liệu đầu vào cho mạng
    net.setInput(blob)

    # chạy mạng để phát hiện ra khuôn mặt
    faces = net.forward()

    # lấy kích thước của ảnh đầu vào
    h,w,d = frame.shape

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
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0,255,0), 2)
            # :.2f: lấy phần trước dấu , và lấy 2 số sau dấu ,
            text = 'Face: {:.2f}%'.format(confidence * 100)
            cv2.putText(frame, text, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
    cv2.imshow('Video player', frame)
    if (cv2.waitKey(1) == ord('q')):
        break

camera.release()
cv2.destroyAllWindows()