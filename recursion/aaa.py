def pal(str,s,e):
    if(str[s] != str[e]):
        return False
    if(s==e):
        return True
    if(s>e):
        return True
    return pal(str,s+1,e-1)
str='absba'
n = len(str)
s=0
e=n-1
print(pal(str,s,e))