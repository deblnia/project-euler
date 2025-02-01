
import math 
with open('./inputs/words.txt', 'r') as f: 
    data = f.read().strip('\n').split(",") 
    data = [e.strip('""') for e in data] 

def is_triangular(n:int)->bool:
    # used quadratic formuala to solve for n 
    x = 8 * n + 1 
    root = math.isqrt(x) 
    return root * root == x and (root - 1) % 2 == 0 

assert is_triangular(55)

# from stackoverflow: https://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
# modified by ChatGPT to work with uppercase letters 
def char_position(letter: str)->int: 
    return ord(letter) - ord('A') + 1  

count_tri = 0 
for word in data: 
    total = 0 
    for letter in word: 
        total += char_position(letter)
    if is_triangular(total): 
        count_tri += 1 
print(count_tri) 
