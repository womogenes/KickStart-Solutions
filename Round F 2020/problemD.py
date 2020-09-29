#import itertools
from functools import lru_cache

def matches(x, y):
    x = list(x)
    y = list(y)
    x.sort()
    y.sort()
    index = -1
    for i in range(len(x)):
        if x[i] == 0:
            continue
        if index == -1:
            index = i
        
        if x[i] != y[i - index]:
            return False
            
    return True
    

def solve(n, m, a):
    k = len(a)
    
    @lru_cache(None)
    def rolls(dist):
        if sum(dist) == n:
            if matches(dist, a):
                return 0
            return -1
        
        possible = []
        for i in range(m):
            x = list(dist)
            x[i] += 1
            y = rolls(tuple(x))
            if y != -1:
                possible.append(y)
        possible.sort()
        
        if len(possible) == 0:
            return -1
        
        best = 1
        for i in range(1, len(possible) + 1):
            if m / i + sum(possible[:i]) / i < m / best + sum(possible[:i]) / best:
                best = i
                
        return m / best + sum(possible[:best]) / best
        
    return rolls(tuple([0] * m))
    
    
caseCount = int(input())
for i in range(caseCount):
    n, m, k = [int(i) for i in input().split(" ")]
    a = []
    for j in range(k):
        a.append(int(input()))
        
    ans = solve(n, m, a)
    print("Case #" + str(i + 1) + ": " + str(ans))