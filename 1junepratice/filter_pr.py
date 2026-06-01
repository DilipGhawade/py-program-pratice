numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = list(filter(lambda x: x%2==0,numbers))

# print(res)



# Names Longer Than 5 Character

names = ["John", "Alexander", "Sam", "Jennifer"]

result = list(filter(lambda name :len(name)>5,names))
# print(result)

#  print positive numbers 

nums  = [-5, 10, -2, 20, 30]
res = list(filter(lambda x:x>0,nums))
print(res)
