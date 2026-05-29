class Student:
    school = "ABC School"
    def __init__(self,name,age,marks):
        self.name = name
        self.age=age
        self.marks=marks
    def display_info(self):
        print(f"School is {self.school}\n Student Name: {self.name} \n Age: {st.age} Obtained Marks {self.marks}" )
    def is_pass(self):
        if self.marks >=35:
            print("Congrats You are pass")
        else:
            print("Sorry you are failed")


st= Student("Dilip",32,31)
st.display_info()
st.is_pass()
