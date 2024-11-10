# divis = []
# for i in range(1,1001):
#   if i % 5 == 0 or i % 3 == 0:
#     divis.append(i)
#   else: 
#     pass
# print(sum(divis))

rv = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
print(rv)
