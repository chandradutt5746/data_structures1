from collections import Counter


str1='hello'
str2='olleh'

str1=sorted(str1)
str2=sorted(str2)
print(str1)
print(str2)
if(str1 == str2):
    print('anagram')
else:
    print('not anagram')
if(Counter(str1) == Counter(str2)):
    print('string is anagram')
else:
    print('not anagram')