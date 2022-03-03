def merge(arr1,arr2,c):
    #c = arr1 + arr2
    print(c)
    c.sort()
    return c

def merge1(arr1,arr2):
    i,j=0,0
    m=len(arr1)
    n=len(arr2)
    while(i<m and j<n):
        if(arr1[i]<arr2[j]):
            print(arr1[i])
            i+=1
        else:
            print(arr2[j])
            j+=1
      
    while(i<m):
        print(arr1[i])
        i+=1
    while(j<n):
        print(arr2[j])
        j+=1

arr1=[2,4,6,8,9]
arr2=[3,4,5,6]
c=arr1+arr2
merge1(arr1,arr2)
print(merge(arr1,arr2,c))