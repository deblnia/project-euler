

def primes_up_to(num: int) -> int: 
    size = num * 200
    is_prime = [True] * size 
    # 0 and 1 are not prime
    is_prime[0] = is_prime[1] = False

    # finding primes using sieve of eratosthenes
    for i in range(2, int(size ** 0.5) + 1):
        if is_prime[i]: 
            # cross out all multiples 
            for multiple in range(i * i, size, i): 
                is_prime[multiple] = False 
    primes = []
    for i in range(size): 
        if is_prime[i]:
            primes.append(i)
            if len(primes) == num: 
                return primes[-1]
    return primes[-1]


assert primes_up_to(6) == 13
print(primes_up_to(10001))