def movezero(arr, n):
    count = 0
    for i in range(n):
        if (arr[i] != 0):
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr


def movezero1(arr, n):
    arr1 = []
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr1.append(arr[i])
        elif arr[i] == 0:
            count += 1
        else:
            pass

    while count:
        arr1.append(0)
        count -= 1

    return arr1


arr = [10, 5, 0, 0, 8, 9, 0]
n = len(arr)
print(movezero(arr, n))
print(movezero1(arr, n))
