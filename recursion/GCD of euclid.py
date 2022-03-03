import statistics
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b, a%b)

a=60
b=48
print(GCD(a,b))