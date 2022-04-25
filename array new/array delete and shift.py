def find_delete(arr, n, x):
    if n == 0:
        return 'delete not possible'

    for i in range(n):
        if x == i:
            del(arr[i])
            # for j in range(i, n-1):
            #     arr[i] = arr[i]
            #     print(arr)
    return arr


arr= [3, 1, 2, 5, 90]
x = 2
n = len(arr)
print(find_delete(arr, n, x))