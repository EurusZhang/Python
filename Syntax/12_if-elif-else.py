cars = ['audi', 'benz', 'bmw', 'lamborghini', 'porsche', 'ferrari']
for car in cars:
    if car == 'bmw':  # 用==检查是否相等，考虑大小写
        print(car.upper())
    else:
        print(car.title())

# if-else语句
age = 17
if age != 17:  # 用!=检查是否不相等
    print('lalala')
else:
    print('xixixi')

# 用>,<,>=,<=比较数字。使用该比较运算符时，两边要加一个空格。
# 用and,or检查多个条件

# 简单if语句
age = 11
ages = [12, 13, 14, 15]
if age in ages:  # 用关键字in检查特定值是否包含在列表中
    print('True')
if age not in ages:  # 用关键字not in检查特定值是否不包含在列表中
    print('False')

# if-elif-else语句及多个elif语句，也可以省略else
age = 12
if age < 8:
    print('hahaha')
elif age <= 12:
    print('henghengheng')
else:
    print('lueluelue')

# 布尔表达式：True和False