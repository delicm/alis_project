import numpy as np
from matplotlib import pyplot as plt

def LIS(arr):
    n = len(arr)
 
    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1]*n
 
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
 
    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0
 
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])
 
    return maximum

def standard(n, X, Y):
    lst = [0 for _ in range(2*n)]
    for i in range(n): lst[i] = 4*i+4-2*X[i]
    for i in range(n): lst[n+i] = 4*i+1+2*Y[i]
    return lst

def std_k_l(n, X, Y, k=1, l=1):
    M = 2*max(k, l)
    preliminary = standard(n, X, Y)
    for i in range(2*n): preliminary[i] *= M
    
    lst = [0 for i in range(n*k+n*l)]
    for box in range(n):
        for ind in range(k): 
            lst[k*box+ind] = ind+preliminary[box]
    for box in range(n):
        for ind in range(l): 
            lst[n*k+l*box+ind] = ind+preliminary[n+box]
    
    return lst

def level_arg(t, k, X, Y):
    N = 2*t*k
    lst  = [i for i in range(N)]
    level = [0 for i in range(2*t)]
    
    for group in range(t):
        if X[group] == 0: level[2*group+1] = N**2 - group
        else: level[2*group+1] = group
        
    for group in range(t):
        if Y[group] == 0: level[2*group] = -N**2 + group
        else: level[2*group] = group
        
    for ind in range(N):
        group = ind%(2*t)
        lst[ind] = ind+level[group]*k

    for ind in range(len(lst)): lst[ind] += N**2*k
    
    return lst

t = 3
k = 2
X = [1, 0, 1]
Y = [0, 1, 1]

plt.scatter([i for i in range(2*t*k)], level_arg(t, k, X, Y), c = [i%(2*t) for i in range(2*t*k)], s=10)
plt.title(f't = {t}, k = {k}, LIS = {LIS(level_arg(t, k, X, Y))}')
plt.show()

# plt.scatter([i for i in range(2*n*k)], std_k_l(n, X, Y, k, l))
# plt.show()