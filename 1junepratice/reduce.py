from functools import reduce

# numbers = [1, 2, 3, 4, 5]
# res = reduce(lambda x,y:x+y,numbers)

# print(res)

#  Find the largest numbers

numbers = [45, 12, 78, 99, 23]

largest = reduce(lambda x,y: x if x>y else y, numbers)

# print(largest)

# Multiply all numbers

nums = [1,2,3,4,5,6]
res = reduce(lambda x,y: x*y,nums)
print(res)