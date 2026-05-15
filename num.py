# Take two number from user and make addition of it

# num1 = int(input("Enter first number  "))
# num2 = int(input("Enter second number"))
# res = num1+num2
# print(f"The addition of {num1} and {num2} is = {res}")

# check the given number is even or odd 
# if num1 % 2 ==0:
#     print("Event Number")
# else:
#     print("Odd number")    

# check the voting  age
# age = int(input("Enter your age  "))

# if age >=18:
#     print("You can vote")
# else:
#     print("You can not vote")

# find the biggest number
# 
# num = int(input("Ener first number ")) 
# num2 = int(input("Enter second number "))

# if num > num2:
#     print(num, "is bigger")
# else :
#     print(num2,"is bigger")

# for i in range(1,11):
#     print(num*i)

# sum of 1 to 10
# total = 0

# for i in range(1,11):
#     total = total + i
# print(f"The totoal is {total}")



#  count character in string

# name = input("Enter a name ")

# count = len(name)
# print(count)

#  Reverse a string

# text = "dilip"
# reverse = text[::-1]
# print(f"reverse text is {reverse}")


#  count vowels

# text = "dilip"
# count=0
# for ch in text:
#     if ch in "aeiouAEIOU":
#         count +=1
# print("Vowels: ",count)

# Find factorial

# fact=1
# num=5
# for i in range(1,num+1):
#     fact = fact*i
# print("Factorial: ", fact)

# check the string is palindrome

word = "python"

# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Print * pattern 
# for i in range(1,6):
#     print("*" * i)

def welcome():
    print("Welcome back Dilip ")

# welcome()

def print_username():
    name = input("Enter you name ")
    print(f"Hello, {name}")

# print_username()

# Add Two numbers

def add():
    n1= int(input("Enter numer 1 "))
    n2= int(input("Enter numer 2 "))
    total = n1+n2
    print("Sum: ", total)
# add()

#check the no is even or odd

def check_even_odd():
    number = int(input("Enter a number"))
    if number %2 ==0:
        print("Even")
    else:
        print("Odd")
# check_even_odd()

def add(a:int,b:int):
    return a+b
# res = add(12,12)
# print(res)

# print multiplication table

def table(a:int):

    for i in range(1, 11):
        print(a*i)
# num = int(input("Enter number to generate a table "))

# table(num)

# check even odd number

def even_odd(num:int):
    if num %2==0:
        print("Even")
    else:
        print("Odd")
# even_odd(7)

