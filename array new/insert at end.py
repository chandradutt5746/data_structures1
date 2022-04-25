def insert_end(arr, k):
    n = len(arr)
    arr.insert(n, k)
    # print(arr)
    k = 9
    for i in range(n):
        pass
    arr.insert(n, k)
    print(arr)

arr = [1, 2, 3, 4, 5]
k = 6
print(insert_end(arr, k))
