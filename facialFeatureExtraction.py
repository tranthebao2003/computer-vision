"""
Công nghệ nhận dạng khuôn mặt thường tìm kiếm những đặc trưng sau:
- Khoảng cách giữa 2 mắt
- Khoảng cách từ trán tới cầm
- Khoảng cách giữa mũi và miệng
- Độ sâu của hốc mắt
- Hình dạng của xương gò má
- Đường viền của môi, tai và cằm

Dlib shape predictors
Đây là 1 công cụ và thư viện mã nguồn mở trong lĩnh vực thị giác máy tính và xử lý
ảnh, được phát triển bởi Davis E. King. Dlib Shape Predictors chủ yếu được sử dụng
để nhận diện và dự đoán vị trí của các đặc điểm đặc trưng trên khuôn mặt, đặc biệt
là trong việc nhận diện và theo dõi các đặc điểm trên khuôn mặt của con người.

Được sử dụng để dự đoán và xaác định vị trí của các điểm đặc trưng trên khuôn mặt,
như mắt, miệng, mũi và các điểm trên mô hình 3d của khuôn mặt. Điều này cho phép
nhận diện và phân tích khuôn mặt một cách chi tiết
"""

import dlib
import cv2
from imutils import face_utils

faceLandmarksModelPath = './facialFeatureExtraction/shape_predictor_68_face_landmarks.dat'
faceRecognitionModelPath = './facialFeatureExtraction/dlib_face_recognition_resnet_model_v1.dat'

imgpath = './img/face.png'

# tạo object bộ nhận diện khuôn mặt
faceDetector = dlib.get_frontal_face_detector()

# đọc hình ảnh và phát hiện ra face
img = cv2.imread(imgpath)

# nhận diện các khuôn mặt bên trong ảnh
# nó sẽ trả về ds những face đc phát hiện với mỗi face đc bao bọc bởi hộp giới hạn
faces = faceDetector(img)

# Vòng lặp qua từng khuôn mặt
for face in faces:
    pointA = face.left(), face.top()
    pointB = face.right(), face.bottom()

    # tạo 1 object shape_predictor dự đoán các điểm đặc trưng trên khuôn mặt
    shapePredictor = dlib.shape_predictor(faceLandmarksModelPath)
    # shapePredictor(img, face): để dự đoán vị trí của các đặc trưng trên khuôn mặt đc
    # phát hiện (face) từ ảnh img

    faceShape = shapePredictor(img, face)

    # trả về 1 mảng numpy, trog đó mỗi hàng đại diện cho 1 đặc trưng và có 2 cột
    # là tọa độ (x,y) của đặc trưng đó trên hình ảnh
    faceShapeArray = face_utils.shape_to_np(faceShape)

    # tính toán đặt trưng của face
    # tạo 1 đối tượng từ tệp mô hình được chỉ định bởi biến faceRecognitionModelPath
    shapeDescriptor = dlib.face_recognition_model_v1(faceRecognitionModelPath)

    #  sử dụng đối tượng shapeDescriptor để tính toán mô tả khuôn mặt từ hình ảnh img và
    #  các landmarks faceShape. Kết quả là một vectơ mô tả khuôn mặt, thường có kích thước
    #  cố định và chứa các thông tin đặc trưng về khuôn mặt để sử dụng trong quá trình nhận
    #  dạng hoặc so sánh khuôn mặt.
    faceDescriptors = shapeDescriptor.compute_face_descriptor(img, faceShape)

    # print(faceDescriptors)
    # vẽ hình chữ nhật và các điểm đặc trưng lên hình ảnh
    cv2.rectangle(img, pointA, pointB, (0,255,0))
    for point in faceShapeArray:
        cv2.circle(img, tuple(point), 3, (255,0,0), -1)

# tóm lại bài toán ở trên là để xác định khuôn mặt và các đặc trưng của khuôn mặt đó để phục vụ cho việc
# nhận dạng khuôn mặt giải quyết bài toán xác định khuôn mặt đó là của ai
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()