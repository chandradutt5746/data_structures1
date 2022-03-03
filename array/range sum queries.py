#merge two sorted arrays
def mergetwoarrays(arr1,arr2,n1,n2):
    arr3 = [None] * (n1 + n2)
    i,j,k = 0,0,0
    while(i<n1 and j<n2):
        if(arr1[i]<arr2[j]):
            arr3[k]=arr1[i]
            i += 1
            k += 1
        else:
            arr3[k]=arr2[j]
            j += 1
            k += 1

    while(i<n1):
        arr3[k]=arr1[i]
        k+=1
        i+=1
    
    while(j<n2):
        arr3[k]=arr2[j]
        k+=1
        j+=1

    print("arr1:- \n", arr1)
    print("arr2:- \n", arr2)


    print("print array:- \n")
    print(arr3)

arr1 = [1,4,6,3,4,3]
arr2 = [0,9,6,4,9,8,7,1]
n1 = len(arr1)
n2 = len(arr2)
mergetwoarrays(arr1,arr2,n1,n2)


def deletearray(arr, n, k):
    for i in range(n):
        if(arr[i] == k):
            break
    if i == n:
        return n

    for j in range(n-1):
        arr[j-1]=arr[j]
    print(arr)
    return len(arr)

def largestelement(arr):
    res = 0
    for i in range(len(arr)):
        if(arr[i]>=arr[res]):
            res = i
    return i

arr = [1,2,3,4,5,8,7]
k = 3
n = len(arr)
print(" largest element" ,largestelement(arr))
print("delete element", deletearray(arr, n, k))




def secondlargest(arr,n):
    res = -1
    largest = 0
    for i in range(n):
        if(arr[i]>arr[largest]):
            res = largest
            largest = i
        elif(arr[i] != arr[largest]):
            if(res == -1 or arr[i] > arr[res]):
                res = arr[i]
    return res

arr = [5,20,12,10,8]
n = len(arr)
print("second largest", secondlargest(arr, n))