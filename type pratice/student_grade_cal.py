
def calculate_grade(marks:list[int]) -> float:
    return sum(marks)/len(marks)

marks = [80,90,75]

print(calculate_grade(marks))