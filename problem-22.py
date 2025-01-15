
with open('inputs/0022_names.txt', "r") as f: 
    names = [x.strip('"') for x in f.read().split(",")]


names.sort() # in place 

# multiply sum of index in digits by index in list 

def find_name_score(name: str) -> int: 
    az = {
        'a' : 1, 
        'b' : 2, 
        'c' : 3, 
        'd' : 4, 
        'e' : 5, 
        'f' : 6, 
        'g' : 7, 
        'h' : 8, 
        'i' : 9, 
        'j' : 10, 
        'k' : 11, 
        'l' : 12, 
        'm' : 13, 
        'n' : 14, 
        'o' : 15, 
        'p' : 16, 
        'q' : 17, 
        'r' : 18, 
        's' : 19, 
        't' : 20, 
        'u' : 21, 
        'v' : 22, 
        'w' : 23, 
        'x' : 24, 
        'y' : 25, 
        'z' : 26
    }
    score = 0 
    name = name.lower() 
    for c in name: 
        score += az[c] 
    return score 

assert find_name_score('COLIN') == 53

total = 0 
for i, name in enumerate(names): 
    # subtle off by one here - enumerate starts from 0! 
    total += ((i + 1) * (find_name_score(name)))
print(total)