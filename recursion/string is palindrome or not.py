'''def pal(str, s, e):
    if(str[s] != str[e]):
        return False
    
    if s == e:
        return True
    
    if s > e:
        return True

    return pal(str, s+1, e-1)
str = 'ababa'
s=0
n = len(str)
e=n-1
print(pal(str,s,e))
'''

def pal(str, s, e):
    if(s==e):
        return True
    if(s>e):
        return True
    if(str[s]!=str[e]):
        return False
    
    return pal(str, s+1, e-1)
str='abcba'
n = len(str)
s=0
e=n-1
print(pal(str,s,e))
s='1q1q'
if s == s[::-1]:
    print(True)
else:
    print(False)