# Creating a base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Initialize the base class
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)
        self._a = 3
        print("Calling modified protected member inside derived class: ", self._a)

# Creating objects of Derived and Base class
obj1 = Derived()
obj2 = Base()

# Accessing the protected member
print("Accessing protected member of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)
