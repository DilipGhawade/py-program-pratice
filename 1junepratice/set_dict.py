square_dict = {x: x*x for x in range(1, 6)}

# print(square_dict)

words = ["apple","banana", "orange"]
res = {word :len(word) for word in words}
print(res)
