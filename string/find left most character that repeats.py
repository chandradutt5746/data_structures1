from turtle import st


string = 'patel chandradutt'
def fs(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if(string[i] == string[j]):
                return i
    return -1

print(fs(string))