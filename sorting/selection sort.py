def selection(arr,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if(arr[j]<arr[min]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]

arr=[6,3,8,9,4,2]
n=len(arr)
selection(arr,n)
for i in range(n):
    print(arr[i])