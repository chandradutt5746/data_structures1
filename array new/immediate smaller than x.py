def immediate_smaller_x(arr, n, x):
    arr.sort()
    for i in range(n):
        print(arr[i])
        if arr[i] == x:
            print(arr[i])
            return arr[i - 1]


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
x = 6
print(immediate_smaller_x(arr, n, x))
