N = "Sorting1234"
s = sorted(N)
lower = list(filter(lambda x: x.islower(), s))
upper = list(filter(lambda x: x.isupper(), s))
odd = list(filter(lambda x: x.isdigit() and int(x)%2==1,s))
even = list(filter(lambda x: x.isdigit() and int(x)%2==0,s))
print(*(lower+upper+odd+even),sep='')

# sl = []
# su = []
# dodd = []
# deven = []
# for c in s:
#     if c.islower():
#         sl.append(c)
#     if c.isdigit():
#         if int(c)%2==0:
#             deven.append(c)
#         else:
#             dodd.append(c)
#     if c.isupper():
#         su.append(c)
# result = ''.join(sl+su+dodd+deven)
# print(result)