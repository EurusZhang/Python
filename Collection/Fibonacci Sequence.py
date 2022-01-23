def Fibonacci(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    else:
        i = 3
        while i <= n:
            a, b = b, a + b
            i += 1
        return b


print(Fibonacci(int(input('输入一个数: '))))
