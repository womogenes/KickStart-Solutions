import copy

def solve(s, a, b, c):
    """
    a and b are tuples.
    c is a set of tuples.
    """
    def score(a, b, _taken, turn, prevFailed=False):
        """
        taken is a set of unusable rooms.
        It includes both rooms under construction and already-painted rooms.
        turn is 0 for Alma and 1 for Berthe.
        """
        #print(a, b, _taken, turn)
        taken = set(_taken)
        possible = [] # Possible next moves.
        
        if turn == 0:
            x = a
        else:
            x = b
        
        if x[1] > 1:
            new = (x[0], x[1] - 1)
            if new not in taken:
                possible.append(new)
                
        if x[1] < x[0] * 2 - 1:
            new = (x[0], x[1] + 1)
            if new not in taken:
                possible.append(new)
            
        if x[1] % 2 == 0:
            if x[0] > 1:
                new = (x[0] - 1, x[1] - 1)
                if new not in taken:
                    possible.append(new)
        else:
            if x[0] < s:
                new = (x[0] + 1, x[1] + 1)
                #print("bOOOOOOOOOm", new in taken)
                if new not in taken:
                    possible.append(new)
                    
        #print("    possible:", possible)
        
        p = len(possible)
        if p == 0:
            if prevFailed:
                return 0
            return score(a, b, tuple(taken), 1 - turn, True)
            
        if turn == 0:
            scores = []
            for i in range(p):
                ac = possible[i]
                taken.add(ac)
                scores.append(score(ac, b, tuple(taken), 1 - turn))
                taken.remove(ac)
            return max(scores) + 1
            
        else:
            scores = []
            for i in range(p):
                bc = possible[i]
                taken.add(bc)
                scores.append(score(a, bc, tuple(taken), 1 - turn))
                taken.remove(bc)
            return min(scores) - 1
            
    taken = [a, b]
    taken.extend(list(c))
    ans = score(a, b, tuple(taken), 0)
    
    return ans
    
    
caseCount = int(input())
for i in range(caseCount):
    s, ra, pa, rb, pb, cn = [int(i) for i in input().split(" ")]
    a = (ra, pa)
    b = (rb, pb)
    c = set()
    for j in range(cn):
        c.add(tuple([int(i) for i in input().split(" ")]))
        
    ans = solve(s, a, b, c)
    print("Case #" + str(i + 1) + ": " + str(ans))