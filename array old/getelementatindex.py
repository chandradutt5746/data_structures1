def getelement(arr,n):
    pos = 3
    for i in range(n):
        if(arr[i]==pos):
            return arr[i+1]
arr = [2,3,5,6]
n = len(arr)
print(getelement(arr,n))