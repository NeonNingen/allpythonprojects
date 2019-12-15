pass_ok=False #My Validations
age_ok=False
year_ok=False
import re #The module I'm using 

#Notes: This Code Updates all the time due to my decision in layout and style also, (Note to Future Self) Remember to put the code in this order:
#(File_intro)(validate)(user_register)(username_and_password_file_1)(user_1_start)(Quiz Menu)(Quiz (Easy/Medium/Hard)(Replay (Yes/No)(Yes = Quiz Menu)(No = user_register)(loop)


def file_intro():
    with open('All User Details and Results.txt', 'a') as name_of_student:
            name_of_student.write("All User Details and Results Below!\n")
    with open('User One\'s Details and Results.txt', 'a') as name_of_student:
            name_of_student.write("User One\'s Details and Results Below!\n")
    with open('User Two\'s Details and Results.txt', 'a') as name_of_student:
            name_of_student.write("User Two\'s Details and Results Below!\n")
    with open('User Three\'s Details and Results.txt', 'a') as name_of_student:
            name_of_student.write("User Three\'s Details and Results Below!\n")

                                  
def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 7:
            print("Make sure your password is at least 7 letters")
            pass_ok=False
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
            pass_ok=False
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
            pass_ok=False
        else:
            print("Your password seems fine\n")
            pass_ok=True
            return password
            break

def user_register():
    user_name = input("Enter your Username - ")
    while True:
        age = input("Enter your age - ")
        if re.search('[0-9]',age) is None:
            print("Must have a Number")
            age_ok=False
        else:
            age_ok=True
            break
    while True:
        year_group = input("Enter your year group - ")
        if re.search('[0-9]',year_group) is None:
            print("Must have a number")
            year_ok=False
        else:
            year_ok=True
            break 
    u_username = print("Your Unique Username - " + user_name[0:3] + age[0:3]) #Unique Username
    return user_name, age, year_group, u_username

def username_and_password_file_1(a,b,c,d,e):
    with open('All User Details and Results.txt', 'a') as name_of_student:
        name_of_student.write("\n1st Username - " + '{0}'.format(a))
        name_of_student.write("\nAge of this user - " + '{0}'.format(b))
        name_of_student.write("\nYear Group of this user - " + '{0}'.format(c))
        name_of_student.write("\nUnique Username of this user - " + '{0}'.format(d))
        name_of_student.write("\nPassword for this user is - " + '{0}'.format(e))
    with open('User One\'s Details and Results.txt', 'a') as name_of_student:
        name_of_student.write("\n1st Username - " + '{0}'.format(a))
        name_of_student.write("\nAge of this user - " + '{0}'.format(b))
        name_of_student.write("\nYear Group of this user - " + '{0}'.format(c))
        name_of_student.write("\nUnique Username of this user - " + '{0}'.format(d))
        name_of_student.write("\nPassword for this user is - " + '{0}'.format(e))
    user_name_1 = a
    u_username_1 = d
    return user_name_1, u_username_1


def username_and_password_file_2(f,g,h,i,j):
    with open('All User Details and Results.txt', 'a') as name_of_student:
        name_of_student.write("\n\n2nd Username - " + '{0}'.format(f))
        name_of_student.write("\nAge of this user - " + '{0}'.format(g))
        name_of_student.write("\nYear Group of this user - " + '{0}'.format(h))
        name_of_student.write("\nUnique Username of this user - " + '{0}'.format(i))
        name_of_student.write("\nPassword for this user is - " + '{0}'.format(j))
    with open('User Two\'s Details and Results.txt', 'a') as name_of_student:
        name_of_student.write("\n2st Username - " + '{0}'.format(f))
        name_of_student.write("\nAge of this user - " + '{0}'.format(g))
        name_of_student.write("\nYear Group of this user - " + '{0}'.format(h))
        name_of_student.write("\nUnique Username of this user - " + '{0}'.format(i))
        name_of_student.write("\nPassword for this user is - " + '{0}'.format(j))
    user_name_2 = f
    u_username_2 = i
    return user_name_2, u_username_2

def username_and_password_file_3(k,l,m,n,o):
    with open('All User Details and Results.txt', 'a') as name_of_student:
        name_of_student.write("\n\n3rd Username - " + '{0}'.format(k))
        name_of_student.write("\nAge of this user - " + '{0}'.format(l))
        name_of_student.write("\nYear Group of this user - " + '{0}'.format(m))
        name_of_student.write("\nUnique Username of this user - " + '{0}'.format(n))
        name_of_student.write("\nPassword for this user is - " + '{0}'.format(o))
    with open('User Three\'s Details and Results.txt', 'a') as name_of_student:
        name_of_student.write("\n3st Username - " + '{0}'.format(k))
        name_of_student.write("\nAge of this user - " + '{0}'.format(l))
        name_of_student.write("\nYear Group of this user - " + '{0}'.format(m))
        name_of_student.write("\nUnique Username of this user - " + '{0}'.format(n))
        name_of_student.write("\nPassword for this user is - " + '{0}'.format(o))
    user_name_3 = k
    u_username_3 = n
    return user_name_3, u_username_3
    
def user_1_start(u):
    print("User One- {0} Begin!".format(u))
    print("Going To Game Menu")

def choices():
    difficulties = [Easy,Medium,Hard]

def main():
    file_intro()
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_1, u_username_1 = username_and_password_file_1(user_name, age, year_group, password, u_username)
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_2, u_username_2 = username_and_password_file_2(user_name, age, year_group, password, u_username)
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_3, u_username_3 = username_and_password_file_3(user_name, age, year_group, password, u_username)
    user_1_start(u_username_1)
main()

