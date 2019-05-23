def maxsubprod(A):
    max = A[0]
    prod = A[0]
    n=len(A)
    for i in range(1,n):
        prod = prod*A[i]
        if(prod>=max):
            max=prod
        if(max<=A[i]):
            prod=A[i]
            max=A[i]
    return max


A = [1,2,0.5,3,2]
B = [1,2,0.5,1,1]
C = [1,2,0.5,2,3]
D = [0.5,1,1]
E = [3,0.5,0,1,4]
F = [4,100,0.1,1000] 
G = [4,1000,0.1,0.1,10] 


print str(maxsubprod(A))