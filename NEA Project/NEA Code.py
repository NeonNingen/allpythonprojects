pass_ok=False #My Validations
age_ok=False
year_ok=False
quiz_ok=False
debug_ok = False
import re #The modules I'm using
import sys
import codecs #New to me, allows python to read unicode.
import os
import webbrowser
from time import *
import time

#Notes: This Code Updates all the time due to my decision in layout and style
#Note to all: So Many Throwaway variables/Pointers you could buy a Alienware laptop with these if they were money!

#Also Create a Main Menu That allows multiple options on starting and features.
#E.G. Enter all users details first or just do user 1 or user 2 or user 3. Remember to do this after completing the main menu!
#Features = Help, LeaderBoards, Website to creator of code (Youtube or My own Website) (Add to Credits)!


def file_intro():
    print("\nWelcome to Subject Quizzes, Just enter the first 3 students details\nand then get to playin!\n")
    with open('All User Details and Results.txt', 'w') as name_of_student:
        name_of_student.write("All User Details and Results Below!\n")
    with open('User One\'s Details and Results.txt', 'w') as name_of_student:
        name_of_student.write("User One\'s Details and Results Below!\n")
    with open('User Two\'s Details and Results.txt', 'w') as name_of_student:
        name_of_student.write("User Two\'s Details and Results Below!\n")
    with open('User Three\'s Details and Results.txt', 'w') as name_of_student:
        name_of_student.write("User Three\'s Details and Results Below!\n")
    with open('leaderboard_list.txt', 'w') as name_of_student:
        name_of_student.write("All Scores in the leaderboard below!\n")

#def temp():                               #Spare Debug Parts
    #u_username_1 = input("")
    #u_username_2 = input("")
    #u_username_3 = input("")
    #return u_username_1, u_username_2, u_username_3

def spare_user_2():
    u_username_2 = ("")
    u_username_3 = ("")
    return u_username_2, u_username_3

def spare_user_1():
    u_username_3 = ("")
    return u_username_3
                    
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
    u_username_says = print("Your Unique Username - " + user_name[0:3] + age[0:3]) #Unique Username 
    u_username = (user_name[0:3] + age[0:3])
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
    


# Roses are Red, Violet are blue... Omoi wa mou shinderu!
# NANI!

def user_1_start(u):
    for quest in "User One- {0} Begin!".format(u):
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write('\r')
    sys.stdout.flush()
    print("\nGoing To Game Menu")

def user_2_start(xz):
    for quest in "User Two- {0} Begin!".format(xz):
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write('\r')
    sys.stdout.flush()
    print("\nGoing To Game Menu")

def user_3_start(xy):
    for quest in "User Three- {0} Begin!".format(xy):
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write('\r')
    sys.stdout.flush()
    print("\nGoing To Game Menu")

def places(number1,number2,number3):
    who_first = input("Who is going first? (Please enter 1,2 or 3. e.g. 1 = User 1)\n")
    if who_first == "1":
        print("Go User 1!\n")
        user_1_start(number1)
        choices(number1, number2, number3)
    elif who_first == "2":
        print("Go User 2!\n")
        user_2_start(number2)
        choices(number1, number2, number3)
    elif who_first == "3":
        print("Go User 3\n")
        user_3_start(number3)
        choices(number1, number2, number3)
    else:
        print("Please Try again, Make sure to enter 1-3")
        number1, number2, number3 = places(number1, number2, number3)


