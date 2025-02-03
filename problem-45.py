
import math 

def is_triangular(n:int)->bool:
	discrim = 1 + 8 * n 
	sd = math.sqrt(discrim)
	return sd == int(sd) 
	

def is_pentagonal(n:int)->bool: 
	discrim = 1 + 24 * n
	sd = math.sqrt(discrim) 
	return sd == int(sd) and ((1 + sd) / 6) % 1 == 0 

def is_hexagonal(n:int)->bool:
	k = (1 + math.sqrt(1 + 8*n)) / 4 
	return k == int(k) 
	 

n = 40756
while True: 
	if is_triangular(n) and is_pentagonal(n) and is_hexagonal(n): 
		print(n) 
		break 
	n += 1 


