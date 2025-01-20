
# simulating the spiral was ... hard 
# notice the corners: each descends to 1 in different but predictable steps 
# this was pretty difficult analytically: https://math.berkeley.edu/~elafandi/euler/p28/
p28 = lambda n=1001: 2*(n**3 - n)//3 + (n**2 - 1)//2 + 2*n - 1

print(p28())


