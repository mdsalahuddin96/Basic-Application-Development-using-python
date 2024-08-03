class Student:
    def __init__(self,r,n,g):
        self.roll=r
        self.name=n
        self.gpa=g
    def student_info(self):
        print(f'I am {self.name},my roll and gpa is {self.roll},and {self.gpa}')
T=Student(10,'Wahid',3.5)
S=Student(20,'Utsab',3.6)
J=Student(30,'Foysal',3.3)
T.student_info()
S.student_info()
J.student_info()


