Week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# 用“[]”表示列表，用逗号分隔元素

# print(Week)
# print(Week[0].title())  # “列表名[数字]”访问列表元素，并且索引从0开始
# print(Week[-1])  # [-1]表示访问列表中倒数第1个元素
# print(Week[-2])  # [-2]表示访问列表中倒数第2个元素
# print(Week[-3])  # [-3]表示访问列表中倒数第3个元素

# Week[0] = 'monday'  # 修改列表中某一位元素，直接覆盖
# print(Week)

# Week.append('Seven')  # 用方法.append()将元素添加进列表末尾
# print(Week)

# Week.insert(0,'Seven')  # 用方法.insert()在列表中特定位置添加特定元素
# print(Week)

# del Week[0]  # 用函数del删除列表中特定位置的元素
# # print(Week)

# pop_Week = Week.pop()  # 用方法.pop()默认删除列表末尾的元素，并将删除的元素放在给定变量中
# print(Week)
# print(pop_Week)

# pop_Week = Week.pop(1)  # 用方法.pop()删除列表中任意位置的元素，并将删除的元素放在给定变量中
# print(Week)
# print(pop_Week)

Week.remove('Wednesday')  # 用方法.remove()删除列表中特定的元素值
print(Week)
Del_Element = 'Monday'
Week.remove(Del_Element)
print(Week)
