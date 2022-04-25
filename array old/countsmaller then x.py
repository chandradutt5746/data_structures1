def count1(arr,n,x):
    count = 0
    for i in range(n):
        if(arr[i]<x):
            count+=1
    return count

def greater(arr,n,x):
    count=0
    for i in range(n):
        if(arr[i]>x):
            count += 1
    return count
arr=[1,6,0,3,8,-0,12,56,98,34,23]
n = len(arr)
x = 54
print(count1(arr,n,x))
print("greater than x:- ",greater(arr,n,x))