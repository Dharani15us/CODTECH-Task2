class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

class GradeTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)
            print(f"Added student: {name}")
        else:
            print(f"Student {name} already exists.")

    def record_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grade(grade)
            print(f"Recorded grade {grade} for {name}.")
        else:
            print(f"Student {name} not found.")

    def get_average(self, name):
        if name in self.students:
            avg = self.students[name].average_grade()
            print(f"{name}'s average grade: {avg:.2f}")
        else:
            print(f"Student {name} not found.")

def main():
    tracker = GradeTracker()

    while True:
        action = input("Choose an action: add_student, record_grade, get_average, exit: ").strip().lower()

        if action == 'add_student':
            name = input("Enter student name: ")
            tracker.add_student(name)

        elif action == 'record_grade':
            name = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            tracker.record_grade(name, grade)

        elif action == 'get_average':
            name = input("Enter student name: ")
            tracker.get_average(name)

        elif action == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
