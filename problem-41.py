
from itertools import permutations 
def is_pandigital(n:int)->bool: 
	d = len(str(n)) 
	for i in range(1, d + 1): 
		if str(i) not in str(n): 
			return False 
	return True 

assert is_pandigital(2143) 

def is_prime(n:int)->bool: 
	for i in range(2, int((n ** 0.5)) + 1): 
		if (n %  i) == 0: 
			return False 
	return True 

assert is_prime(31) 
assert not is_prime(9) 

# tricky terminating condition again 
# what range could the largest n-digit be in? 
	# got help: if the sum of digits is divisible by 3 then it's not prime 
	# so not 9 or 8 digits, start with 7 
# also digits still means 1-9 
digits = '7654321' 

pd = [] 
for perm in permutations(digits): 
	num = int(''.join(perm))
	if is_prime(num) and is_pandigital(num): 
		pd.append(num) 

print(max(pd))   
