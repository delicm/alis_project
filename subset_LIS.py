import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import bernoulli

#############################################################################################################################################################

'''HELPER FUNCTIONS'''

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
def deterministic(seq):
    n = len(seq)
    if n == 0: return 0
    
    P = [1e15 for _ in range(n+5)]; P[0] = -1
    for element in seq:
        loc = bsearch(P, element)
        P[loc+1] = element
    
    return bsearch(P, 1e15 - 1)

# takes in seq, retains every element w/ probability p
def sample(seq, p):
    subseq = []
    for element in seq:
        choose = bernoulli(p).rvs(1)
        if choose: subseq.append(element)
    
    return subseq

#############################################################################################################################################################

'''EXECUTION & SAMPLING'''

# compares LIS to subseq
def trial(seq, p):
    subseq = sample(seq, p)
    return deterministic(subseq) / deterministic(seq)

# randomize trial
def randomized_trial(len_, p):
    return trial(np.random.permutation(len_), p)

#############################################################################################################################################################

'''DIRECT INTERACTION'''

# write samples to a file, p = 0.8
def write_to_file(iters= 100):
    file = open('point_eight.txt', 'a')
    for _ in range(iters):
        file.write(f'{randomized_trial(100, 0.8)}\n')
    file.close

# move file to list - point_eight.txt
def read_from_file():
    file = open('point_eight.txt')
    lst = []
    for line in file.readlines():
        lst.append(float(line))
    return lst

def plot_file():
    data = read_from_file()
    
    print(f'mean: {np.mean(data)}')
    print(f'stdev: {np.std(data)}')
    print(f'n = {len(data)}')
    
    plt.hist(data, 30)
    plt.show()

def direct_plot(size, p, iters):
    lst = []
    for _ in range(iters): lst.append(randomized_trial(size, p))
    
    print(f'Mean: {np.mean(lst)} \nStDev: {np.std(lst)} \nP[X>p] = {np.count_nonzero(np.array(lst) > p) / iters}')
    
    plt.hist(lst, 30)
    plt.show()

def test_seq():
    try:
        lst = []
        while True:
            lst.append(int(input()))
    except:
        print(lst)
        print(deterministic(lst))

#############################################################################################################################################################

'''MAIN'''

test_seq()