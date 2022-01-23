# slice：切片，即列表的部分元素
provinces = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'hongkong']
print(provinces[1:3])  # 输出列表中从索引1开始，到索引3前面的元素停止的元素，类似range
print(provinces[:3])  # 输出自动从列表开头开始的3个元素
print(provinces[3:])  # 输出从第三个元素开始到末尾的所有元素
print(provinces[-3:])  # 输出最后3位的元素

for province in provinces[:4]:
    print('I want to go to ' + province.title())

copy_provinces = provinces[:]  # [:]表示复制列表，即创建一个始于第一个元素，终止于最后一个元素的切片
copy_provinces.append('Weihai')
print(copy_provinces)
