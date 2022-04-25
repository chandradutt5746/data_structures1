def update_index(arr, ind):

    for i in range(ind):
        if ind == i:
            arr[i] = 100
    print(arr)


arr = [1, 32, 5, 3, 4, 76]
ind = 2
update_index(arr, ind)