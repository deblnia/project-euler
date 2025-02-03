
import math 

def pentagonal(x:int)->int: 
    """Generates the nth pentagonal number""" 
    return x * (3 * x - 1) // 2 

def is_pentagonal(x:int)->bool: 
    n = (1 + math.isqrt(24 * x + 1)) / 6
    return n == int(n) 

# arbitrary threshold to start 
pn = [pentagonal(i) for i in range(1, 3000)] 
pns = set(pn) 

found = False 
for j in range(1, len(pn)): 
    for k in range(j - 1, -1, -1): 
        pj, pk = pn[j], pn[k] 

        if (pj - pk) in pns and (pj + pk) in pns: 
            print(abs(pk - pj)) 
            found = True 
            break
    if found: 
        break 
     

