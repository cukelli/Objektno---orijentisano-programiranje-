class Student(object):

    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        self._grades = []
        self._average = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    def set_average(self, average):
        self._average = average

    def add_grade(self, grade):
        self._grades.append(grade)

    def remove_grade(self, grade):
        self._grades.remove(grade)

    def calculate_average(self):
        sum = 0
        counter = 0
        for grade in self._grades:
            sum = sum + grade
            counter = counter + 1
            average = sum / counter
        return "Student's average grade is " + str(average)

    def __str__(self):
        return "Student's name is " + self._name + " ,and surname is " + self._surname


if __name__ == "__main__":
    student = Student("Pera", "Peric")
    print(student)
    student.add_grade(6)
    student.add_grade(8)
    print(student._grades)
    student.calculate_average()
    print(student.calculate_average())
    student.add_grade(10)
    print(student.calculate_average())
