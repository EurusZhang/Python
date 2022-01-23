# input(), Python 2.7中的命令是raw_input()
# prompt = 'Nice to meet you! '
# prompt += 'Tell me something: '  # +=表示在字符串后面添加字符串
# message = input(prompt)  # Hello Everyone! I'm Eurus.
# print(message)
# print('...')

# 使用input()时，python将用户输入解读为字符串，int()用来将字符串表示转换为数值表示
Number = input('Which number do you want to judge?\n')
Number = int(Number)
if Number % 2 == 0:  # %表示求模运算，它将两个数相除并返回余数
    print('Even')
else:
    print('Odd')