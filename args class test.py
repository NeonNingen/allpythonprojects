class Person:
    def __init__(self, fname, sname):
        self.firstname = fname
        self.surname = sname

    def fullname(self):
        return "Your Name is: " + self.firstname + " " + self.surname


me = Person("Zain", "Cheema")

print(me.fullname())
