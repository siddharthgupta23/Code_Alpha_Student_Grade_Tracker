from tabulate import tabulate

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grades(self, grades):
        valid_grades = [grade for grade in grades if 0 <= grade <= 100]
        if len(valid_grades) != len(grades):
            print("Some grades were invalid and not added. Please ensure grades are between 0 and 100.")
        self.grades.extend(valid_grades)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_grade_letter(self, average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def get_details(self):
        grades_str = ', '.join(str(grade) for grade in self.grades)
        average = self.get_average()
        grade_letter = self.get_grade_letter(average)
        return [self.name, grades_str, f"{average:.2f}", grade_letter]


class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
        else:
            print(f"Student {student_name} already exists.")

    def add_grades_for_student(self, student_name, grades):
        if student_name in self.students:
            self.students[student_name].add_grades(grades)
        else:
            print(f"Student {student_name} not found. Please add the student first.")

    def display_all_students(self):
        if not self.students:
            print("No students available.")
        else:
            table = [["Name", "Grades", "Average", "Grade"]]
            for student in self.students.values():
                table.append(student.get_details())
            print(tabulate(table, headers="firstrow", tablefmt="grid"))

    def delete_student(self, student_name):
        if student_name in self.students:
            del self.students[student_name]
            print(f"Student {student_name} has been deleted.")
        else:
            print(f"Student {student_name} not found.")
        self.display_all_students()


def main():
    tracker = GradeTracker()

    while True:
        
        print("1. Add Student")
        print("2. Add Grades for Student")
        print("3. Display All Student Grades")
        print("4. Delete Student Details")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            student_name = input("Enter the student's name: ")
            tracker.add_student(student_name)

        elif choice == '2':
            student_name = input("Enter the student's name: ")
            try:
                num_subjects = int(input("How many subjects' marks do you want to enter? "))
                grades = []
                for i in range(num_subjects):
                    grade = float(input(f"Enter marks for subject {i+1}: "))
                    grades.append(grade)
                tracker.add_grades_for_student(student_name, grades)
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '3':
            tracker.display_all_students()

        elif choice == '4':
            student_name = input("Enter the name of the student to delete: ")
            tracker.delete_student(student_name)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

