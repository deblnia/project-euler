

units = {
    1: 'one', 
    2: 'two', 
    3: 'three', 
    4: 'four', 
    5: 'five', 
    6: 'six', 
    7:'seven', 
    8:'eight', 
    9:'nine' 
}

teens = {
    10: 'ten', 
    11: 'eleven', 
    12: 'twelve', 
    13: 'thirteen', 
    14: 'fourteen', 
    15: 'fifteen', 
    16: 'sixteen', 
    17: 'seventeen', 
    18: 'eighteen', 
    19: 'nineteen'
}


tens = {
    20: 'twenty', 
    30: 'thirty', 
    40: 'forty', 
    50: 'fifty', 
    60: 'sixty', 
    70: 'seventy', 
    80: 'eighty', 
    90: 'ninety' 
}

def number_to_words(n: int) -> str: 
    if 1 <= n <= 9:
        return units[n]
    elif 10 <= n <= 19:
        return teens[n]
    elif 20 <= n <= 99:
        return tens[n // 10 * 10] + (units[n % 10] if n % 10 != 0 else "")
    elif 100 <= n <= 999:
        return units[n // 100] + "hundred" + ("and" + number_to_words(n % 100) if n % 100 != 0 else "")
    elif n == 1000:
        return "onethousand"

test = [] 
for i in range(1, 6): 
    test.append(number_to_words(i))

assert test == ['one', 'two', 'three', 'four', 'five']
assert len(''.join(test)) == 19


solve = [] 
for i in range(1, 1001): 
    solve.append(number_to_words(i))
print(len(''.join(solve).strip()))