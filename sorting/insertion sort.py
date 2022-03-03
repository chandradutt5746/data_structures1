def insertion(arr,n):
    for i in range(n):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1] = key

arr=[2,6,9,4,2,6,5]
n = len(arr)
insertion(arr,n)
for i in range(n):
    print(arr[i])