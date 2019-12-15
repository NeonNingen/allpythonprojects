import os
import sys
music_ok = False
from time import sleep


for c in "Welcome To Python Music Menu 1.0...(C++ Version is at 4.5.0)":
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.04)
sys.stdout.write('\n')
sys.stdout.flush()

def inuyashiki_1():
    os.system("start e:\Inuyashiki_-_My_Hero_-_MAN_WITH_A_MISSION.wav")
    
def melty_blood_2():
    os.system("start e:\Melty Blood Actress Again OST - Blood Drain.wav")

def coldplay_3():
    os.system("start e:\Coldplay_-_Clocks.wav")

def all_songs_4():
    os.system("start e:\Inuyashiki_-_My_Hero_-_MAN_WITH_A_MISSION.wav")
    os.system("start e:\Melty Blood Actress Again OST - Blood Drain.wav")
    os.system("start e:\Coldplay_-_Clocks.wav")

def inuyashiki_1_1():
    print("\nDo you want to play the song or Exit")
    option_1 = input("\n1) Play the song"
                     "\n2) Exit Program\n\n")
    if option_1 == "1":
        inuyashiki_1()
    elif option_1 == "2":
        print("Exiting")
        sys.exit()
    else:
        print("Invalid Choice, Pick from option 1-2")
        inuyashiki_1_1()
    

def melty_blood_1_2():
    print("\nDo you want to play the song or Exit")
    option_1 = input("\n1) Play the song"
                     "\n2) Exit Program\n\n")
    if option_1 == "1":
        melty_blood_2()
    elif option_1 == "2":
        print("Exiting")
        sys.exit()
    else:
        print("Invalid Choice, Pick from option 1-2")
        melty_blood_1_2()

    
def main():
    print("Pick option 1 - 5 (Still Fixing Infinte Loops)")
    choice = [" Inuyashiki"," Melty Blood"," ColdPlay"," All Songs"," Exit"]
    option = input("\n1) Inuyashiki: My Hero"
                   "\n2) Melty Blood: Blood Drain"
                   "\n3) Coldplay Clocks"
                   "\n4) All songs"
                   "\n5) Exit Program\n\n")
    while (music_ok == False):
        if option == "1":
          print("You chose" + "" + choice[0])
          inuyashiki_1_1()
          break
        elif option == "2":
          print("You chose" + "" + choice[1])
          melty_blood_1_2()
          break
        elif option == "3":
          print("You chose" + "" + choice[2])
          break
        elif option == "4":
          print("You chose" + "" + choice[3])
          all_songs_4()
          break
        elif option == "5":
          print("You chose" + "" + choice[4])
          print("See Ya!")
          sys.exit()
          break
        else:
            print("Invalid Choice, Pick from option 1-5")
            main()

main()

