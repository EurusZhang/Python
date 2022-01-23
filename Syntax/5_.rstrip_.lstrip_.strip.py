favorite_language = 'Python '
print(favorite_language)
print(favorite_language.rstrip())
'''
In "Terminal" interface, you can see the space behind the "Python"
'''
favorite_language = 'Python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# The following programs shall be ran in the "Terminal" interface
favorite_language = ' Python '
favorite_language.rstrip()  # 删除右边空白
favorite_language.lstrip()  # 删除左边空白
favorite_language.strip()  # 删除两端空白