

def is_palindrome(n: int)->bool: 
    return str(n) == str(n)[::-1] 

if is_palindrome(585): 
    print("Pass") 

if is_palindrome(1001001001): 
    print("Pass") 

def to_binary(n:int)->str:
    return bin(n) 

if to_binary(585) == "0b1001001001":
    print("Pass") 

ts = []
for i in range(1, 1_000_000 + 1): 
    if is_palindrome(i) and is_palindrome(to_binary(i)[2:]): 
        ts.append(i) 
print(sum(ts))
