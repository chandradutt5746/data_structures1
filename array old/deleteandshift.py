def delete(arr, n, x):
    for i in range(n):
        if (arr[i] == x):
            break

    if (i < n):
        n = n - 1
        for j in range(i, n, 1):
            arr[j] = arr[j + 1]
        del arr[j]
    return arr


arr = [4, 5, 7, 3, 8, 9]
n = len(arr)
x = 7
print(delete(arr, n, x))
