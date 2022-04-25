def movezero(arr, n):
    count=0
    for i in range(n):
        if(arr[i] != 0):
            arr[i],arr[count]=arr[count],arr[i]
            count+=1
    return arr

arr = [10,5,0,0,8,9,0]
n = len(arr)
print(movezero(arr, n))