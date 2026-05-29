def square(num:int):
    result = num *num
    print("Square:", result)

# square(6)

# find cube 

def cube(num:int):
    result = num * num*num
    print("Cube: ",result)
# cube(3)

# Convert Celsius to Fahrenheit
# formula -> (c* 9/5)+32

def convert(temp:int):
    fahrenheit = (temp*9/5)+32
    print("Tempreatre: ", fahrenheit)
# convert(30)

# Calculate rectangle area

def area(length:int,width:int):
    result = length * width
    print("Area ",result)

# area(10,5)

# Find simple interest

def interest(p:int,r,t):
    result = (p*r*t)/100

    print("Interest:", result)
# interest(10000,5,2)