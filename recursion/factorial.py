def pos(arr,n):
    pos=[]
    neg=[]
    for i in range(n):
        if(arr[i]>=0):
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    i,j,k=0,0,0
    while(i < len(neg) and j < len(pos)):
        arr[k]=pos[j]
        j += 1
        k += 1
        arr[k]=neg[i]
        i+=1
        k+=1

    while(i < len(neg)):
        arr[k]=neg[i]
        k += 1
        i += 1

    while(j < len(pos)):
        arr[k]=pos[j]
        j+=1
        k+=1
    return arr

arr=[9, 4, -2, -1, 5, 0, -5, -3, 2]
n = len(arr)
print(pos(arr,n))