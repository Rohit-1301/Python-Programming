from functools import reduce

# # Map Example
lists=[1,2,3,4,5]
# squares = lambda x:x*x

# square=map(squares,lists)
# print(list(square))

# Filter example
# def even(l):
#     if l%2==0:
#         return True
#     else:
#         return False
    
# evens=filter(even,lists)
# print(list(evens))

# Reduce Example
def sum(a,b):
    return a+b

sums=reduce(sum,lists)
print(sums)