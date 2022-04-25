from collections import Counter


def majority(arr, n):
    print(Counter(arr))
    for i in list(Counter(arr)):
        for j in i:
            print(j)


arr = [1, 2, 3, 4, 1, 2, 3, 1, 2, 11, 2, 3, 3, 2, 1, 4]
n = len(arr)
print(majority(arr, n))