def computer_science_quiz_easy(coolname1,coolname2,coolname3):    #Trying to put a1_easy_1.txt as a file but the code finds it a OS ERROR because a1 is a error code = X071_easy_1.txt so it does not work.
    score_e = 0
    score_e_percentage = 0
    for quest in "\nEach correct answer is 10 points\nEach incorrect answer is negative 10 points\nYou will also gain a percentage and grade in the external text file\n":
        sys.stdout.write(quest)
        sleep(0.04)
    sys.stdout.write('\r')
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_1.txt", "r" ) as e_easy_quiz_1:
        e_questions_1 = e_easy_quiz_1.read().splitlines()
    for eachLine in e_questions_1:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_1_easy = input("Input 1-2 ")
        if e_answers_1_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        elif e_answers_1_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nPlease enter a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_2_easy = input("Input 1-2 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_3.txt", "r" ) as e_easy_quiz_3:
        e_questions_3 = e_easy_quiz_3.read().splitlines()
    for eachLine in e_questions_3:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_3_easy = input("Input 1-2 ")
        if e_answers_3_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_3.txt", "r" ) as e_easy_quiz_3:
                e_questions_3 = e_easy_quiz_3.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        elif e_answers_3_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_3.txt", "r" ) as e_easy_quiz_3:
                e_questions_3 = e_easy_quiz_3.read().splitlines()
            for eachLine in e_questions_3:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        else:
            print("\nPlease enter a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_4.txt", "r" ) as e_easy_quiz_4:
        e_questions_4 = e_easy_quiz_4.read().splitlines()
    for eachLine in e_questions_4:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_4_easy = input("Input 1-2 ")
        if e_answers_4_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_4.txt", "r" ) as e_easy_quiz_4:
                e_questions_4 = e_easy_quiz_4.read().splitlines()
            for eachLine in e_questions_4:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_4_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_4.txt", "r" ) as e_easy_quiz_4:
                e_questions_4 = e_easy_quiz_4.read().splitlines()
            for eachLine in e_questions_4:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nPlease enter a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_5.txt", "r" ) as e_easy_quiz_5:
        e_questions_5 = e_easy_quiz_5.read().splitlines()
    for eachLine in e_questions_5:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_5_easy = input("Input 1-2 ")
        if e_answers_5_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_5.txt", "r" ) as e_easy_quiz_5:
                e_questions_5 = e_easy_quiz_5.read().splitlines()
            for eachLine in e_questions_5:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_5_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_5.txt", "r" ) as e_easy_quiz_5:
                e_questions_5 = e_easy_quiz_5.read().splitlines()
            for eachLine in e_questions_5:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nPlease enter a valid option 1-2")
            quiz_ok = False
    with open('Computer Science\'s Easy Quiz Results!.txt', 'w') as score_variable:
        score_variable.write("Final results below! (Any Latest Scores go to the Leaderboard)")
    for quest in "Please Enter: 1 = User 1, 2 = User 2 3 = User 3\nTo confirm who is taking the quiz":
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        confirm_e_easy = input("")
        if confirm_e_easy == "1":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname1))
            with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname1) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_list.txt', 'a') as add_scores:
                add_scores.write("\n\nComputer Science:\n")
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e))
            with open('Leaderboard_list_store_computer_science_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e) + '\n')
            for quest in "Going To User Select!\n":     #Remember to have an option to allow the user to select the difficulty above or it returns them to user select
                sys.stdout.write(quest)                 #Add after adding Medium Difficulty Computer Science
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            time.sleep(1)
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "2":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname2))
            with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname2) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname2) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_list.txt', 'a') as add_scores:
                add_scores.write("\n\nComputer Science:\n")
                add_scores.write("{0}, Score is- ".format(coolname2) + str(score_e))
            with open('Leaderboard_list_store_computer_science_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname2) + str(score_e) + '\n')
            for quest in "Going To User Select\n":
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            time.sleep(1)
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "3":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname3))
            with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname3) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname3) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_list.txt', 'a') as add_scores:
                add_scores.write("\n\nComputer Science:\n")
                add_scores.write("{0}, Score is- ".format(coolname3) + str(score_e))
            with open('Leaderboard_list_store_computer_science_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname3) + str(score_e) + '\n')
            for quest in "Going To User Select\n":
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            time.sleep(1)
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-3")
            quiz_ok = False
        
def computer_science_quiz_medium(coolname1,coolname2,coolname3):    
    score_e = 0
    score_e_percentage = 0
    for quest in "\nEach correct answer is 10 points\nEach incorrect answer is negative 10 points\nYou will also gain a percentage and grade in the external text file\n":
        sys.stdout.write(quest)
        sleep(0.04)
    sys.stdout.write('\r')
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_1.txt", "r" ) as e_easy_quiz_1:
        e_questions_1 = e_easy_quiz_1.read().splitlines()
    for eachLine in e_questions_1:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_1_easy = input("Input 1-2 ")
        if e_answers_1_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        elif e_answers_1_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        else:
            print("\nPlease enter a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_2_easy = input("Input 1-2 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_2_easy = input("Input 1-2 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_2_easy = input("Input 1-2 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\computer_science_quiz\computer_science_easy\computer_science_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
        sleep(1.1)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_2_easy = input("Input 1-2 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\computer_science_quiz\computer_science_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open('Computer Science\'s Easy Quiz Results!.txt', 'w') as score_variable:
        score_variable.write("Final results below! (Any Latest Scores go to the Leaderboard)")
    for quest in "Please Enter: 1 = User 1, 2 = User 2 3 = User 3\nTo confirm who is taking the quiz":
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        confirm_e_easy = input("")
        if confirm_e_easy == "1":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname1))
            with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname1) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_list.txt', 'a') as add_scores:
                add_scores.write("\n\nComputer Science:\n")
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e))
            with open('Leaderboard_list_store_computer_science_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e) + '\n')
            for quest in "Going To User Select!\n":     #Remember to have an option to allow the user to select the difficulty above or it returns them to user select
                sys.stdout.write(quest)                 #Add after adding Hard Difficulty Computer Science
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            time.sleep(1)
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "2":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname2))
            with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname2) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_list.txt', 'a') as add_scores:
                add_scores.write("\n\nComputer Science:\n")
                add_scores.write("{0}, Score is- ".format(coolname2) + str(score_e))
            with open('Leaderboard_list_store_computer_science_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname2) + str(score_e) + '\n')
            for quest in "Going To User Select\n":
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            time.sleep(1)
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "3":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname3))
            with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname3) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Computer Science\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_list.txt', 'a') as add_scores:
                add_scores.write("\n\nComputer Science:\n")
                add_scores.write("{0}, Score is- ".format(coolname3) + str(score_e))
            with open('Leaderboard_list_store_computer_science_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname3) + str(score_e) + '\n')
            for quest in "Going To User Select\n":
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            time.sleep(1)
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-4")
            quiz_ok = False        

def maths_quiz_easy(coolname1,coolname2,coolname3):
    score_e = 0
    score_e_percentage = 0
    for quest in "\nEach correct answer is 10 points\nEach incorrect answer is negative 10 points\nYou will also gain a percentage and grade in the external text file\n":
        sys.stdout.write(quest)
        sleep(0.04)
    sys.stdout.write('\r')
    with open("quiz_questions\maths_quiz\maths_easy\maths_easy_1.txt", "r" ) as e_easy_quiz_1:
        e_questions_1 = e_easy_quiz_1.read().splitlines()
    for eachLine in e_questions_1:
        print(eachLine)
        sleep(1.4)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_1_easy = input("Input 1-2 ")
        if e_answers_1_easy == "1":
            with open("quiz_questions\maths_quiz\maths_easy\q1_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        elif e_answers_1_easy == "2":
            with open("quiz_questions\maths_quiz\maths_easy\q2_easy_1.txt", "r", encoding='utf-8' ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\maths_quiz\maths_easy\maths_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
        sleep(1.5)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_2_easy = input("Input 1-2 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\maths_quiz\maths_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\maths_quiz\maths_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\maths_quiz\maths_easy\maths_easy_3.txt", "r" ) as e_easy_quiz_3:
        e_questions_3 = e_easy_quiz_3.read().splitlines()
    for eachLine in e_questions_3:
        print(eachLine)
        sleep(1.5)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_3_easy = input("Input 1-2 ")
        if e_answers_3_easy == "1":
            with open("quiz_questions\maths_quiz\maths_easy\q1_easy_3.txt", "r" ) as e_easy_quiz_3:
                e_questions_3 = e_easy_quiz_3.read().splitlines()
            for eachLine in e_questions_3:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        elif e_answers_3_easy == "2":
            with open("quiz_questions\maths_quiz\maths_easy\q2_easy_3.txt", "r" ) as e_easy_quiz_3:
                e_questions_3 = e_easy_quiz_3.read().splitlines()
            for eachLine in e_questions_3:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\maths_quiz\maths_easy\maths_easy_4.txt", "r" ) as e_easy_quiz_4:
        e_questions_4 = e_easy_quiz_4.read().splitlines()
    for eachLine in e_questions_4:
        print(eachLine)
        sleep(1.5)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_4_easy = input("Input 1-2 ")
        if e_answers_4_easy == "1":
            with open("quiz_questions\maths_quiz\maths_easy\q1_easy_4.txt", "r" ) as e_easy_quiz_4:
                e_questions_4 = e_easy_quiz_4.read().splitlines()
            for eachLine in e_questions_4:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        elif e_answers_4_easy == "2":
            with open("quiz_questions\maths_quiz\maths_easy\q2_easy_4.txt", "r" ) as e_easy_quiz_4:
                e_questions_4 = e_easy_quiz_4.read().splitlines()
            for eachLine in e_questions_4:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open("quiz_questions\maths_quiz\maths_easy\maths_easy_5.txt", "r" ) as e_easy_quiz_5:
        e_questions_5 = e_easy_quiz_5.read().splitlines()
    for eachLine in e_questions_5:
        print(eachLine)
        sleep(1.5)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_5_easy = input("Input 1-2 ")
        if e_answers_5_easy == "1":
            with open("quiz_questions\maths_quiz\maths_easy\q1_easy_5.txt", "r" ) as e_easy_quiz_5:
                e_questions_5 = e_easy_quiz_5.read().splitlines()
            for eachLine in e_questions_5:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 20
            quiz_ok = True
            break
        elif e_answers_5_easy == "2":
            with open("quiz_questions\maths_quiz\maths_easy\q2_easy_5.txt", "r" ) as e_easy_quiz_5:
                e_questions_5 = e_easy_quiz_5.read().splitlines()
            for eachLine in e_questions_5:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 20
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-2")
            quiz_ok = False
    with open('Maths\'s Easy Quiz Results!.txt', 'w') as score_variable:
        score_variable.write("Final results below! (Any Latest Scores go to the Leaderboard)")
    for quest in "Please Enter: 1 = User 1, 2 = User 2 3 = User 3\nTo confirm who is taking the quiz":
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        confirm_e_easy = input("")
        if confirm_e_easy == "1":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname1))
            with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname1) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_List.txt', 'a') as add_scores:
                add_scores.write("\nMaths:\n")
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e))
            with open('Leaderboard_List_store_maths_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e) + '\n')
            for quest in "Going To User Select!\n":     #Remember to have an option to allow the user to select the difficulty above or it returns them to user select
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "2":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname2))
            with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname2) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_List.txt', 'a') as add_scores:
                add_scores.write("\nMaths:\n")
                add_scores.write("{0}, Score is- ".format(coolname2) + str(score_e))
            with open('Leaderboard_List_store_maths_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname2) + str(score_e) + '\n')
            for quest in "Going To User Select\n":
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "3":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname3))
            with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname3) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= 0:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 30:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 50:
                with open('Maths\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print()
            with open('Leaderboard_List.txt', 'a') as add_scores:
                add_scores.write("\nMaths:\n")
                add_scores.write("{0}, Score is- ".format(coolname3) + str(score_e))
            with open('Leaderboard_List_store_maths_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname3) + str(score_e) + '\n')
            for quest in "Going To User Select\n":
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-3")
            quiz_ok = False

def product_design_easy(coolname1,coolname2,coolname3):
    score_e = 0
    score_e_percentage = 0
    for quest in "\nEach correct answer is 10 points\nEach incorrect answer is negative 10 points\nYou will also gain a percentage and grade in the external text file\n":
        sys.stdout.write(quest)
        sleep(0.04)
    sys.stdout.write('\r')
    with open("quiz_questions\product_design_quiz\product_design_easy\product_design_easy_1.txt", "r" ) as e_easy_quiz_1:
        e_questions_1 = e_easy_quiz_1.read().splitlines()
    for eachLine in e_questions_1:
        print(eachLine)
        sleep(1.4)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_1_easy = input("Input 1-4 ")
        if e_answers_1_easy == "1":
            with open("quiz_questions\product_design_quiz\product_design_easy\q1_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 50
            quiz_ok = True
            break
        elif e_answers_1_easy == "2":
            with open("quiz_questions\product_design_quiz\product_design_easy\q2_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        elif e_answers_1_easy == "3":
            with open("quiz_questions\product_design_quiz\product_design_easy\q3_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        elif e_answers_1_easy == "4":
            with open("quiz_questions\product_design_quiz\product_design_easy\q4_easy_1.txt", "r", encoding='utf-8' ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-3")
            quiz_ok = False
    with open("quiz_questions\product_design_quiz\product_design_easy\product_design_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
        sleep(1.5)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        e_answers_2_easy = input("Input 1-4 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\product_design_quiz\product_design_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 50
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\product_design_quiz\product_design_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 50
            quiz_ok = True
            break
        elif e_answers_2_easy == "3":
            with open("quiz_questions\product_design_quiz\product_design_easy\q3_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e + 10
            score_e_percentage = score_e_percentage + 50
            quiz_ok = True
            break
        elif e_answers_2_easy == "4":
            with open("quiz_questions\product_design_quiz\product_design_easy\q4_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_e = score_e - 10
            score_e_percentage = score_e_percentage - 50
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-3")
            quiz_ok = False
    with open('Product Design\'s Easy Quiz Results!.txt', 'w') as score_variable:
        score_variable.write("Final results below! (Any Latest Scores go to the Leaderboard)")
    for quest in "Please Enter: 1 = User 1, 2 = User 2 3 = User 3\nTo confirm who is taking the quiz":
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.write('\r')
    sys.stdout.flush()
    while True:
        confirm_e_easy = input("")
        if confirm_e_easy == "1":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname1))
            with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname1) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= -10:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 10:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 20:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print("ERROR")
            with open('Leaderboard_List.txt', 'a') as add_scores:
                add_scores.write("\nProduct Design:\n")
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e))
            with open('Leaderboard_List_store_product_design_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e) + '\n')
            for quest in "Going To User Select!\n":     #Remember to have an option to allow the user to select the difficulty above or it returns them to user select
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "2":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname1))
            with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname1) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= -10:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 10:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 20:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print("ERROR")
            with open('Leaderboard_List.txt', 'a') as add_scores:
                add_scores.write("\nProduct Design:\n")
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e))
            with open('Leaderboard_List_store_product_design_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e) + '\n')
            for quest in "Going To User Select!\n":     #Remember to have an option to allow the user to select the difficulty above or it returns them to user select
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        elif confirm_e_easy == "3":
            print("\nOkay {0}, Thanks for inputing we will save your score to external save txt document".format(coolname1))
            with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                score_variable.write("\n\n{0} score is- ".format(coolname1) + str(score_e))
                score_variable.write("\n{0} percentage is- ".format(coolname1) + str(score_e_percentage))
            int(score_e)
            if score_e <= -10:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a C")
            elif score_e <= 10:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a B")
            elif score_e <= 20:
                with open('Product Design\'s Easy Quiz Results!.txt', 'a') as score_variable:
                    score_variable.write("\nYou got a A")
            else:
                print("ERROR")
            with open('Leaderboard_List.txt', 'a') as add_scores:
                add_scores.write("\nProduct Design:\n")
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e))
            with open('Leaderboard_List_store_product_design_easy.txt', 'a') as add_scores:
                add_scores.write("{0}, Score is- ".format(coolname1) + str(score_e) + '\n')
            for quest in "Going To User Select!\n":     #Remember to have an option to allow the user to select the difficulty above or it returns them to user select
                sys.stdout.write(quest)
                sys.stdout.flush()
                sleep(0.04)
            sys.stdout.write('\r')
            sys.stdout.flush()
            places(coolname1,coolname2,coolname3)
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-3")
            quiz_ok = False

