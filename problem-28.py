
# simulating the spiral was ... hard 
# notice the corners: each descends to 1 in different but predictable steps 
# this was pretty difficult analytically: https://math.berkeley.edu/~elafandi/euler/p28/
p28 = lambda n=1001: 2*(n**3 - n)//3 + (n**2 - 1)//2 + 2*n - 1

print(p28())


# okay back with some clarifications 
# the corners follow this pattern: 
    # top-right: n^2 
    # top-left: n^2 - (n - 1)
    # bottom-left: n^2 - 2(n - 1)
    # bottom-right: n^2 - 3(n - 1)
# so the sum of corners is 4n^2 - 6(n - 1)
def diff_p28(size:int)->int:
    total = 1 # this is the base case, center 
    for n in range(3, size + 1, 2): # only odd layers 
        total += 4 * n ** 2 - 6 * (n - 1)
    return total  

print(diff_p28(1001))