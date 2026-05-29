# num = int(input("Enter number "))
# result = "Even" if num%2==0 else "Odd"
# print("the given number is ",result)

# day = int(input("Enter a day number "))

# match day: 
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")    
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wensday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Invalid Day")


# for i in range(20,0,0-1):
    # print(i)

def printEven1to50():
    for i in range(1,51):
        if i % 2==0:
            print(i)

printEven1to50()