#REMEMBER MEEE, BEFORE I HAVE TO PRODUCT DESIGN.!?!

def choices(player1,player2,player3):
    difficulties = ['E','M','H','e','m','h']
    print("\nLesson Quiz choices after difficulty selections!")
    choice = input("Please pick Easy,Medium or Hard! (Input it as E,M or H) ")    #3 out of 9 Quizzes Complete
    while True:
        if choice == difficulties[0]:
            print("You picked Easy!")
            quiz_ok = True
            selection_subject = input("Please Select: Computer Science, Maths, Product Design (Input it as 1,2,3.)\n1= Computer Science\n2= Maths\n3= Product Design\n")
            if selection_subject == "1":
                print("Commencing Computer Science Quiz")
                computer_science_quiz_easy(player1,player2,player3) #Complete
            elif selection_subject == "2":
                print("Commencing Maths Quiz")
                maths_quiz_easy(player1,player2,player3) #Complete
            elif selection_subject == "3":
                print("Commencing Product Design Quiz")
                product_design_easy(player1,player2,player3) #Complete
            else:
                print("Returning to difficulties selection due to invalid selections")
                choices(player1,player2,player3)
            break
        elif choice == difficulties[1]:
            print("You picked Medium!")
            quiz_ok = True
            selection_subject = input("Please Select: Computer Science, Maths, Product Design (Input it as 1,2,3.)\n1= Computer Science\n2= Maths\n3= Product Design\n")
            if selection_subject == "1":
                print("Commencing Computer Science Quiz")
                #computer_science_quiz_medium(player1,player2,player3)
            elif selection_subject == "2":
                print("Commencing Maths Quiz")
                #maths_quiz_medium(player1,player2,player3)
            elif selection_subject == "3":
                print("Commencing Product Design Quiz")
                #product_design_medium(player1,player2,player3)
            else:
                print("Returning to difficulties selection due to invalid selections")
                choices(player1,player2,player3)
            break
        elif choice == difficulties[2]:
            print("You picked Hard!")
            quiz_ok = True
            selection_subject = input("Please Select: Computer Science, Maths, Product Design (Input it as 1,2,3.)\n1= Computer Science\n2= Maths\n3= Product Design\n")
            if selection_subject == "1":
                print("Commencing Computer Science Quiz")
                #computer_science_quiz_hard(player1,player2,player3)
            elif selection_subject == "2":
                print("Commencing Maths Quiz")
                #maths_quiz_medium_hard(player1,player2,player3)
            elif selection_subject == "3":
                print("Commencing Product Design Quiz")
                #product_design_medium_hard(player1,player2,player3)
            else:
                print("Returning to difficulties selection due to invalid selections")
                choices(player1,player2,player3)
            break
        elif choice == difficulties[3]:
            print("You picked Easy!")
            quiz_ok = True
            selection_subject = input("Please Select: Computer Science, Maths, Product Design (Input it as 1,2,3.)\n1= Computer Science\n2= Maths\n3= Product Design\n")
            if selection_subject == "1":
                print("Commencing Computer Science Quiz")
                computer_science_quiz_easy(player1,player2,player3)
            elif selection_subject == "2":
                print("Commencing Maths Quiz")
                maths_quiz_easy(player1,player2,player3)
            elif selection_subject == "3":
                print("Commencing Product Design Quiz")
                product_design_easy(player1,player2,player3)
            else:
                print("Returning to difficulties selection due to invalid selections")
                choices(player1,player2,player3)
            break
        elif choice == difficulties[4]:
            print("You picked Medium!")
            quiz_ok = True
            selection_subject = input("Please Select: Computer Science, Maths, Product Design (Input it as 1,2,3.)\n1= Computer Science\n2= Maths\n3= Product Design\n")
            if selection_subject == "1":
                print("Commencing Computer Science Quiz")
                #computer_science_quiz_medium(player1,player2,player3)
            elif selection_subject == "2":
                print("Commencing Maths Quiz")
                #maths_quiz_medium(player1,player2,player3)
            elif selection_subject == "3":
                print("Commencing Product Design Quiz")
                #product_design_medium(player1,player2,player3)
            else:
                print("Returning to difficulties selection due to invalid selections")
                choices(player1,player2,player3)
            break
        elif choice == difficulties[5]:
            print("You picked Hard!")
            quiz_ok = True
            selection_subject = input("Please Select: Computer Science, Maths, Product Design (Input it as 1,2,3.)\n1= Computer Science\n2= Maths\n3= Product Design\n")
            if selection_subject == "1":
                print("Commencing Computer Science Quiz")
                #computer_science_quiz_hard(player1,player2,player3)
            elif selection_subject == "2":
                print("Commencing Maths Quiz")
                #maths_quiz_medium_hard(player1,player2,player3)
            elif selection_subject == "3":
                print("Commencing Product Design Quiz")
                #product_design_medium_hard(player1,player2,player3)
            else:
                print("Returning to difficulties selection due to invalid selections")
                choices(player1,player2,player3)
            break
        else:
            print("Please Pick E,M or H")
            quiz_ok = False
            choices(player1,player2,player3)
            break

        
