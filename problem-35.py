
from itertools import combinations 
def is_prime(n: int)->bool: 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i  == 0: 
            return False 
    return True 

assert is_prime(197) 
assert is_prime(971) 
assert is_prime(719) 
 
def rotate_digits(n: int)->list[int]:
    n_str = str(n)
    rotations = set()
    for i in range(len(n_str)):
        # move the first i characters to the end  
        rotations.add(int(str(n)[i:] + str(n)[:i]))
    return list(rotations) 
    
assert rotate_digits(197) ==  [971, 197, 719] 

circular = set() 
for i in range(2, 1_000_000): 
    if is_prime(i):
        rotations = rotate_digits(i) 
        if all(is_prime(rot) for rot in rotations): 
            circular.update(rotations) 


print(len(circular))


