import os
from PIL import Image

def loadImage(imagePath):
    # Đọc ảnh từ đường dẫn cho trx và trả về đối tưởng ảnh
    #nếu sử dụng try except thì nếu bị lỗi thì chương trình phía sau vẫn chạy đc
    try:
        img = Image.open(imagePath)
        return img
    # nó sẽ bắt tất cả ngoại lệ (lỗi) và gán lỗi đó vào biến e
    # sau đó in ra string, path, cái lỗi đó và trả về none ngụ ý là ko thể mở ảnh
    except Exception as e:
        print('Lỗi khi đọc hình ảnh từ', imagePath, ' ', e)
        return None


def isImageFile(filePath):
    """
    return True - nếu là ảnh
            False - nếu khác ảnh
    """
    # là kiểu tubple nếu quên xem lại
    extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")
    # lower() và viết thường hết, endswith là kiểm tra phần mở rộng của đường path nó trong tuple extensions ko
    return filePath.lower().endswith(extensions)

def getImgList(folderPath):
    # tạo 1 list
    imgList = []
    # t1 kiểm tra xem đường dẫn có tồn tại hay ko và xem nó có phải là 1 folder hay ko
    # os.path.exists(folderPath): trả về true nếu nó có tồn tại, false nếu đường dẫn ko tồn tại
    # os.path.isdir(folderPath): trả về true nếu nó là 1 folder ngược lại trả về false
    if os.path.exists(folderPath) and os.path.isdir(folderPath):
        #os.listdir(folderPath): lấy toàn bộ ảnh trong folder
        fileNames = os.listdir(folderPath)
        for fileName in fileNames:
            # nó sẽ kết hợp giữa đường dẫn với fileName để ra 1 đường dẫn hoàn chỉnh đến từng file đó
            filePath = os.path.join(folderPath, fileName)
            # kiểm tra xem đường path của từng file trong floder nó có phải là 1 file hay ko and nó có phải 1
            # tấm ảnh hay ko
            if os.path.isfile(filePath) and isImageFile(filePath):
                img = loadImage(filePath)
                imgList.append(img)
    return imgList

