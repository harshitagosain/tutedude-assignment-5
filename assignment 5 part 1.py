student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 76
}
name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")