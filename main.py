students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("\nStudent added successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n===== STUDENT LIST =====")

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")
        print("------------------------")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Try again.")


main()
