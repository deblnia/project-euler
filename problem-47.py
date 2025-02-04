

def is_prime(n: int)->bool: 
	if n < 2: 
		return False 
	for i in range(2, int(n ** 0.5) + 1): 
		if n % i == 0: 
			return False 
	return True 	

def n_prime_factors(n: int)->int:
	pf = set()  	 
	i = 2 
	while i * i <= n: 
		if n % i == 0 and is_prime(i): 
			pf.add(i)
			while n % i  == 0: 
				n = n / i 
		i += 1 
	if n > 1: 
		pf.add(int(n)) 
	return len(pf)  


assert n_prime_factors(14) == 2 
assert n_prime_factors(15) == 2

def p47()->int: 
	i = 2 
	while True: 
		if (n_prime_factors(i) == 4 and 
			n_prime_factors(i + 1) == 4 and 
			n_prime_factors(i + 2) == 4 and 
			n_prime_factors(i + 3) == 4): 
			return i 
		i += 1 

print(p47())  
