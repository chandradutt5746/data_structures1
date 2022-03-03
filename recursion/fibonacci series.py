def fibo(n):
    if(n<=1):
        return n
    else:   
        return (fibo(n-1) + fibo(n-2))

n = 10
for n in range(n):
    print(fibo(n))
