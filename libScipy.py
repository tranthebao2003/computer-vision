"""
- SciPy là 1 thư viện mã nguồn mở trong ngôn ngữ lập trình python
dùng cho tính toán khoa học và kỹ thuật
- Nó cung cấp 1 tập hợp rộng rãi các chức năng và công cụ để giải
quyết các vấn đề phức tạp trong nhiều lĩnh vực, từ toán học
đến khoa học dữ liệu
- Scipy được xây dựng trên NumPy
"""

from scipy import linalg
import numpy as np

# giải hệ phương trình tuyến tính
"""
a1x + b1y = c
a2x + b2y = d
Tìm x, y bằng ma trận ngày xưa
[a1, b1
 a2, b2] 
 
 [c, d]
"""

# Định nghãi hệ phương trình tuyến tính
"""
theo vd Dưới ta có hpt: 2x + y = 5 và 3x + 2y = 7
"""
A = np.array([[2, 1],[3, 2]])
B = np.array([5, 7])

# giả hpt tuyến tính
x = linalg.solve(A, B)

print("kết quả x, y: ", x)

#tính tích phân của 1 hàm số
from scipy import integrate

# định nghĩa hàm f(x) = x^2
def myFunction(x):
    return x ** 2

# tính tích phân của f(x) từ 0 đến 1
integral = integrate.quad(myFunction, 0, 1)
print("Tích phân của f(x) từ 0 đến 1: ", integral)

# tính giá trị riêng và vector riêng của 1 ma trận:
matrix = np.array([[2,1], [3,2]])


eigenValue, eigenVector = linalg.eig(matrix)
print("Giá trị riêng", eigenValue)
print("Vector riêng", eigenVector)