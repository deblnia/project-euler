
from itertools import permutations 

def gen_pandigital_numbers()->list[(int)]: 
    """Returns 10 digit numbers that contain 0-9 exactly once"""
    return list(permutations([0,1,2,3,4,5,6,7,8,9], 10)) 

def is_substring_divisible(n:str)->bool:  
    
    if len(n) != 10: 
        print("N needs to be 10 digits") 
        return False 

    if int(n[1:4]) % 2 != 0:
        return False 
    if int(n[2:5]) % 3 != 0: 
        return False 
    if int(n[3:6]) % 5 != 0: 
        return False 
    if int(n[4:7]) % 7 != 0: 
        return False 
    if int(n[5:8]) % 11 != 0: 
        return False 
    if int(n[6:9]) % 13 != 0: 
        return False 
    if int(n[7:10]) % 17 != 0: 
        return False 
    return True 

assert is_substring_divisible('1406357289')

tot = 0 
pd = gen_pandigital_numbers() 
for i in pd: 
    n = ''.join(str(d) for d in i)
    if is_substring_divisible(n): 
        tot += int(n)  
print(tot) 
