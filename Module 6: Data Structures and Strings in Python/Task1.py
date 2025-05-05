# Task 1: Create a Dictionary of Student Marks

name = input("Enter the student name: ")
try:
    students_marks = {
    "Amit": 85,
    "Priya": 92,
    "Rahul": 76,
    "Sneha": 89,
    "Vikram": 67,
    "Anjali": 95,
    "Sourav": 81,
    "Pooja": 74,
    "Karan": 88,
    "Neha": 90
    }
    print(f"{name} : {students_marks[name]}")
          
except KeyError:
    print("Student not found.")


