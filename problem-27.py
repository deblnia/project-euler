
def is_prime(n: int)->bool: 
    if n <= 1: 
        return False 
    for i in range(2, ((n // 2) + 1)): 
        if n % i == 0: 
            return False 
    return True 

assert is_prime(13)
assert not is_prime(15)

def brute_force(): 
    best = 0 
    best_prod = 0 
    for a in range(-999, 1000): 
        for b in range(1, 1001): 
            n = 0
            while is_prime(n ** 2 + (a * n) + b):
                n += 1 
            if n > best: 
                best = n 
                best_prod = a * b 
    return best_prod

print(brute_force())