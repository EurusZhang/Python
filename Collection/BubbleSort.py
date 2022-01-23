def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
example = [3, 4, 1, 5, 9, 6, 8, 2, 7]
BubbleSort(example)
for x in range(len(example)):
    print(example[x])