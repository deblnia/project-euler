
from functools import reduce 
# had a similar idea but i am losing the ability to debug 
# creds to https://www.thehiddenblade.com/project-euler-now-all-problems-50-solved
s=''.join([str(i) for i in range(1,1_000_000)])
print(reduce(lambda x,y: x*y, map(int,[s[0],s[9],s[99],s[999],s[9999],s[99999],s[999999]])))


s2 = '' 
for i in range(1, 1_000_000): 
	s2 += str(i) 

acc = 1 
for i in range(1, 1_000_000): 
	if i == 0 or i == 9 or i == 99 or i == 999 or i == 9999 or i == 99_999 or i == 999_999: 
		print(i) 
		acc *= int(s2[i]) 
print(acc)  
