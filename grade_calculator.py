import csv

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'D'

# Ask how many students
num_students = int(input("Enter number of students: "))

# List to store data
data = []

for i in range(num_students):
    name = input(f"Enter student {i+1} name: ")
    marks = int(input(f"Enter {name}'s marks: "))
    grade = calculate_grade(marks)
    data.append([name, marks, grade])

# Save to CSV
with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Marks', 'Grade'])  # header
    writer.writerows(data)

print("✅ Grades saved to grades.csv")
