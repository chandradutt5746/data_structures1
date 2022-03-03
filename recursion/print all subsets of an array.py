def subset(str, curr="", index=0):
    n = len(str)
    if(index==n):
        return curr

    subset(str, curr, index+1)
    subset(str, curr+str[index], index+1)

str='abc'
print(subset(str))