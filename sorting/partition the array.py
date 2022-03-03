'''def lomuto(arr,l,h):
    pivot = arr[h-1]
    i = l-1
    j=l
    for j in range(h-1):
        if(arr[j]<pivot):
            l += 1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

arr=[2,4,78,2,1,6]
n = len(arr)
l = arr[0]
h = arr[n-1]
print(lomuto(arr,l,h))'''


from typing import Counter


def con(lst):
    it = iter(lst)
    dic = dict(zip(it,it))
    print(dic)

    res = {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
    print(res)

lst=[1,32,2,34,5,56,6,3]
con(lst)

def monotonic(arr,n):
    for i in range(n):
        if(arr[i]>0):
            print(arr[i])
arr = [5,4,3,2,1,9,-3,-2,5,-1]
n=len(arr)
print(monotonic(arr,n))