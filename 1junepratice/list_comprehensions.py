nums = [1,2,3,4,5]
squars = [n**2 for n in nums]
# print(squars)

# print event numbers from given list of range

numbers = range(1,21)
evens = [n for n in numbers if n %2==0]
# print(evens)

# upper case the number
names = ["john", "sam","ales"]
res = [name.upper() for name in names]
print(res)