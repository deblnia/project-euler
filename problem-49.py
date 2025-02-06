
from itertools  import permutations 

def is_prime(n:int)->bool: 
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False 
    return True 

def gen_permutations(n:int)->list[int]: 
    perms = set(int(''.join(p)) for p in permutations(str(n)))
    return sorted(p for p in perms if p >= 1000 and is_prime(p)) 

found_sequences = set()

for i in range(1000, 10000):
    if not is_prime(i):
        continue

    primes = gen_permutations(i)

    for j in range(len(primes)):
        for k in range(j + 1, len(primes)):
            diff = primes[k] - primes[j]
            third = primes[k] + diff
            if third in primes and (primes[j], primes[k], third) not in found_sequences:
                found_sequences.add((primes[j], primes[k], third))

found_sequences.discard((1487, 4817, 8147))

print(found_sequences)
