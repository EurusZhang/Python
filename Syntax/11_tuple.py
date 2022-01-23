# tuple: 元组。列表可以修改其中元素，元组即不可修改元素的列表。元组用圆括号()表示
dimensions = (200, 50, 30, 20, 10)
print(dimensions[0], dimensions[3])  # 访问元组中元素与访问列表中元素相同
for dimension in dimensions:  # 遍历元组中的所有值
    print(dimension)
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值，即覆盖元组的元素