def maxcut(n,a,b,c):
    if n == 0:
        return 0
    if n < 0:
        return -1

    res = max(maxcut(n-a,a,b,c),maxcut(n-b,a,b,c),maxcut(n-c,a,b,c))
    if res == -1:
        return -1
    
    return res+1
    
n=23
a=11
b=9
c=12
print(maxcut(n,a,b,c))



def maxcuts1(n,a,b,c):
    if(n==0):
        return 0
    if(n < 0):
        return -1
    res = max(maxcuts1(n-a,a,b,c),maxcuts1(n-b,a,b,c),maxcuts1(n-c,a,b,c))
    if(res == -1):
        return -1
    return res+1

n=5
a=2
b=1
c=5
print(maxcuts1(n,a,b,c))