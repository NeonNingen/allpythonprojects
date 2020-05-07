import os
import sys
music_ok = False
from time import sleep


for c in "Welcome To Python Music Menu 1.0...(C++ Version is at 3.9.1)":
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.04)
sys.stdout.write('\n')
sys.stdout.flush()

def main():
    print("Pick option 1 - 5 (Includes Infinte Loops!)")
    choice = [" Inuyashiki"," Melty Blood"," ColdPlay"," All Songs"," Exit"]
    option = input("\n1) Inuyashiki: My Hero"
                   "\n2) Melty Blood: Blood Drain"
                   "\n3) Coldplay Clocks"
                   "\n4) All songs"
                   "\n5) Exit Program\n")
    while (music_ok == False):
        if option == "1":
            print ("You chose" + choice[0])
            break
        elif option == "2":
            print ("You chose" + choice[1])
            break
        elif option == "3":
            print ("You chose" + choice[2])
            break
        elif option == "4":
            print ("You chose" + choice[3])
            break
        elif option == "5":
            print ("You chose" + choice[4])
            break


main()

os.system("start e:\Inuyashiki_-_My_Hero_-_MAN_WITH_A_MISSION.wav")
