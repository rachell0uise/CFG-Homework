class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()



class CFGStudent(Student):
    def __init__(self, name,age, id, subject):
        super().__init__(name,age, id)
        self.subject = subject


student_1 = CFGStudent ('Steve Harrington', 17, 4532, 'Software')
student_2 = CFGStudent ('Eddie Munson', 18, 3254, 'Data Science')