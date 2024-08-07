import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

#line chart
# x và y phải có giá trị bằng nhau
x = [1,5,3,10,15]
y = [10,20,30,15,3]

x2 = [4,2,4,10,11,12]
y2 = [2,4,1,5,3,4]

plt.plot(x,y,'go-', label = 'Công ty A')
plt.plot(x2,y2,'bo-', label = 'Công ty B')
plt.legend() # hàm này kết hợp vs label để hiện ra chứ thích dữ liệu
plt.xlabel('Trục X')
plt.ylabel('Trục Y')
plt.show()

# #bar chart
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [15, 10, 25, 12, 18]
# barChart = plt.bar(categories, values, color = 'b', alpha = 0.6)
# plt.bar_label(barChart, fmt = '%d') # cần chuyền vào 1 object biểu đồ, fmt = '%d' hiển thị số liệu
# plt.xlabel('Danh mục')
# plt.ylabel('Giá trị')
# plt.show()


# #pie chart
# myLabels = ['A', 'B', 'C', 'D', 'E']
# # size này ko đồng nghĩa với % trên biểu đồ mà tổng size là 100% sau đó nó sẻ chia tỉ lệ ra
# size = [15,30,45,10,20]
# myColors = ['red', 'green', 'blue', 'yellow', 'cyan']
#
# # autopct = '%.1f%%' : từ trái qua phải % đại diện cho nhìu con số 1f% sau
# # dấu . đại diện 1 số thập phân sau dấu , % tiếp theo là dấu %
# plt.pie(size, labels = myLabels, colors = myColors, autopct = '%.1f%%')
# plt.title('Biểu đồ hình tròn')
# plt.show()

# #scatter chart
# x = [1, 2, 3, 4, 5]
# y = [10, 16, 20, 30, 25]
# plt.scatter(x, y, c ='r', marker = 'o' , label = 'Dữ liệu')
# plt.xlabel('Trục x')
# plt.ylabel('Trục y')
# plt.legend()
# plt.show()


# #box plot
# data = [15, 18, 22, 30, 35, 45, 50, 55, 65]
# plt.boxplot(data)
# plt.title('Biểu đồ hộp')
# plt.ylabel('Giá trị')
# plt.show()


# # violinplot
# data = [15, 18, 22, 30, 35, 45, 50, 55, 65]
# plt.violinplot(data)
# plt.title('Biểu đồ violin')
# plt.ylabel('Giá trị')
# plt.show()

# # library wordclound
# text = 'Python is amazing language for data visualiztion and word clouds'
#
# wordcloud2 = WordCloud(width = 800, height = 400).generate(text)
#
# plt.imshow(wordcloud2, interpolation = 'bilinear')
# plt.axis('off')
# plt.title('Biểu đồ đám mây từ văn bản ví dụ')
# plt.show()

# # polar chart (biểu đồ rada)
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [22,10,3,22,3]
#
# N = len(categories)
# values += values[:1]
#
# angles = [n / float(N) * 2 * np.pi for n in range(N)]
# angles += angles[:1]
#
# plt.polar(angles, values, 'o-', linewidth = 2)
# plt.fill(angles, values, 'b', alpha = 0.1)
# plt.title('Biểu đồ radar ví dụ')
# plt.show()