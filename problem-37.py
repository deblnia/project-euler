

def is_prime(n:int)->bool: 
    if n <= 1: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i  == 0: 
            return False 
    return True 

if is_prime(7): 
    print("Pass") 

if not is_prime(8):
    print("Pass")

def is_truncatable_prime(n:int)->bool:
    if n < 10: 
        return False 
    ns = str(n) 
    for i in range(len(ns)):
        # checking right 
        if not is_prime(int(ns[i:])): 
            return False
    for i in range(1, len(ns)): 
        # checking left 
        if not is_prime(int(ns[:i])): 
            return False 
    return True 

if is_truncatable_prime(3797): 
    print("Pass") 
if not is_truncatable_prime(3799):
    print("Pass") 

ts = [] 
n = 10 
while len(ts) < 11: 
    if is_truncatable_prime(n): 
        ts.append(n) 
    n += 1 

print(sum(ts))
