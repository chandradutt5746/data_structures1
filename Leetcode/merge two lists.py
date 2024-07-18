def merge(arr1, arr2, m, n):
    p1, p2, p = m-1, n-1, m+n-1
    
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] > arr2[p2]:
            arr1[p] = arr1[p1]
            p1 -= 1
        else:
            arr1[p] = arr2[p2]
            p2 -= 1
        p -= 1
    
    arr1[:p2+1] = arr2[:p2+1]
    return arr1
    
arr1 = [1, 2,3,0,0,0]
arr2 = [2, 5, 6]
m = 3
n = 3
print(merge(arr1, arr2, m, n))
