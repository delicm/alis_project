import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import bernoulli

# returns biggest index i with seq[i] <= target
def bsearch(seq, target): 
    n = len(seq)
    if n == 0: return None
    
    a, b = 0, n-1
    while a < b:
        c = (a+b)//2
        if seq[c] <= target and (c == n-1 or seq[c+1] > target):
            return c
        if seq[c] > target:
            b = c
            continue
        a = c
        continue
    
    return None
            
# returns length of LIS of seq
def LIS(seq):
    n = len(seq)
    if n == 0: return 0
    
    P = [1e15 for _ in range(n+5)]; P[0] = -1
    for element in seq:
        loc = bsearch(P, element)
        P[loc+1] = element
    
    return bsearch(P, 1e15 - 1)

def genPerms(n, iters):
    lst = []
    const = [i+1 for i in range(n)]
    for _ in range(iters): lst.append(LIS(np.random.permutation(const)))
    minl = np.min(lst)
    maxl = np.max(lst)
    
    print(f'Mean: {np.mean(lst)}')
    print(f'StDev: {np.std(lst)}')
    print(f'Range: {minl} - {maxl}')
    plt.hist(lst, bins=[i for i in range(n+1)])
    plt.show()

def visualizePerm(n):
    lst = np.random.permutation([i for i in range(n)])
    plt.scatter([i for i in range(n)], lst)
    plt.show()

visualizePerm(1000)