def credit():
    for quest in "\nMade by Zain Cheema ザイン・シマ\n":
        sys.stdout.write(quest)
        sys.stdout.flush()
        sleep(0.04)
    sys.stdout.flush()
    print("By The Way I'm not Japanese I just got a A* in that subject\n")
    credit_select = input("Press 1 to go back to the menu\nPress 2 to exit\nPress 3 to go to my Youtube Channel\n")
    if credit_select == "1":
        main_menu()
    elif credit_select == "2":
        sys.exit("Sayonara")
    elif credit_select == "3":
        webbrowser.open('https://www.youtube.com/channel/UC1NS-DNBiQUQGlfyjHZRMag')
        print("Returning to Main Menu")
        main_menu()
    else:
        print("Pick a valid option 1 or 2")
        credit()


def leaderboard_difficulties_computer_science():   #Copy, paste this 4 times for this and 2 subjects plus a combined leaderboard
    difficulties = ['E','M','H','e','m','h']
    while True:
        print("\nPlease select the difficulty! (E = Easy, M = Medium H = Hard)")
        leaderboard_difficulty = input("")
        if leaderboard_difficulty == difficulties[0]:
            for ultra_instinct in "\nThe Highest score for Computer Science Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_easy.txt", "r" ) as leaderboard_cs_e:
                leaderboard_easy = leaderboard_cs_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[1]:
            for ultra_instinct in "\nThe Highest score for Computer Science Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_medium.txt", "r" ) as leaderboard_cs_m:
                leaderboard_medium = leaderboard_cs_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[2]:
            for ultra_instinct in "\nThe Highest score for Computer Science Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_hard.txt", "r" ) as leaderboard_cs_h:
                leaderboard_hard = leaderboard_cs_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[3]:
            for ultra_instinct in "\nThe Highest score for Computer Science Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_easy.txt", "r" ) as leaderboard_cs_e:
                leaderboard_easy = leaderboard_cs_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[4]:
            for ultra_instinct in "\nThe Highest score for Computer Science Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_medium.txt", "r" ) as leaderboard_cs_m:
                leaderboard_medium = leaderboard_cs_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[5]:
            for ultra_instinct in "\nThe Highest score for Computer Science Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_hard.txt", "r" ) as leaderboard_cs_h:
                leaderboard_hard = leaderboard_cs_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        else:
            print("Please Pick a valid option\n")
            quiz_ok = False

