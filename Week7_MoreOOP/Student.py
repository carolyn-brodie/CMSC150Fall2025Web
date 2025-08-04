class Student:

    ## constructor
    def __init__(self, name, studentid):
        self.name = name
        self.id = studentid

    ## str
    def __str__(self):
        return f"{self.name} is a student with id {self.id}"


class Course:

    def __init__(self, department, number):
        self.department = department
        self.dept_number = number
        self.students = []

    def add_students(self, new_student):
        if new_student not in self.students:
            self.students.append(new_student)

    def drop_students(self, student_to_remove):
        if student_to_remove in self.students:
            self.students.remove(student_to_remove)

    def __str__(self):
        out = f"{self.department} {self.dept_number} has the following students:\n"
        for std in self.students:
            out = out + f"\t{std}\n"
        return out


def tester():
    suzy = Student("Suzy", 123)
    tommy = Student("Tommy", 456)
    cmsc150 = Course("CMSC", 150)
    print(cmsc150)
    cmsc150.add_students(suzy)
    cmsc150.add_students(tommy)
    print(cmsc150)


if __name__ == "__main__":
    tester()