n = int(input())
order = 1
factorialsum = 0
i = 1
while n >= i:
    order = order * i
    factorialsum = factorialsum + order
    i = i + 2
print(factorialsum)
