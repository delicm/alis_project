import numpy as np
import random
from matplotlib import pyplot as plt

#######################################################

def LIS(seq):
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
    
    n = len(seq)
    if n == 0: return 0
    
    P = [1e15 for _ in range(n+5)]; P[0] = -1
    for element in seq:
        loc = bsearch(P, element)
        P[loc+1] = element
    
    return bsearch(P, 1e15 - 1)

#######################################################

'''sequence generation'''

def getSequence_n_over_2(n, range_):
    def genIncreasing(n, range_):
        return np.sort(random.sample([i+1 for i in range(range_)], n))
    
    def insertRandom(seq, range_):
        n = len(seq)
        noise = [random.randint(1, range_) for _ in range(n)]

        sol = []
        cnti, cntn = 0, 0
        while cnti+cntn < 2*n:
            if cnti == n:
                sol.append(noise[cntn])
                cntn += 1
                continue
            if cntn == n:
                sol.append(seq[cnti])
                cnti += 1
                continue
            
            choice = random.randint(0, 1)
            if choice == 1:
                sol.append(noise[cntn])
                cntn += 1
            else:
                sol.append(seq[cnti])
                cnti += 1
                
        return sol
    
    increasing_part = genIncreasing(n, range_)
    return insertRandom(increasing_part, range_)

def getSequence_root(n, X, Y):
    lst = [0 for _ in range(n*n)]
    for i in range(n): lst[i] = float(2*n+i)
    
    for box in range(1, n):
        for ind in range(n):
            if X[ind] == 1 and Y[ind] == 1: lst[box*n+ind] = (2**box)*lst[ind]
            else: lst[box*n+ind] = (2**(-box))*lst[ind]
            
    return lst

#######################################################


n = 7
X = [0, 1, 0, 1, 0, 0, 1]
Y = [1, 0, 0, 1, 0, 1, 0]

sample = getSequence_root(n, X, Y)
L = LIS(sample)
plt.title(f'LIS = {L} = {L/n :.2f}n')
plt.scatter([i for i in range(n*n)],sample)
plt.show()
