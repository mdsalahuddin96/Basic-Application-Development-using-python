
# Programm of custom iterator which prints the factorial of numbers till the limit
#number is reached.
class factorial:

    # constructor
    # Intializing the limit
    def __init__(self, limit):
        self.limit = limit

    # returns an iterator object when called.
    def __iter__(self):
        self.num = 1
        self.fact = 1
        return self

    # returns the factorial of next number
    # until the number <= limit.
    def __next__(self):

        # current number.
        curr_num = self.num

        # current number factorial
        curr_fact = self.fact

        # if current number <= limit
        if curr_num <= self.limit:

            # updating number for next iteration
            self.num = self.num + 1

            # updating factorial for next iteration
            self.fact = self.fact*self.num

            # returning curent number factorial
            return curr_fact

        # if number exceeds limit raise error
        else:
            raise StopIteration

# intialzing the object of the class factorial
fact = factorial(5)
for x in fact:
    print(x)