def keywords():
    a_p = input("\nInput the password to access the debug mode!\n")
    if a_p == "You Know De Wae":
        print("Hello Admin\n")
        t_debug_mode()
    else:
        print("Incorrect Password, Leave\n\n")
        main_menu()
    
def leaderboard_difficulties_maths():
    difficulties = ['E','M','H','e','m','h']
    while True:
        print("\nPlease select the difficulty! (E = Easy, M = Medium H = Hard)")
        leaderboard_difficulty = input("")
        if leaderboard_difficulty == difficulties[0]:
            for ultra_instinct in "\nThe Highest score for Maths Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_easy.txt", "r" ) as leaderboard_m_e:
                leaderboard_easy = leaderboard_m_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[1]:
            for ultra_instinct in "\nThe Highest score for Maths Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_medium.txt", "r" ) as leaderboard_m_m:
                leaderboard_medium = leaderboard_m_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[2]:
            for ultra_instinct in "\nThe Highest score for Maths Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_hard.txt", "r" ) as leaderboard_m_h:
                leaderboard_hard = leaderboard_m_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[3]:
            for ultra_instinct in "\nThe Highest score for Maths Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_easy.txt", "r" ) as leaderboard_m_e:
                leaderboard_easy = leaderboard_m_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[4]:
            for ultra_instinct in "\nThe Highest score for Maths Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_medium.txt", "r" ) as leaderboard_m_m:
                leaderboard_medium = leaderboard_m_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[5]:
            for ultra_instinct in "\nThe Highest score for Maths Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_hard.txt", "r" ) as leaderboard_m_h:
                leaderboard_hard = leaderboard_m_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        else:
            print("Please Pick a valid option\n")
            quiz_ok = False

