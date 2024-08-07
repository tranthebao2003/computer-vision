import numpy as np
import cv2
import os
import pickle

"""
this is project final so all things studied before lessons and special is lesson,
if you don't remember please can see again
"""

# face detection model
face_Detection_Model = './res10_300x300_ssd_iter_140000_fp16.caffemodel'

# mô tả kiến trúc
face_Detection_Proto = './deploy.prototxt.txt'

# mô hình mô tả đặc trưng của face
face_Descriptor = './openface.nn4.small2.v1.t7'

# sử dụng OpenCV DNN đọc mô hình nhận diện khuôn mặt
dectector_Model = cv2.dnn.readNetFromCaffe(face_Detection_Proto, face_Detection_Model)

# Đọc mô hình đặc tả khuôn mặt từ file Torch (meta)
descriptor_Model = cv2.dnn.readNetFromTorch(face_Descriptor)


# tạo ra 1 function để áp dụng cho nhiều ảnh
def detect(imgPath):
    # trích xuất đặc trưng cho 1 ảnh
    img1 = cv2.imread(imgPath)

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
        i = np.argmax(
            detections[0, 0, :, 2])  # ':'chọn all khuôn mặt và lấy chỉ số thứ 2 của những face đó => confidence
        # i = np.argmax(detections[0,0, :,2]): nó sẽ trả về khuôn mặt có độ tin cậy cao nhất
        confidence = detections[0, 0, i, 2]

        # kiểm tra face có confidence max thì nó có lớn hơn 0.5 ko
        if (confidence > 0.5):
            # tính toán hộp bao quanh khuôn mặt
            # Mình sẽ lấy value của index từ 3 đến 6 nhân với kích thước widthm height
            # để ra đc tọa độ thật của box chứa face nhận dạng đc t(ương tự trong bài identifyFaceDnn)
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            # chuyển đổi từ box float sang int và lưu chữ trog các biến tương ứng
            (startX, startY, endX, endY) = box.astype('int')

            # detection vùng ảnh chứa khuôn mặt ra
            # Dòng mã này tạo ra một vùng (region) mới trong ảnh gốc (imgCopy) bằng cách cắt (crop) ra một phần
            # của ảnh dựa trên tọa độ của bounding box đã tính toán trước đó.
            regionOfImg = imgCopy[startY:endY, startX:endX]

            # chuẩn bị dữ liệu đầu vào cho mô hình trích xuất đặc trưng
            """
            Chuẩn bị dữ liệu đầu vào cho mô hình trích xuất đặc trưng
            tạo Blob từ ảnh, Blob là một cấu trúc dữ liệu được sử dụng
            trong deep learning để biểu diễn dữ liệu hình ảnh.
            1 / 255 là tỷ lệ tỷ lệ màu, thông thường là 1/255 để chia tỷ lệ giá trị pixel từ 0-255 thành 0-1,
            phù hợp với đầu vào của mạng neural network.
            SwapRB=True có nghĩa là hoán đổi các kênh màu đỏ và xanh lá cây. 
            Trong OpenCV, các hình ảnh màu thường được biểu diễn dưới dạng BGR,
            nhưng một số mô hình deep learning yêu cầu đầu vào ở dạng RGB, do đó cần phải hoán đổi các kênh màu.
            Crop=True có nghĩa là cắt ảnh để có kích thước đúng (crop) nếu kích thước của ảnh không phù hợp với kích thước mục tiêu
            """
            faceBlob = cv2.dnn.blobFromImage(regionOfImg, 1 / 255, (96, 96), swapRB=True, crop=True)

            # thiết lập mô hình đầu vào cho mô hình
            descriptor_Model.setInput(faceBlob)

            # thực hiện việc trích xuất đặc trưng
            vectors = descriptor_Model.forward()

            # print vectors
            return vectors


# apply for all images

# khởi tạo 1 dictionary và lưu data kèm theo nhãn của nó
data = dict(data=[], label=[])

mydir = './imgTraining'
floders = os.listdir(mydir)

# duyệt qua từng thư mục
for folder in floders:
    path = mydir + '/' + folder

    # duyệt qua từng file trong từng folder
    files = os.listdir(path)
    for fileName in files:
        # ta thử xem nó có triết xuất đặc trưng cho từng tấm ảnh đc ko
        # nếu ko thì vector đó none và nếu thế thì ta sẻ bỏ qua luôn
        try:
            # gọi hàm chiết xuất đặc trưng
            vector = detect(path + '/' + fileName)

            # kiểm tra vc trích xuất đặc trưng thành công
            if vector is not None:
                data['data'].append(vector)
                data['label'].append(folder)
        except:
            pass

# print(data)
# # data: nó sẽ trả về cho mik 1 dictionary gồm 2 từ khóa là data, label
# # giá trị của data là 1 list rất nhìu mảng tương ứng vs số face đc phát hiện
# # và mỗi phần tử trong list đó lại là 1 array 2 chiều chứa 128 đặc trưng tương
# # ứng cới 128 giá trị của cái face đó. Tương ứng mỗi face thì sẽ được gán nhãn
# # và nằm trong 1 list và list này chính là giá trị của key 'label'

# # tạo 1 series từ dictionary
# labelSeries = pd.Series(data['label'])
#
# # đếm số lần xuất hiện của mỗi label
# labelCounts = labelSeries.value_counts()
# print(labelCounts)

# Save data thành file
# wb: write binar. Vì thế method dưới đây sẽ ghi đè dữ liệu
pickle.dump(data, open('./data_face_features.pickle', mode='wb'))
