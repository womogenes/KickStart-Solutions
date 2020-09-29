# Problem B: Metal Harvesting

import math

def solve(n, k, times):
    times.sort()
    deploys = 0
    lastAvailable = 0
    for s, e in times:
        #print("s, e, deploys", s, e, deploys)
        
        if lastAvailable >= e:
            continue
        
        if lastAvailable > s:
            startTime = lastAvailable
        else:
            startTime = s
            
        newDeploys = math.ceil((e - startTime) / k)
        lastAvailable = startTime + newDeploys * k
        deploys += newDeploys
        
        #print("deploys", deploys, lastAvailable)
        
    return deploys
    

caseCount = int(input())
for i in range(caseCount):
    n, k = [int(i) for i in input().split(" ")]
    times = []
    for j in range(n):
        times.append([int(i) for i in input().split(" ")])
        
    ans = solve(n, k, times)
    print("Case #" + str(i + 1) + ": " + str(ans))