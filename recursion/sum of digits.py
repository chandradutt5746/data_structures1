'''def sum(n):
    if(n<10):
        return n
    
    return sum(n/10)+n%10
n=235
print(int(sum(n)))'''

def ss(n):
    if(n<10):
        return n
    return ss(n/10) + n % 10

n = 654456
print(int(ss(n)))