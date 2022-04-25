def small(arr, n, x):
    arr.sort()
    smaller = -1
    for i in range(n):
        if(0<x-i<x-smaller):
            smaller=i
    return smaller

arr = [4,3,6,9,7,3,2]
n = len(arr)
x = 10
print(small(arr,n,x))

''' arr.sort()
    print(arr)
    for i in range(n):
        if(i==0 and arr[i]==x):
            return -1
        if(arr[i]<x and arr[i]>= x):
            return arr[i]
    return -1
'''