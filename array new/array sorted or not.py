def array_sorted(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    return True


arr = [1, 2, 3, 9, 4, 5, 6]
print(array_sorted(arr))
