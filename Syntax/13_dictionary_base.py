# dictionary：字典，
# 即一系列键-值对。
# 键值一一对应。值可以为数字、字符串、列表、字典，可以为Python对象。
# 字典中可以包含任意数量的键-值对。

alien = {'color': 'green', 'points': '5'}  # 创建字典的第1种方式。用{}表示字典，冒号前为键，冒号后为值。键-值对之间用逗号分隔。
alien['x_position'] = 0  # 创建字典的第2种方式。先用空花括号{}创建一个空字典，然后向字典添加键-值对。
alien['y_position'] = 1  # 该方法也可用于修改字典中的值
print(alien)  # 打印整个字典
print(alien['color'])  # 访问字典中的值
print(alien['points'])

del alien['color']  # 用del语句永久性删除字典中某一键-值对
print(alien)

print('\n', '------ I am Dividing line ------', '\n')

languages = {
    '1st': 'c',
    '2nd': 'python',
    '3rd': 'c++',
    }  # 创建字典第1种方式的另一种书写方式，更清晰，适用于较长的字典。末尾的花括号前要加一个制表符。

print('My favorite language is ' +
      languages['2nd'].title() +  # 在合适的地方换行拆分内容。
      '.')

# 遍历字典
# 用方法.items()遍历字典中的所有键-值对
for order, language in languages.items():
    print(order + ' coding language is ' + language.title() + '.')
# 用方法.keys()遍历字典中的所有键。
for order in languages.keys():  #遍历字典时，会默认遍历所有的键，即该语句也可以改为for order in languages:，输出不变
    print(order)
# 用函数sorted()排序
for order in sorted(languages.keys()):  # 先列出字典中所有键，然后用函数sorted()将所有的键排序
    print(order)
# 用方法.values()遍历字典中的所有值
# 用函数”集合set()“剔除重复项，使得列表中元素都独一无二
