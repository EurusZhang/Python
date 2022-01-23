# 在列表中嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:  # 遍历列表中所有字典
    print(alien)
print('\t...\n')

aliens = []
for alien_number in range(30):  # 确定个数为30，即确定循环次数
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)  # 每次执行这个循环时，都创建一个键值对，并添加进字典末尾
for alien in aliens[:5]:
    print(alien)
print('Total number of aliens: ' + str(len(aliens)))
print('...')

for alien in aliens[:3]:  # 修改列表中前三个字典的键值对
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
print('...')

# 在字典中嵌套列表
favorite_languages = {
    'Michael': ['C', 'Python'],
    'Jack': ['Ruby', 'Matlab', 'Java'],
    'Lisa': ['C++'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print('\n' + name + "'s favorite language is:")
    else:
        print('\n' + name + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())
print('...')

# 在字典中嵌套字典
# 创建方式1：
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'aeinstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     }
# }
# 创建方式2：
users = dict(aeinstein=dict(first='albert', last='aeinstein', location='princeton'),
             mcurie=dict(first='marie', last='curie', location='paris'))

for username, user_info in users.items():
    print("\nUsername: " + username.title())
    fullname = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull Name: ' + fullname.title())
    print('\tLocation: ' + location.title())
print('...')