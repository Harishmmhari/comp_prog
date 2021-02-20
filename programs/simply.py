import numpy as np
def convertToWave( A, N):
    # Your code here
    n = N
    a = np.sort(A)
    i = 0
    while ((i < n) & ((i + 1) < n)):
        print("i",i)
        temp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = temp
        # a[i],a[i+1]=a[i+1],a[i]
        i = i + 2
    A = a
    print(a,A)
    return (a)

convertToWave([6907,7808,8551,8683,9205,9980],6)