def leaderboard_difficulties_product_design():
    difficulties = ['E','M','H','e','m','h']
    while True:
        print("\nPlease select the difficulty! (E = Easy, M = Medium H = Hard)")
        leaderboard_difficulty = input("")
        if leaderboard_difficulty == difficulties[0]:
            for ultra_instinct in "\nThe Highest score for Product Design Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_easy.txt", "r" ) as leaderboard_pd_e:
                leaderboard_easy = leaderboard_pd_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[1]:
            for ultra_instinct in "\nThe Highest score for Product Design Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_medium.txt", "r" ) as leaderboard_pd_m:
                leaderboard_medium = leaderboard_pd_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[2]:
            for ultra_instinct in "\nThe Highest score for Product Design Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_hard.txt", "r" ) as leaderboard_pd_h:
                leaderboard_hard = leaderboard_pd_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[3]:
            for ultra_instinct in "\nThe Highest score for Product Design Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_easy.txt", "r" ) as leaderboard_pd_e:
                leaderboard_easy = leaderboard_pd_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[4]:
            for ultra_instinct in "\nThe Highest score for Product Design Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_medium.txt", "r" ) as leaderboard_pd_m:
                leaderboard_medium = leaderboard_pd_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[5]:
            for ultra_instinct in "\nThe Highest score for Product Design Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_hard.txt", "r" ) as leaderboard_pd_h:
                leaderboard_hard = leaderboard_pd_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        else:
            print("Please Pick a valid option\n")
            quiz_ok = False


def leaderboard_difficulties_all():
    difficulties = ['E','M','H','e','m','h']
    while True:
        print("\nPlease select the difficulty! (E = Easy, M = Medium H = Hard)")
        leaderboard_difficulty = input("")
        if leaderboard_difficulty == difficulties[0]:
            for ultra_instinct in "\nThe Highest score for Computer Science Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_easy.txt", "r" ) as leaderboard_cs_e:
                leaderboard_easy = leaderboard_cs_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Maths Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_easy.txt", "r" ) as leaderboard_m_e:
                leaderboard_easy = leaderboard_m_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Product Design Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_easy.txt", "r" ) as leaderboard_pd_e:
                leaderboard_easy = leaderboard_pd_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[1]:
            for ultra_instinct in "\nThe Highest score for Computer Science Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_medium.txt", "r" ) as leaderboard_cs_m:
                leaderboard_medium = leaderboard_cs_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Maths Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_medium.txt", "r" ) as leaderboard_m_m:
                leaderboard_medium = leaderboard_m_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Product Design Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_medium.txt", "r" ) as leaderboard_pd_m:
                leaderboard_medium = leaderboard_pd_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[2]:
            for ultra_instinct in "\nThe Highest score for Computer Science Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_hard.txt", "r" ) as leaderboard_cs_h:
                leaderboard_hard = leaderboard_cs_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Maths Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_hard.txt", "r" ) as leaderboard_m_h:
                leaderboard_hard = leaderboard_m_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Product Design Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_hard.txt", "r" ) as leaderboard_pd_h:
                leaderboard_hard = leaderboard_pd_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[3]:
            for ultra_instinct in "\nThe Highest score for Computer Science Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_easy.txt", "r" ) as leaderboard_cs_e:
                leaderboard_easy = leaderboard_cs_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Maths Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_easy.txt", "r" ) as leaderboard_m_e:
                leaderboard_easy = leaderboard_m_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Product Design Easy Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_easy.txt", "r" ) as leaderboard_pd_e:
                leaderboard_easy = leaderboard_pd_e.read().splitlines()
            for eachLine in leaderboard_easy:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[4]:
            for ultra_instinct in "\nThe Highest score for Computer Science Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_medium.txt", "r" ) as leaderboard_cs_m:
                leaderboard_medium = leaderboard_cs_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Maths Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_medium.txt", "r" ) as leaderboard_m_m:
                leaderboard_medium = leaderboard_m_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Product Design Medium Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_medium.txt", "r" ) as leaderboard_pd_m:
                leaderboard_medium = leaderboard_pd_m.read().splitlines()
            for eachLine in leaderboard_medium:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        elif leaderboard_difficulty == difficulties[5]:
            for ultra_instinct in "\nThe Highest score for Computer Science Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_computer_science_hard.txt", "r" ) as leaderboard_cs_h:
                leaderboard_hard = leaderboard_cs_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Maths Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_maths_hard.txt", "r" ) as leaderboard_m_h:
                leaderboard_hard = leaderboard_m_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            for ultra_instinct in "\nThe Highest score for Product Design Hard Quiz\n":
                sys.stdout.write(ultra_instinct)
                sys.stdout.flush()
                sleep(0.035)
            sys.stdout.flush()
            with open("Leaderboard_list_store_product_design_hard.txt", "r" ) as leaderboard_pd_h:
                leaderboard_hard = leaderboard_pd_h.read().splitlines()
            for eachLine in leaderboard_hard:
                print(eachLine)
                sleep(1.1)
            sys.stdout.write('\r')
            sys.stdout.flush()
            quiz_ok = True
            break
        else:
            print("Please Pick a valid option\n")
            quiz_ok = False


