
def find_prime_factors(num: int)->list[int]: 
    prime_factors = []
    factor = 2 
    while num >= 2: 
        if num % factor == 0:
            num = num / factor 
            prime_factors.append(factor) 
        else: 
            factor += 1 
    return prime_factors

max(find_prime_factors(600851475143))


