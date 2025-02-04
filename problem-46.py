

# composite number is odd and and not prime 

def is_prime(n:int)->bool: 
	if n < 2: 
		return False 
	for i in range(2, int(n ** 0.5) + 1): 
		if n % i == 0: 
			return False 
	return True 

def is_square(n:int)->bool: 
	sqrt = (n ** 0.5) 
	return int(sqrt) == sqrt 

def p46(): 
	n = 3 
	while True: 
		if not is_prime(n): 
			found = False 
			for p in range(2,n): 
				if is_prime(p): 
					dif = n - p 
					# can't be odd or 2*$perfect_square 
					if dif % 2 == 0 and is_square(dif // 2): 
						found = True 
						break 
			if not found:
				return n   
		n += 2 
					





print(p46()) 
