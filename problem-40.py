
from functools import reduce 

s=''.join([str(i) for i in range(1,1_000_000)])
print(reduce(lambda x,y: x*y, map(int,[s[0],s[9],s[99],s[999],s[9999],s[99999],s[999999]])))
