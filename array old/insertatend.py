def insertatend(arr,key):
    arr.append(key)
    return arr

def insertatindex(arr,x):
    #arr = [len(arr)+1]
    index = int(input("enter index value:- "))
    
    arr.insert(index,x)
    #return arr1

    return arr
arr = [1,2,3,4,5]
key = 20
x=50
print(insertatend(arr, key))
print(insertatindex(arr,x))