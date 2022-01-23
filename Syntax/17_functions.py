# 函数传递信息
def greet(username, age='30'):  # 括号内为形参。age为给形参指定默认值。使用默认值形参时，形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
    """简单的问候"""  # 此处三个双引号表示函数注释
    print(username + "'s age is " + age + '.')


# 位置实参
greet('Eurus', '25')  # 注意实参的顺序要与形参一致。函数内形参只能是str格式
# 关键字实参
greet(age='26', username='Grace')  # 不用在乎顺序。写内部语句时又不需要空格
# 默认实参
greet('Jack')
print('...')


# 返回值 & 实参可选
def number_sum(number_1, number_2, number_3=''):  # 实参number_3指定一个空字符串，并移至末尾，使其变为可选实参。
    if number_3:
        number = int(number_1) + int(number_2) + int(number_3)
    else:
        number = int(number_1) + int(number_2)
    return number  # 使用return语句将值返回到调用函数的代码行。需要用一个变量用于存储返回值。

print(number_sum('5', '3', '6'))
print('...')


# 返回字典 & 实参可选
def build_name(first_name, last_name, middle_name=''):
    person = {'first': first_name, 'last': last_name}
    if middle_name:
        person['middle'] = middle_name
    return person

print(build_name('Eurus', 'Zhang', 'Ran'))
print('...')


# 任意数量的实参 & 位置实参
def make_pizza(size, *toppings):  # *表示创建一个名为toppings的空元组，并将收到的所有值都封存在这个元组中。
    print('\nMaking a pizza with the following ' + str(size) + ' toppings: ')  # 这里要将输入的size转换为str
    for topping in toppings:
        print('-' + topping.title())

make_pizza(13, 'sugar')
make_pizza(34, 'mushrooms', 'green peppers', 'extra cheese')
print('...')


# 使用任意数量的关键字形参
def build_profile(first, last, **user_info):  # **表示创建一个名为user_info的空字典
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last  # 此处定义字典还可以有此方式：profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

print(build_profile('Eurus', 'Zhang', Location='Shanghai', Company='DJI'))
print('...')



# 将函数存储在模块中
# 首先将函数单独存为一个模块即.py文件：
# def make_cake(size, *toppings):
#     print('\nMaking a cake with the following ' + str(size) + ' toppings: ')  # 这里要将输入的size转换为str
#     for topping in toppings:
#         print('-' + topping.title())

# import subfunctions  # 函数名称命名不能以数字开头。若要调用被导入模块中的函数，用句号分隔。
'''
用import导入整个函数模块，然后用module_name.function_name()使用其中特定的函数
用import.function_name导入函数模块中的某一个特定函数
'''


'''
若模块文件（.py文件）中包含多个定义的函数，可以选择导入特定的函数，此时调用函数就无需使用句点，即：
from "module_name" import "function_name"

若导入模块中所有的函数，即：
from "module_name" import *

也可以将导入的函数名称命名为其它名字，后续即可使用替换过的函数名，即：
from "module_name" import "function_name" as "f_n"

也可以给导入的模块重新命名，即
import "module_name" as "m_n"
'''


# subfunctions.make_pizza(13, 'sugar')
# subfunctions.make_pizza(34, 'mushrooms', 'green peppers', 'extra cheese')
# print('...')

# 函数编写指南
'''
1：函数名称应只使用小写字母和下划线
2：函数定义后，后面紧跟注释
3：函数定义时，给形参指定默认值和函数调用中给定实参时，等号两边不要有空格
4：代码行不应超过79字符，可以换行缩进输入
5：程序或模块中若有多个函数，可使用两行空行将各个函数分开
6：所有import语句都应放在开头，除非文件开头使用了注释来描述整个程序
'''