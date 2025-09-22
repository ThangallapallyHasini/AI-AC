# Define a function to welcome a student
def welcome_student(name):
    print("Welcome", name)  # Print a welcome message

students = ["Alice", "Bob", "Charlie"]  # List of student names

# Loop through each student and call the function
for student in students:
    welcome_student(student)