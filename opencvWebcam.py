import time
import cv2

# cv2.VideoCapture(0): đọc video từ camera1, nếu có nhiều camera thì cứ đánh dấu từ 0 đến n
camera = cv2.VideoCapture(0)

# tạo 1 cửa sổ để hiển thị
cv2.namedWindow('Video player', cv2.WINDOW_NORMAL)

# cứ 5 frame thì mình sẽ save 1 frame
interval = 5
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
        cv2.imwrite(f'./imgWebcam/image_{count}.jpg', frame)

    # thời gian sau khi đọc
    endTime = time.time()

    # Tính fps
    # vd: đọc 1 frame thì mất 0.1s thì ta lấy 1/0.1 thì 1s ta đọc đc 10 frame
    fps = 1/(endTime - startTime)

    #ghi số lượng fps
    cv2.putText(frame, f'FPS: {fps:.2f}', (10,30), font, 1, fontColor, fontThickness)

    # hiển thị
    cv2.imshow('Video player', frame)

    if(cv2.waitKey(10) == ord('q')):
        break

# dùng để giải phóng tài nguyên sau khi kết thúc vc sử dụng nó
camera.release()
cv2.destroyAllWindows()