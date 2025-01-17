
import itertools 

# this uses the generator object and is more efficient 
# perms = itertools.permutations([0, 1,2,3,4,5,6,7,8,9])
# millionth_permutation = next(itertools.islice(perms, 1_000_000 - 1, None))
# print("".join(map(str, millionth_permutation)))

# this was my first thought - don't forget the 0! 
perms = list(itertools.permutations([0, 1,2,3,4,5,6,7,8,9])) 
print(perms[999999])
