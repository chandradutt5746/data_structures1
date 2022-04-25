def smaller_x(arr, n, x):
    count = 0
    count1 = 0
    for i in range(n):
        if arr[i] <= x:
            count += 1
        elif(arr[i] > x):
            count1 += 1
    print('as', count1)
    return count


arr = [12,332,65,67,23,1,5,7,9,45,23]
n = len(arr)
x = 60
print(smaller_x(arr, n, x))