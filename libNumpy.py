import numpy as np
"""
- Numpy được viết bằng C, nhanh hơn việc sử dụng list trong python
- Numpy xử lí mảng đa chiều dễ dàng
- Hỗ trợ đa dạng loại dữ liệu số học
"""

# # tạo mảng
# a = np.array([1, 2, 3])
#
# # in mảng ra
# print(a)
#
# # in ra 1 phần tử
# element = a[1]
# print(element)
#
# # tạo mảng 2 chiều
# matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print('Matrix')
# print(matrix)
#
# #[1,2]: dòng 1 cột 2
# print(matrix[1,2])


# #tạo mảng toàn số 0
# arrayZero = np.zeros(5)
# arrayOne = np.ones(6, dtype=np.int64) #: dtype=np.int64: kiểu dữ liệu của giá trị trog mảng
# arrayEmpty = np.empty(0)
# print(type(arrayOne[2]))
# print(arrayEmpty)
# print(arrayZero)
# print(arrayOne)

# # tạo mảng từ 0 đến 100
# # np.arange(n). Trả về 1 mảng nó n phần từ bắt đầu từ 0
# zeroToHundred = np.arange(101)
# print(zeroToHundred)

# Tạo mảng gồm các phần tử với khoảng cách đều nhau
# linspace(0, 10, num = 5): return array có 5 phần tử khoảng cách giá trị = nhau
# và có giá trị từ 0 đến 10 có
equalValue = np.linspace(0, 10, num = 5)
print(equalValue)

# add, remove, sort array
# arr = np.array([3, 1, 2, 4, 5])

# # sort ascending
# arr = np.sort(arr)
# print('sort Accesing',arr)
#
# sort descending: thêm dấu - vào lib numpy và - vào mảng
# arr = -np.sort(-arr)
# print('sort descending',arr)

# # add
# arr = np.append(arr, 100)
# print(arr)
#
# # remove at index
# arr = np.delete(arr, 3)
# print(arr)

# #sort acsending Row in array 2 dimensionalc
# matrix = np.array([[3,2,1], [4,6,5], [9,7,8]])
# sortRow = np.sort(matrix, axis=1)
# print('Sắp xếp tăng dần theo hàng\n', sortRow)
#
# #sort acsending Column in array 2 dimensionalc
# sortColumn = np.sort(matrix, axis=0)
# print('Sắp xếp tăng dần theo cột\n', sortColumn)
#
#
# #sort descending Row in array 2 dimensionalc
# matrix = np.array([[3,2,1], [4,6,5], [9,7,8]])
# sortRow = -np.sort(-matrix, axis=1)
# print('Sắp xếp giảm dần theo hàng\n', sortRow)
#
# #sort descending Column in array 2 dimensional
# sortColumn = -np.sort(-matrix, axis=0)
# print('Sắp xếp giảm dần theo cột\n', sortColumn)

# #Tạo 1 mảng 2d
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# # sử dụng các thuộc tính để lấy thông tin về mảng
# dimensional = arr.ndim #(số chiều): 2
# sizeArray = arr.size #kích thước là tổng số ptu: 6
# shapeArr = arr.shape #Hình dạng (số hàng, số cột)
#
# print('Số chiều:',dimensional)
# print('Kích thước:',sizeArray)
# print('Hình dạng:',shapeArr)

# #chuyển đổi kiểu dữ liệu cho mảng
# arrInt = np.array([1,2,3,4,5])
# print(arrInt)
# arrFloat = arrInt.astype(float)
# print(arrFloat)
#
# # thay đổi hình dạng của mảng
# arrShade = np.array([1,2,3,4,5,6])
# print(arrShade.shape)
# reshapeArr = arrShade.reshape(2, 3)
# print(reshapeArr)
# reshapeArr2 = arrShade.reshape(3, 2)
# print(reshapeArr2)
#
# #biến mảng đa chiều thành mảng 1 chiều
# flatArry = reshapeArr2.flatten()
# print(flatArry)
#
# cắt mảng
array2 = np.array([[[[1,2,3,4,5,-1,-2],[6,7,8,9,10,-3,-4],[11,12,13,14,15,-5,-6],[16,17,18,19,20,-7,8]]]])
#array2 là mảng 4 chiều và mỗi chiều sẽ có 7 phần tử phục vụ cho DNN

print(array2.shape)
subArr1 = array2[0, 0, 3, 3:7] # cắt từ phần tử thứ 1 đến phần t3
print('array2[1:4]: ', subArr1)

# bỏ đi phần tử cuối cùng trong mảng: bởi vì nó đi lui
# phần tử đầu tiên là 0 thì đi lui phần tử cuối cùng sẽ là -1
# mặc định ban đầu nó lấy từ index bằng 0 đến index -1
subArr2 = array2[:-1]
print('array2[:-1]: ', subArr2)

# chỉ lấy phần tử -2 đến cuối cùng trong mảng
subArr3 = array2[-2:]
print('array2[-2:]: ', subArr3)

# # để chuyển vị mảng, chúng ta có thể sự dụng .T hoặc hàm numpy.transpose().
# arrayBd = np.array([[1,2,3], [4,5,6]])
# print(arrayBd)
# arrayTranspose = arrayBd.T
# print(arrayTranspose)
#
# # nối mảng
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
#
# arr12 = np.concatenate((arr1, arr2))
# print(arr12)

# #II hàm tính tổng các phần tử trong mảng
# arr4 = ([1,2,3,4])
# total = np.sum(arr4)
# print('Tổng các phần tử trong mảng', total)
#
# #III hàm tính trung bình của các ptu trong mảng
# average = np.mean(arr4)
# print('Trung bình của các phần tử trong mảng', average)
#
# #IV tìm max min trong mảng
# maxValue = np.max(arr4)
# minValue = np.min(arr4)
# print('Max value', maxValue)
# print('Min value', minValue)
#
# #hàm tính độ lệch chuẩn (standard deviation)
# # hàm numpy.std() tính độ lệch chuẩn của mảng, đo lường mức độ
# # phân tán của dữ liệu
# stdDeviation = np.std(arr4)
# print('Độ lệch chuẩn: ',stdDeviation)
#
# #hàm tính phương sai (variance)
# # hàm numpy.var() tính phương sai của mảng, đo lường mức độ biến thiên
# # của dữ liệu.
# variance = np.var(arr4)
# print('Phương sai của mảng arr:', variance)
#
# #hàm tính tổng tích chập (dot product)
# # hàm numpy.dot() tính tổng tích chập của 2 mảng (vector)
# arr5 = np.array([1, 2, 3])
# arr6 = np.array([4, 5, 6])
# docProduct = np.dot(arr5, arr6)
# print('Tổng tích chập của arr5 và arr6:', docProduct)