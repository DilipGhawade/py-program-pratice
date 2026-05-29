# # count the event number in list 

# num = [2,5,8,7,10,13]
# eventCount = 0
# for i in num:
#     if i%2==0:
#         eventCount +=1

# print("Even count is: ", eventCount)

# numbers = [1,2,2,3,4,4,5]

# numbers.reverse()
# print(numbers)
# Remove duplicates


# unique =[]
# for i in numbers:
#     if i not in unique:
#         unique.append(i)

# print(unique)

# Search element in list

# num = [10,20,30,40]

# n = 30

# if n in num:
#     print("Found")
# else:
#     print("Not found")

# num = [10,20,30,40,10]
# count =  num.count(10)
# print(count)

# Count positive and negative numbers

# num = [10,-2,5,-7,-8,20]

# positive=0
# negative=0

# for i in num:
#     if i >=0:
#         positive +=1
#     else:
#         negative +=1
# print("Positive: ", positive)
# print(F"Negative: {negative}")

#  Find duplicate values only
# num = [1,2,3,2,4,5,1,6]
# duplicates=[]

# for i in num:
#     if num.count(i)>1:
#         if i not in duplicates:
#             duplicates.append(i)

# print(duplicates)

# Count uppercase, lowercase, digits

# text = "PyThon123"

# upper=0
# lower =0
# digits=0

# for ch in text:
#     if ch.isupper():
#         upper +=1
#     elif ch.islower():
#         lower +=1
#     elif ch.isdigit():
#         digits +=1
#     else :
#         print("Invalid char")

# print("Upper:", upper)
# print("Lower:", lower)
# print("Digits:", digits)

# Find character frequency

# for ch in text:
#     count = text.count(ch)
#     print(ch,count)

# def freqCount():
#     freq={}
#     text = "python"
#     for ch in text:
#         freq[ch] = freq.get(ch,0)+1
#     return freq
    

# res = freqCount()
# print(res)

# Print key and values

student = {
    "name":"Dilip",
    "age":32,
    "city":"Pune"
}

for key,value in student.items():
    print(key,value)

 
       
 s