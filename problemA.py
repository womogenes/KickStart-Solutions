import sys
import math

def solve(n, x, a):
    times = []
    for i in range(n):
        times.append((math.ceil(a[i] / x), i))
        
    times.sort()
    return [x[1] for x in times]
    

caseCount = int(next(sys.stdin))

for i in range(caseCount):
    n, x = [int(i) for i in next(sys.stdin)[:-1].split(" ")]
    a = [int(i) for i in next(sys.stdin)[:-1].split(" ")]
    
    ans = solve(n, x, a)
    print("Case #" + str(i + 1) + ":", " ".join([str(i + 1) for i in ans]))