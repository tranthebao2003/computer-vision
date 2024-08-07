from PIL import Image
import numpy as np


def imgToArray2d(path):
    #Đọc ảnh
    img = Image.open(path)
    #ảnh xám
    grayImg = img.convert('L')
    # convert img to array
    imgArray = np.array(grayImg)

    return imgArray