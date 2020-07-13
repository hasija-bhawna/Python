class schoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initializing SchoolMember {}!'.format(self.name))

    def tell(self):
        print('Name:{} Age:{}'.format(self.name, self.age), end=" ")


class Teacher(schoolMember):
    def __init__(self, name, age, salary):
        schoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher {}'.format(self.name))

    def tell(self):
        schoolMember.tell(self)
        print('Salary:{}'.format(self.salary))


class Student(schoolMember):
    def __init__(self, name, age, marks):
        schoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized Student {}'.format(self.name))

    def tell(self):
        schoolMember.tell(self)
        print('Marks:{}'.format(self.marks))

t = Teacher('Bhawna','35','25000')
s = Student('Rayhan','5',67)

members = [t,s]
for member in members:
    member.tell()
