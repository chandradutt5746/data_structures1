def leftrotateone(arr, n, d):
    for i in range(d):
        leftrotate(arr, n)
    return arr


def leftrotate(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
d = 3
print(leftrotateone(arr, n, d))
