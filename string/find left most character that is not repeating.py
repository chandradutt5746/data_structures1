from collections import Counter


string='geeksforgeeks'

def nr(string):
    c = Counter(string)
    print(c)
    for i in string:
        if(c[i]==1):
            print(i)
            break
        
    

print(nr(string))