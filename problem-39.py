
def num_solutions(p: int)->int:
    """ Given the perimeter of a right angle triangle, returns numbers of solutions """
    soln = 0
    for i in range(1, p ):
        for j in range(i + 1, p - i): # j >= i to avoid dupes
            k = p - i - j
            if k > j  and i ** 2 + j ** 2 == k ** 2:
                soln += 1
                # print(i, j, k)
    return soln

assert num_solutions(120) == 3

mx_sln = 0
val = 0
for i in range(1, 1000 + 1):
    if num_solutions(i) > mx_sln:
        mx_sln = num_solutions(i)
        val = i

print(val)
