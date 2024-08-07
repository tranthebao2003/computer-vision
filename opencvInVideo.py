import time
import cv2

# đọc video từ 1 file
myVideo = cv2.VideoCapture('./img/video.mp4')

# tạo 1 cửa sổ để hiển thị
cv2.namedWindow('Video player', cv2.WINDOW_NORMAL)

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
    ret, frame = myVideo.read()

    #Thoát khi ko thể đọc được frame
    if not ret:
       break

    # thời gian sau khi đọc
    endTime = time.time()

    # Tính fps
    # vd: đọc 1 frame thì mất 0.1s thì ta lấy 1/0.1 thì 1s ta đọc đc 10 frame
    fps = 1/(endTime - startTime)

    #ghi số lượng fps
    cv2.putText(frame, f'FPS: {fps:.2f}', (10,30), font, 1, fontColor, fontThickness)

    # hiển thị
    cv2.imshow('Video player', frame)

    """
        Hàm cv2.waitKey() chờ để nhận một sự kiện từ bàn phím trong một 
        khoảng thời gian được chỉ định (ở đây là 10 miligiây).
        Nếu không có sự kiện nào từ bàn phím trong khoảng thời gian chờ, 
        hàm này trả về một giá trị âm (-1).Nếu có sự kiện từ bàn phím được nhận, 
        hàm sẽ trả về mã ASCII tương ứng với phím được nhấn.
        ord('q'):Hàm ord() trả về mã ASCII của ký tự được chuyển đổi thành 
        đối số của nó (trong trường hợp này là ký tự "q").
    """
    if(cv2.waitKey(10) == ord('q')):
        break

# dùng để giải phóng tài nguyên sau khi kết thúc vc sử dụng nó
myVideo.release()
cv2.destroyAllWindows()