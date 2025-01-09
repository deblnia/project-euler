
# # first pass but super super slow 
# def triangular(num: int)->int: 
#     """
#     Returns the value of the num-th triangular number 
#     """
#     return sum([x for x in range(1, num + 1)])

# assert triangular(7) == 28 

# def find_factors(num: int) -> dict[int, list]: 
#     """
#     Takes in a number that indexes the triangular values 
#     Returns a dictionary of triangular values and a list of their factors 
#     """
#     tri = []
#     for i in range(1, num + 1): 
#         tri.append(triangular(i))
#     d = {}
#     for i in tri:
#         d[i] = []
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 d[i].append(j)
#     return d

# assert find_factors(7) == {1: [1], 3: [1, 3], 6: [1, 2, 3, 6], 10: [1, 2, 5, 10], 15: [1, 3, 5, 15], 21: [1, 3, 7, 21], 28: [1, 2, 4, 7, 14, 28]}


# # I'm trying to find the first triangular number to have len(d[i]) >= 500 
# i = 1
# while True:
#     tri_num = triangular(i)
#     d = find_factors(i)
#     if len(d[tri_num]) >= 500:
#         print(tri_num)
#         break
#     i += 1


def triangular(num: int) -> int:
    """
    Returns the value of the num-th triangular number
    """
    return num * (num + 1) // 2  # Formula for triangular numbers 

assert triangular(7) == 28

def count_factors(num: int) -> int:
    """
    Returns the number of factors of a given number
    """
    count = 0
    sqrt_n = int(num**0.5)
    for i in range(1, sqrt_n + 1):
        if num % i == 0:
            count += 2 if i != num // i else 1
    return count

assert count_factors(28) == 6

i = 1
while True:
    tri_num = triangular(i)
    if count_factors(tri_num) >= 500:
        print(tri_num)
        break
    i += 1