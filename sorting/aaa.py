from collections import defaultdict


def c(arr,n):
    '''ht = defaultdict(lambda:0)
    for i in range(n):
        ht[arr[i]] += 1
    
    return ht'''
    dict1={arr[i] : arr[i+1] for i in range(0,len(arr)-1,2)}
    print('this is dictonary: ',dict1)
    it = iter(arr)
    dict1 = dict(zip(it,it))
    
    return dict1

lst = [1, 2, -1, '3', 2]
n = len(lst)
print(c(lst,n))