#Only Debug Procedures

def t_debug_mode(): #Debug Mode
    for hacks in "What part of the code do you want to go to?\n":
        sys.stdout.write(hacks)
        sys.stdout.flush()
        sleep(0.045)
    sys.stdout.flush()
    print("1) Main Menu\n2) Quizzes\n3) Exit")
    debug_input = input("I choose - ")
    if debug_input == "1":
        main_menu()
    elif debug_input == "2":
        quiz_selection()
    elif debug_input == "3":
        sys.exit("Matane")
    else:
        print("Wrong Value\n\n")
        t_debug_mode()


def keywords():
    a_p = input("\nInput the password to access the debug mode!\n")
    if a_p == "You Know De Wae":
        print("Hello Admin\n")
        t_debug_mode()
    else:
        print("Incorrect Password, Leave\n\n")
        main_menu()


def quiz_selection(): #Only used in Debug Mode
    while True:
        a = ("Uganda Knuckles") #Names for Debug Mode
        b = ("Da Queen")
        c = ("Horitsu")
        which_quiz = input("\nSelect a Quiz (1,2,3,4,5,6,7,8,9)\n") #1 = Computer_Science_Easy
        if which_quiz == "1":
            computer_science_quiz_easy(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "2":
            computer_science_quiz_medium(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "3":
            computer_science_quiz_hard(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "4":
            maths_quiz_easy(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "5":
            maths_quiz_medium(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "6":
            maths_quiz_hard(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "7":
            product_design_quiz_easy(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "8":
            product_design_quiz_medium(a,b,c)
            debug_ok = True
            break
        elif which_quiz == "9":
            product_design_quiz_hard(a,b,c)
            debug_ok = True
            break
        else:
            print("Retry")
            debug_ok = False

def debug_mode(): #Last Debug Procedure
    keywords()


def leaderboard():
    for ultra_instinct in "\nWelcome To Leaderboards!\nHere we allow users to read their score and show who got the highest score!\nYou get to pick between all 3 subjects or\nHave them Together!":
        sys.stdout.write(ultra_instinct)
        sys.stdout.flush()
        sleep(0.03)
    sys.stdout.flush()
    while True:
        leaderboard_choices = input("\n1 = Computer Science, 2 = Maths, 3 = Product Design, 4 = All Subjects\n")
        if leaderboard_choices == "1":
            leaderboard_difficulties_computer_science()
            time.sleep(2)
            print("\nGoing back to menu\n")
            main_menu()
            quiz_ok = True
            break
        elif leaderboard_choices == "2":
            leaderboard_difficulties_maths()
            time.sleep(2)
            print("\nGoing back to menu\n")
            main_menu()
            quiz_ok = True
            break
        elif leaderboard_choices == "3":
            leaderboard_difficulties_product_design()
            time.sleep(2)
            print("\nGoing back to menu\n")
            main_menu()
            quiz_ok = True
            break
        elif leaderboard_choices == "4":
            leaderboard_difficulties_all()
            time.sleep(2)
            print("\nGoing back to menu\n")
            main_menu()
            quiz_ok = True
            break
        else:
            print("Pick a valid option 1-4")
            quiz_ok = False
    

def demo():
    score_g = 0
    score_percentage_g = 0
    print("\nHi, welcome to a demo version of this quiz,\nyou get to do one quiz from this code as a tryout")
    a = ("Guest")
    print("\nEach correct answer is 10 points\nEach inccorect answer is negative 10 points\n")
    with open("quiz_questions\maths_quiz\maths_easy\maths_easy_1.txt", "r" ) as e_easy_quiz_1:
        e_questions_1 = e_easy_quiz_1.read().splitlines()
    for eachLine in e_questions_1:
        print(eachLine)
    while True:
        e_answers_1_easy = input("Input 1-4 ")
        if e_answers_1_easy == "1":
            with open("quiz_questions\maths_quiz\maths_easy\q1_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            score_g = score_g + 10
            score_percentage_g = score_percentage_g + 50
            quiz_ok = True
            break
        elif e_answers_1_easy == "2":
            with open("quiz_questions\maths_quiz\maths_easy\q2_easy_1.txt", "r", encoding='utf-8' ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        elif e_answers_1_easy == "3":
            with open("quiz_questions\maths_quiz\maths_easy\q3_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        elif e_answers_1_easy == "4":
            with open("quiz_questions\maths_quiz\maths_easy\q4_easy_1.txt", "r" ) as e_easy_quiz_1:
                e_questions_1 = e_easy_quiz_1.read().splitlines()
            for eachLine in e_questions_1:
                print(eachLine)
            print('')
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-3")
            quiz_ok = False
    with open("quiz_questions\maths_quiz\maths_easy\maths_easy_2.txt", "r" ) as e_easy_quiz_2:
        e_questions_2 = e_easy_quiz_2.read().splitlines()
    for eachLine in e_questions_2:
        print(eachLine)
    while True:
        e_answers_2_easy = input("Input 1-4 ")
        if e_answers_2_easy == "1":
            with open("quiz_questions\maths_quiz\maths_easy\q1_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_g = score_g - 10
            quiz_ok = True
            break
        elif e_answers_2_easy == "2":
            with open("quiz_questions\maths_quiz\maths_easy\q2_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_g = score_g - 10
            quiz_ok = True
            break
        elif e_answers_2_easy == "3":
            with open("quiz_questions\maths_quiz\maths_easy\q3_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_g = score_g + 10
            score_percentage_g = score_percentage_g + 50
            quiz_ok = True
            break
        elif e_answers_2_easy == "4":
            with open("quiz_questions\maths_quiz\maths_easy\q4_easy_2.txt", "r" ) as e_easy_quiz_2:
                e_questions_2 = e_easy_quiz_2.read().splitlines()
            for eachLine in e_questions_2:
                print(eachLine)
            print('')
            score_g = score_g - 10
            quiz_ok = True
            break
        else:
            print("\nInput a valid option 1-3")
            quiz_ok = False
    your_score = print("{0}\'s Score is- ".format(a) + str(score_g))
    your_percentage = print("{0}\'s Percentage is- ".format(a) + str(score_percentage_g) + ("%"))
    int(score_g)
    if score_g <= -10:
        print("You got a C バカ!")
    elif score_g <= 10:
        print("You got a B すばらしよ！")
    elif score_g <= 20:
        print("You got a A すげ！")    
    time.sleep(5)
    print("Returning To Menu\n")
    main_menu()
    
def user_select_main():
    print("\nUser Please select the following options- ")
    print("1) Only 1 User takes the quiz!")
    print("2) Only 2 Users take the quiz!") 
    print("3) All Users take the quiz!")
    print("4) Or return to main menu")
    print("Invaild or No Input returns you to the menu")
    user_select_choice = input("Select 1-4 ")
    if user_select_choice == "1":
        main_quiz_1()
    elif user_select_choice == "2":
        main_quiz_2()
    elif user_select_choice == "3":
        main_quiz_all()
    elif user_select_choice == "4":
        main_menu()
    else:
        main_menu()
    
def main_quiz_all():  
    file_intro()
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_1, u_username_1 = username_and_password_file_1(user_name, age, year_group, u_username, password)
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_2, u_username_2 = username_and_password_file_2(user_name, age, year_group, u_username, password)
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_3, u_username_3 = username_and_password_file_3(user_name, age, year_group, u_username, password)
    places(u_username_1, u_username_2, u_username_3)
    choices(u_username_1, u_username_2, u_username_3)

def main_quiz_1():
    file_intro()
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_1, u_username_1 = username_and_password_file_1(user_name, age, year_group, u_username, password)
    u_username_2, u_username_3 = spare_user_2()
    choices(u_username_1, u_username_2, u_username_3)

def main_quiz_2():
    file_intro()
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_1, u_username_1 = username_and_password_file_1(user_name, age, year_group, u_username, password)
    user_name, age, year_group, u_username = user_register()
    password = validate()
    user_name_2, u_username_2 = username_and_password_file_2(user_name, age, year_group, u_username, password)
    u_username_3 = spare_user_1()
    places(u_username_1, u_username_2, u_username_3)
    choices(u_username_1, u_username_2, u_username_3)

def main_menu():
    for schezwan_sauce in "Welcome To Main Menu, Please pick a option below to start the program\n":
        sys.stdout.write(schezwan_sauce)
        sys.stdout.flush()
        sleep(0.03)
    sys.stdout.flush()
    for schezwan_sauce in "1) Start Quiz\n":
        sys.stdout.write(schezwan_sauce)
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.flush()
    for schezwan_sauce in "2) Skip Students Sign Up and take a Demo (Requires 1 user, Taster)\n":
        sys.stdout.write(schezwan_sauce)
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.flush()
    for schezwan_sauce in "3) Leaderboard (Anyone can view)\n":
        sys.stdout.write(schezwan_sauce)
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.flush()
    for schezwan_sauce in "4) Debug Mode (ADMIN ONLY)\n":
        sys.stdout.write(schezwan_sauce)
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.flush()
    for schezwan_sauce in "5) Credits\n":
        sys.stdout.write(schezwan_sauce)
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.flush()
    for schezwan_sauce in "6) Exit\n":
        sys.stdout.write(schezwan_sauce)
        sys.stdout.flush()
        sleep(0.02)
    sys.stdout.flush()
    select_please = input("Please select option 1-6 ")
    if select_please == "1":                                   
        user_select_main()
    elif select_please == "2":
        demo() 
    elif select_please == "3":
        leaderboard() 
    elif select_please == "4":
        debug_mode() 
    elif select_please == "5":
        credit() 
    elif select_please == "6":
        sys.exit("Goodbye") #Putting text within the sys.exit is not significant or needed. I just like it there, personal perference  
    else:
        print("Pick a valid option 1-6\n")
        main_menu()



def main(): 
    main_menu()
main()
#Temp Way to mess with the quiz without needing to go through the long way. Also Future Zain (SAVE THE FUTURE) add a debug mode to menu :)
#file_intro()
#u_username_1, u_username_2, u_username_3 = temp()
#computer_science_quiz_easy(u_username_1, u_username_2, u_username_3) 
#choices(u_username_1, u_username_2, u_username_3)
