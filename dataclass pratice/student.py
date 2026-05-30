from dataclasses import dataclass

@dataclass
class Student:
    name:str
    age:int
    address:str

st = Student("Dilip",33,"pune")
print(st)