
def is_pythagorean_triple(arr: tuple[int]) -> bool: 
    a,b,c = arr 
    return (a**2 + b**2) == (c**2)

assert is_pythagorean_triple([3, 4, 5])

# i need to find three numbers that sum to 1000 
# and then make sure they are pythagorean triples 
# this takes way too long lol 
# def solve(): 
#     for i in range(1, 1001): 
#         for j in range(1, 1001): 
#             for k in range(1, 1001): 
#                 if i + j + k == 1000 and is_pythagorean_triple((i, j, k)): 
#                     return(i * j * k)

# can reduce redundant checks by realizing 1000 - a - b = c 
def solve():
    for a in range(1, 1000):
        for b in range(a + 1, 1000 - a):
            c = 1000 - a - b
            if c > b and is_pythagorean_triple((a, b, c)):
                return a * b * c
                
print(solve())