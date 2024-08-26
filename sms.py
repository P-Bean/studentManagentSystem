# The Student Object
class Student:
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

# The student Database
# storing multiple functions for easier retrival when called
class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.id] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def display_all_students(self):
        for student in self.students.values():
            print(student)

    def get_student_by_id(self, student_id):
        return self.students.get(student_id)


def main():
    database = StudentDatabase()

    # Display menu for the User
    while True:
        print("\nStudent Management System Menu:")
        print("1. Add new student")
        print("2. Delete student")
        print("3. Update student info")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        # when a choice is made, loops
        # through until the exit option is selected
        if choice == "1":

            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            major = input("Enter student major: ")
            student = Student(id, name, age, major)
            database.add_student(student)

        elif choice == "2":

            student_id = int(input("Enter student ID to delete: "))
            database.remove_student(student_id)

        elif choice == "3":
            
            student_id = int(input("Enter student ID to update: "))
            student = database.get_student_by_id(student_id)
            if student:
                print("Enter new details (press Enter to keep current value):")
                name = input("Enter new name: ") or student.name
                age = int(input("Enter new age: ") or student.age)
                major = input("Enter new major: ") or student.major
                student.name = name
                student.age = age
                student.major = major
            else:
                print("Student not found!")

        elif choice == "4":
            database.display_all_students()

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
