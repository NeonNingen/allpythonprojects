from pygame import *
import sys
music_ok = False
from time import sleep


for c in "Welcome To Pygame Python Music Menu 1.0...(C++ Version is at 4.5.0)":
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep(0.04)
sys.stdout.write('\n')
sys.stdout.flush()

def inuyashiki_1():
    print("Now Playing, 'Inuyashiki: My Hero' ")
    mixer.init()
    mixer.music.load('Inuyashiki_-_My_Hero_-_MAN_WITH_A_MISSION.wav')
    mixer.music.play()
    
def melty_blood_2():
    print("Now Playing, 'Melty Blood: Blood Drain' ")
    mixer.init()
    mixer.music.load('Melty Blood Actress Again OST - Blood Drain.wav')
    mixer.music.play()

def coldplay_3():
    print("Now Playing, 'Coldplay Clocks' ")
    mixer.init()
    mixer.music.load('Coldplay_-_Clocks.wav')
    mixer.music.play()

def all_songs_4():
    mixer.init()
    mixer.music.load('Inuyashiki_-_My_Hero_-_MAN_WITH_A_MISSION.wav')
    mixer.music.play()
    mixer.init()
    mixer.music.load('Melty Blood Actress Again OST - Blood Drain.wav')
    mixer.music.play()
    mixer.init()
    mixer.music.load('Coldplay_-_Clocks.wav')
    mixer.music.play()

def inuyashiki_1_1():
    print("Do you want to play the song or Exit")
    option_1 = input("\n1) Play the song"
                     "\n2) Exit Program\n\n")
    if option_1 == "1":
        inuyashiki_1()
        main()
    elif option_1 == "2":
        print("Exiting")
        sys.exit()
    else:
        print("Invalid Choice, Pick from option 1-2")
        inuyashiki_1_1()
    

def melty_blood_1_2():
    print("Do you want to play the song or Exit")
    option_1 = input("\n1) Play the song"
                     "\n2) Exit Program\n\n")
    if option_1 == "1":
        melty_blood_2()
        main()
    elif option_1 == "2":
        print("Exiting")
        sys.exit()
    else:
        print("Invalid Choice, Pick from option 1-2")
        melty_blood_1_2()

def coldplay_1_3():
    print("Do you want to play the song or Exit")
    option_1 = input("\n1) Play the song"
                     "\n2) Exit Program\n\n")
    if option_1 == "1":
        coldplay_3()
        main()
    elif option_1 == "2":
        print("Exiting")
        sys.exit()
    else:
        print("Invalid Choice, Pick from option 1-2")
        coldplay_1_3()

    
def main():
    print("\nPick option 1 - 5 (Still Fixing Infinte Loops)")
    choice = [" Inuyashiki"," Melty Blood"," Coldplay"," All Songs"," Exit"]
    option = input("\n1) Inuyashiki: My Hero"
                   "\n2) Melty Blood: Blood Drain"
                   "\n3) Coldplay Clocks"
                   "\n4) All songs"
                   "\n5) Exit Program\n")
    while (music_ok == False):
        if option == "1":
          print("\nYou chose" + "" + choice[0])
          inuyashiki_1_1()
          break
        elif option == "2":
          print("\nYou chose" + "" + choice[1])
          melty_blood_1_2()
          break
        elif option == "3":
          print("\nYou chose" + "" + choice[2])
          coldplay_1_3()
          break
        elif option == "4":
          print("\nYou chose" + "" + choice[3])
          all_songs_4()
          break
        elif option == "5":
          print("\nYou chose" + "" + choice[4])
          print("See Ya!")
          sys.exit()
          break
        else:
            print("\nInvalid Choice, Pick from option 1-5")
            main()

main()


