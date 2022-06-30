def bubble(arr, n):
    for i in range(n - 1):
        for j in range(n - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                '''temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp'''
    return arr


arr = [4, 7, 2, 4, 1]
n = len(arr)

print(bubble(arr, n))
