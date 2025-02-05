

def self_powers(n:int)->int:
	total = 0
	for i in range(1, n + 1):
		# modular exp avoids integer overflow  
		total += pow(i, i, 10 **10)
	return str(total)[-10:].zfill(10)   

assert self_powers(10) == '0405071317' 

print(self_powers(1000)) 
