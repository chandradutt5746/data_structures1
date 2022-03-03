out=0
In=1
state=out
wc=0
string = 'a\nhjpfo'
string.split('\\n')
string.split('\\t')
print(string)
for i in range(len(string)):
    
    if(string[i] == ' ' or string[i] == '\\t' or string[i] =='\\n' or string[i] == '\\r'):
        state=out
    elif(state == out):
        state = In
        wc += 1
print(wc)
print(string)