# 根据类创建实例
class Dog:  # 创建类时,类名称后可以不接括号
    def __init__(self, name, age):  # init左右两边是两个下划线
        self.name = name
        self.age = age
        self.sex = 'male'  # 为该类指定默认属性sex，并设其默认值为male。此时就不需要在_init_方法里提供初始值形参

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' is rolled over.')

    def update_sex(self, gender):
        self.sex = gender


class Body:  # 定义一个小类
    def __init__(self, color, size=20):  # 这又是一种定义默认属性的方法，即在形参里直接定义
        self.color = color
        self.size = size

    def describe_body(self):
        print("The dog's color is " + self.color + ', and size is ' + str(self.size) + '.')

    # 访问属性
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + '.')
print("My " + my_dog.sex + " dog's age is " + str(my_dog.age) + ' years old.')
# 调用方法
my_dog.sit()
my_dog.roll_over()
# 直接修改属性的值
my_dog.sex = 'female'
print(my_dog.sex.title())
# 通过方法修改属性的值
'''
在定义类中添加一个方法update_sex()，如上。
然后通过调用update_sex来更改属性值
'''
my_dog.update_sex('U Guess?')
print(my_dog.sex)


# 继承
class CuteDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        '''
        super()为一特殊函数，将父类和子类关联起来，让Python调用父类的方法_init_，让子类实例包含父类所有属性。父类也称为superclass
        注意此处init左右的下划线数目各为2，与前一行不同
        '''
        self.body = Body('yellow')  # 新加入一个用小类Body定义的属性

    def sit(self):
        print(self.name.title() + ' is NOT sitting.')  # 当发现子类里的某一方法与父类的方法不符时，可以在子类里重写该方法，覆盖父类的方法


my_cutedog = CuteDog('jack', 9)
print(my_cutedog.name.title() + "'s age is " + str(my_cutedog.age))
my_cutedog.roll_over()  # 子类也继承了父类定义的所有方法
my_cutedog.sit()  # 检验重写父类的方法

# 将实例作为属性（即将大型类拆分为多个小类），前面已经定义了一个小类Body
print('Body_Info: ' + my_cutedog.body.color.title() + ' ' + str(my_cutedog.body.size))
my_cutedog.body.describe_body()  # 检验新加入的属性body


# 笔记
'''
1：Python中，首字母大写的名称指的是类(class)，小写的名称代表根据类创建的实例
2：init左右有两个下划线！！！
3：不同方法定义即def之间最好隔一行
'''