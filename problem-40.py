
from functools import reduce 
# had a similar idea but i am losing the ability to debug 
# creds to https://www.thehiddenblade.com/project-euler-now-all-problems-50-solved
s=''.join([str(i) for i in range(1,1_000_000)])
print(reduce(lambda x,y: x*y, map(int,[s[0],s[9],s[99],s[999],s[9999],s[99999],s[999999]])))
