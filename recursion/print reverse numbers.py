def reverse(n):
    if(n == 0):
        return
    print(n)
    reverse(n-1)

reverse(5)

def num(n):
    if(n < 1):
        return
    num(n-1)
    print(n)
num(5)

def aa(n,k=1):
    if(n<1):
        return
    print(k)
    aa(n-1,k+1)
aa(5)
