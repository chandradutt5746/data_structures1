import statistics


def sorted(arr, n):

    if(n == 0 or n == 1):
        return True
    
    for i in range(1, n):
        if(arr[i-1] > arr[i]):
            return False
    return True

def meanandmedian(arr):
    m = statistics.mean(arr)
    m1 = statistics.median(arr)
    print(m, "median:- \n", m1)

arr = [1, 2, 3, 4, 5]

n = len(arr)

print(sorted(arr, n))

meanandmedian(arr)
