class Person:   # This is the parent class, A class is an object.
    def __init__(self, fname, lname):   # A first set of attributes (characteristics) to the class.
        self.firstname = fname  # Variables to be used within other parts of the code.
        self.lastname = lname

    def printname(self):    # A procedure that uses the calls the class .
        return self.firstname + " " +  self.lastname


class Student(Person):  # This is a child class.
    def __init__(self, fname, lname, year):     # Second set of attributes plus previous attributes.
        super().__init__(fname, lname)  # This gives the child class all of its parent attributes. Takes line 2 - 4
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)  # Setting the class's attributes.
x.welcome()     # Printing a procedure with the class set attributes.
print(x.printname())
