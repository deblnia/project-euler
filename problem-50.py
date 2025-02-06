

def is_prime(n:int)-> bool: 
	if n < 2: 
		return False 
	for i in range(2, int(n ** 0.5)+1): 
		if n % i == 0: 
			return False 
	return True 

def sieve_of_eratosthenes(limit:int)->list[int]:
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num**2, limit + 1, num):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def longest_consecutive_sum(primes:list[int], limit:int)->int:
    max_length = 0
    max_prime = 0
    for i in range(len(primes)):
        total = 0
        for j in range(i, len(primes)):
            total += primes[j]
            if total > limit:
                break
            if total in primes and j - i + 1 > max_length:
                max_length = j - i + 1
                max_prime = total
    return max_prime

primes = sieve_of_eratosthenes(1_000_000)
result = longest_consecutive_sum(primes, 1_000_000)
print(result)
