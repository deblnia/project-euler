
def is_prime(num: int) -> bool: 
    if num <= 1: 
        return False 
    for i in range(2, num // 2 + 1): 
        if num % i == 0: 
            return False 
    return True  

assert is_prime(5) 
assert not is_prime(8)

# waaaaay too slow 
# def sum_primes_below(num: int)->int:
#     primes = [] 
#     for i in range(1, num + 1):
#         if is_prime(i): 
#             primes.append(i)
#     return sum(primes)  

def sum_primes_below(limit: int) -> int:
    if limit < 2:
        return 0
    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit, start):
                sieve[multiple] = False
    return sum(idx for idx, is_prime in enumerate(sieve) if is_prime)

assert sum_primes_below(10) == 17

print(sum_primes_below(2000000))