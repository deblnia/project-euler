def is_palindrome_number(num: int) -> bool: 
    return str(num) == str(num)[::-1]

max_pal = float('-inf')
for i in range(100, 999): 
    for j in range(100, 999): 
        if is_palindrome_number(i * j):
            max_pal = max(max_pal, (i*j))
print(max_pal)