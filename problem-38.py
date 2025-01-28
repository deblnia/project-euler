

def is_pandigital(target:int)->bool: 
	return len(str(target)) == 9 and set(str(target)) == set('123456789')

if is_pandigital(192384576):
	print("Pass") 
if not is_pandigital(12345):
	print("Pass") 


def concatenate_products(k:int, n:int)->str: 
	""" Generate concatenated products of k with integers from 1 to n"""
	return ''.join(str(k * i) for i in range(1, n + 1))

if concatenate_products(3,4) == '36912':
	print("Pass") 


mx = 0 

for k in range(1, 10_000): 
	for n in range(2, 10): 
		p_str = concatenate_products(k, n) 
		if len(p_str) > 9:
			break
		if is_pandigital(p_str) and int(p_str) > mx:
			mx = int(p_str) 

print(mx)  
			
		
