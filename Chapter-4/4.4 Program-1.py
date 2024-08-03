class person:
    name = "Wahidullah"
    sex = "Male"
    age = 25

    def person_info(self):
        print(f'I am {p.name}, {p.age} years old and I am {p.sex}')
p=person()
print(p.name)
p.person_info()