def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)

def ncr(n,r):
    nCr = fact(n) / (fact(r) * fact(n-r))
    return nCr
n=8
r=3
print(ncr(n,r))