'''n = str(input("Enter your name: "))
print("Hello", n,"!") 

print("Asterisks")
for i in range(5):
    print("*" * (2 * i + 1))
#A
print("A")
for i in range(6):
    if i == 0 or i == 5:
        print("*" * 20)
    else:
        print("*" + " " * 18 + "*")
#B
print("B")
for i in range(6):
    print(" " * (6 - i) + "*" * (2 * i - 1))

#C
print("C")
for i in range(6):
    print("*" * (2 * i - 1) + " " * (10 - 2 * i))

#D
print("D")
for i in range(6):
    print(" " * (10 - 2 * i) + "*" * (2 * i - 1))
#E
print("E")
for i in range(5):
    if i == 0 or i == 4:
        print(" "*4 + "*"*1)
    elif i == 1 or i == 3:
        print(" "*2 + "*"*3)
    else:
        print("*"*5)

#F
print("F")
for i in range(6):
    if i <=2:
        print(" " * (3 - i) + "*" * (2 * i - 1))
    else:
        print(" " * (i - 3) + "*" * (11 - 2 * i))

#G
print("G")
for i in range(1,6):
    if i <=3 :
        print(" " * (i - 1) + "*" * (7 - 2 * i))
    else:
        print(" " * (5 - i) + "*" * (2 * i - 5))

#H
print("H.")
for i in range(5):
    if i == 0 or i == 4:
        print("      *")
    elif i == 1 or i == 3:
        print("    *   *")
    else:
        print("  *       *")    





name = "Dara"                
age = 20                      
score = 85.5                  
is_passed = True              
remarks = None                

subjects = ["Python", "Math", "English"]  #list
student_info = ("Dara", 20)               #tuple
scores = {"Python": 85.5, "Math": 90.0}   #dict
departments = {"Data Science", "IT"}      #set

#Student Record using a Dictionary
student = {
    "name": name,
    "age": age,
    "scores": scores,
    "is_passed": is_passed,
    "remarks": remarks,
    "subjects": subjects
}
#Display Student Information
print("Student Name:", student["name"])
print("Age:", student["age"])
print("Subjects:", student["subjects"])
print("Scores:", student["scores"])
print("Passed:", student["is_passed"])
print("Remarks:", student["remarks"])
print("Departments:", departments)


class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)


#student objects
students = [
    Student("Dara", [80, 90, 85]),
    Student("Sokha", [10, 15, 32]),
    Student("Lina", [90, 95, 88])
]
#display students and calculate averages
lowest_average = min(student.average() for student in students)
#display students except the one with the lowest average
for student in students:
    if student.average() == lowest_average:
        continue  # Skip the student with the lowest average

    print(student.name, "Average:", student.average())
#search for a student
search_name = input("Enter student name to search: ")
i = 0

while i < len(students):
    if students[i].name.lower() == search_name.lower():
        print("Found:", students[i].name, 'with average score of', students[i].average())
    
        break
    i += 1
else:
    print("Student not found")

#Pass statement
for student in students:
    if student.name == "Dara":
        pass  # Skip Dara
    print(student.name)  '''

tags = {"python", "data", "python"}  # dup dropped
tags.add("ml")
tags.remove("data")
print(tags)
print("ml") in tags


a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference

a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)                      
squares = {n**2 for n in range(5)}   
print(squares)


{
"name": "Sokha",
"age": 21,
"scores": [90, 85]
}

student["gpa"] = 3.8       # add a new key
student["age"] = 22        # update existing key
del student["name"]       # delete a key
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

prices = {"apple": 0.5, "banana": 0.3}
for fruit, price in prices.items():
    print(fruit, "->", price)
doubled = {k: v * 2 for k, v in prices.items()}
print(doubled)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        print(f"{self.name} is eating.")
class Dog(Animal):
    def bark(self):
        print("Woof!")
class Cat(Animal):
    def meow(self):
        print("Meow!")
