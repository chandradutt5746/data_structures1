def reverse(arr, n):
    low = 0
    high = n-1
    while(low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    print(arr)

arr=[1,2,3,4,5]
n = len(arr)
reverse(arr,n)