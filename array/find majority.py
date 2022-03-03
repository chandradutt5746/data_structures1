def majority(arr,n):
    maxcount=0
    index= -1
    for i in range(n):
        count=0
        for j in range(n):
            if(arr[i]==arr[j]):
                count+=1
        if(count>maxcount):
            maxcount=count
            index=i
    if(maxcount>n//2):
        return arr[index]
    else:
        return "no majority found"

arr = [1, 1, 2, 1, 3, 5, 1]
n = len(arr)
print(majority(arr,n))



'''
def majorityElement(self, A, N):
        #Your code here
        m = {}
        for i in range(N):
            if A[i] in m:
                m[A[i]] += 1
            else:
                m[A[i]] = 1
        count = 0
        for key in m:
            if m[key] > N / 2:
                count = 1
                return key
                break
        if(count == 0):
            return -1



maj_index = 0
        count = 1
        for i in range(len(A)):
            if A[maj_index] == A[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return A[maj_index]
        
    # Function to check if the candidate occurs more than n/2 times
    def isMajority(self, A, cand):
        count = 0
        for i in range(len(A)):
            if A[i] == cand:
                count += 1
        if count > len(A)/2:
            return True
        else:
            return False
    
    def majorityElement(self, A,N):
        cand = self.findCandidate(A)
    
        # Print the candidate if it is Majority
        if self.isMajority(A, cand) == True:
            return cand
        else:
            return -1


'''