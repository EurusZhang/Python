# while循环：直到指定的条件不满足为止

    # Example 1
# count_number = 1
# while count_number <= 5:
#     print(count_number)
#     count_number += 1
# print('...')

    # Example 2
# message = ' '
# while message != 'quit':
#     message = input('Do you wanna quit?\n')
#     if message != 'quit':
#         print(message)
# print('...')

    # Example 3
# active = True  # 使用标志
# while active:
#     message = input('Do you wanna quit?\n')
#     if message == 'yes':
#         active = False
#     else:
#         print(message)
# print('...')

    # break  # 退出while循环
# while True:
#     message = input('Do you wanna quit?\n')
#     if message == 'yes':
#         break
#     else:
#         print(message)
# print('...')

    # continue  # 跳出当前循环
# current_number = -1
# while current_number < 100:
#     current_number += 1
#     if current_number % 2 != 0:
#         continue
#     else:
#         print(current_number)

    # 在列表之间移动元素
print('在列表之间移动元素')
unconfirmed_users = ['aaa', 'bbb', 'ccc']
confirmed_users = []
while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()
    print('Verifying user: ' + confirmed_user.title())
    confirmed_users.append(confirmed_user)
print('Here are the all confirmed users:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

    # 删除包含特定值的所有列表元素
print('删除包含特定值的所有列表元素')
list = ['a', 'b', 'c', 'a', 'd', 'a', 'e']
while 'a' in list:
    list.remove('a')
print(list)

    # 使用用户输入来填充字典
print('使用用户输入来填充字典')
responses = {}
while True:
    name = input("What's your name? ")
    response = input("What's your favorite programming language? ")
    responses[name] = response
    repeat = input("Do you wanna to ask someone else? ")
    if repeat == 'yes':
        continue
    else:
        break
print('---The all responses are---')
for name, response in responses.items():
    print(name + "'s favorite language is " + response)