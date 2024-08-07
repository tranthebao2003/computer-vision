import cv2
import numpy as np

# mở webcam
camera = cv2.VideoCapture(0)
# face detection model
face_Detection_Model = './model/res10_300x300_ssd_iter_140000_fp16.caffemodel'

# mô tả kiến trúc
face_Detection_Proto = './model/deploy.prototxt.txt'

# mô hình mô tả đặc trưng của face
face_Descriptor = './model/openface.nn4.small2.v1.t7'

# sử dụng OpenCV DNN đọc mô hình nhận diện khuôn mặt
dectector_Model = cv2.dnn.readNetFromCaffe(face_Detection_Proto, face_Detection_Model)

# Đọc mô hình đặc tả khuôn mặt từ file Torch (meta)
descriptor_Model = cv2.dnn.readNetFromTorch(face_Descriptor)


"""
Tóm lại function này là: đầu tiên đọc ảnh, copy ảnh (ko xử lí trên ảnh gốc), nhận
diện face lọc ra face có confidence max sau đó crop lấy vùng face đó trên tấm ảnh copy
"""
def detect_facial_feature_extraction(imgInput):
    # trích xuất đặc trưng cho 1 ảnh
    # img1 = cv2.imread(imgInput)
    img1 = imgInput #(1 tấm ảnh)

    # copy ảnh
    imgCopy = img1.copy()

    # lấy width and height (shape[:2]: chỉ lấy 2 dữ liệu đầu tiên
    h, w = imgCopy.shape[:2]

    # chuẩn bị dữ liệu đầu vào cho mô hình nhận diện khuôn mặt
    imgBlob = cv2.dnn.blobFromImage(imgCopy, 1, (300, 300), (104, 177, 123), swapRB=False, crop=False)

    # thiết lập đầu vào cho mô hình
    dectector_Model.setInput(imgBlob)

    # thực hiện vc nhận diện khuôn mặt
    detections = dectector_Model.forward()

    # in confidence của all khuôn mặt
    # print(detections[0,0,:,2])

    # kiểm tra xem có khuôn mặt nào hay không
    if (len(detections) > 0):
        # chọn khuôn mặt có độ tin cậy cao nhất (confidence) cao nhất
        #  np.argmax: hàm sẽ tìm kiếm phần tử lớn nhất trong toàn bộ mảng và trả về chỉ số tương ứng.
        i = np.argmax(detections[0, 0, :, 2])  # ':'chọn all khuôn mặt và lấy chỉ số thứ 2 của những face đó => confidence
        # i = np.argmax(detections[0,0, :,2]): nó sẽ trả về khuôn mặt có độ tin cậy cao nhất
        confidence = detections[0, 0, i, 2] # độ tin cậy của khuôn mặt có độ tin cậy max

        # kiểm tra face có confidence max thì nó có lớn hơn 0.5 ko
        if (confidence > 0.5):
            # tính toán hộp bao quanh khuôn mặt
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype('int')

            # vẽ hình chữ nhật xung quanh faces detected
            cv2.rectangle(imgCopy, (startX, startY), (endX, endY), (0, 255, 0), 2)
            # :.2f: lấy phần trước dấu , và lấy 2 số sau dấu ,
            text = 'Face: {:.2f}%'.format(confidence * 100)
            cv2.putText(imgCopy, text, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
            cv2.imshow('Video player', imgCopy)

            # detection vùng ảnh chứa khuôn mặt ra (regionOfImg là mảng đã crop (ảnh))
            regionOfImg = imgCopy[startY:endY, startX:endX]

            faceBlob = cv2.dnn.blobFromImage(regionOfImg, 1 / 255, (96, 96), swapRB=True, crop=True)

            # thiết lập mô hình đầu vào cho mô hình
            descriptor_Model.setInput(faceBlob)

            # thực hiện việc trích xuất đặc trưng
            vectors = descriptor_Model.forward()

            # print vectors
            # tới đây
            # return vectors, faceBlob
            print(vectors)


# hiện tại đã kết hợp đc lấy ảnh từ camera xđ face, lấy đc triết xuất đặc trưng
# Tạm thời dừng ở đây vì phần sau huấn luyện model thì liên quan CNN 1 phần của deep
# learning: https://www.youtube.com/watch?v=swguqT77ZLE&list=PL8ZSveYn9kVT0DcOXQKcnuhLlCZeG3a-k. Học thêm ở đường lik này
# hoặc TITV có ra thêm video về computer vision thì xem tiếp. Nếu học seri mới thì phải học từ đầu
while True:
    ret, frame = camera.read()
    # nếu có nhìu hình ảnh thì phải bỏ đoạn dưới vào for
    #chuẩn bị dữ liệu đầu vào

    if not ret:
        break

    detect_facial_feature_extraction(frame)

    if (cv2.waitKey(1) == ord('q')):
        break

camera.release()
cv2.destroyAllWindows()