# Student_info.py

class Student:

    
    def __init__(self, forename, surname, present):
        self.forename = forename
        self.surname = surname
        self.present = present
        self.numofstudents = -1
        self.listofstudents = []
        self.lessons = ["English", "Maths", "Science"]
        

    def fullname(self):
        self.fullname = self.forename + " " + self.surname
        return print(self.fullname)

    def is_present(self):
        if self.present == "TRUE":
            self.numofstudents += 1
            self.listofstudents.append(self.fullname)
            return print("{} is here, therefore they will be in class".format(self.forename))
        else:
            self.numofstudents -= 1
            return print("{} is not here".format(self.forename))


    def getLesson(self):
        listless = self.lessons
        return print("{}'s lesson is {}".format(self.forename, listless[self.numofstudents]))

    def list_students(self):
        liststd = self.listofstudents
        return print("There is {} student(s) in the class and they are {}".format(self.numofstudents + 1, liststd))
    
        

    
        
        
