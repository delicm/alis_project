import math

def summary_set(seq, pairs=False):
    n = len(seq)
    if n == 0: return [-math.inf]
    
    prev = summary_set(seq[0:-1])
    last = seq[-1]
    new = [-math.inf]
    for ind in range(1, len(prev)):
        if last < prev[ind] and last > prev[ind-1]: new.append(last)
        else: new.append(prev[ind])
    if last > prev[-1]: new.append(last)
    
    if pairs == False: return new
    
    neww = []
    for ind in range(1, len(new)):
        neww.append([ind, new[ind]])
    return neww    

print(summary_set([3, 2, 7, 5], pairs=True))