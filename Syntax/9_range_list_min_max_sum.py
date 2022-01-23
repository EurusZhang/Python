# for i in range(11):  # 创建一个从0开始，到10停止的列表，元素个数为11
#     print(i)
# print('...')

# for value in range(1,5):  # 打印1-4，大于或等于5时打印停止
#     print(value)
#
# numbers_1 = list(range(1,6))  # 用list()创建数字列表
# print(numbers_1)
#
# numbers_2 = list(range(2,10,2))  # range()功能为打印从2开始，依次递增2，大于或等于10时打印停止
# print(numbers_2)

# squares = []  # 创建空列表
# for value in range(1,11):
#     square = value**2  # **表示乘方运算
#     squares.append(square)
#     print(squares)
# print(squares)

# numbers = list(range(1,6))
# print(min(numbers),max(numbers),sum(numbers))  # min，max，sum求列表中最小值、最大值、和

squares = [value**2 for value in range(1,6)]  # 列表解析：将for循环和创建新元素代码合为一行
print(squares)