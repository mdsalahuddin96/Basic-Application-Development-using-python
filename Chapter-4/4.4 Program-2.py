class person:
    name = "Wahidullah"
    sex = "Male"
    age = 25

    def person_info(self):
        print(f'I am {self.name}, {self.age} years old and I am {self.sex}')
p=person()
print(p.name)
p.person_info()