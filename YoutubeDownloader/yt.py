import sys
from music import music
from video import video

def menu_retry():
	print("Would you like to return to the menu?")
	while True:
		user_input = input("Would you return? Y or E: ")
		if user_input == "Y" or user_input == "y":
			print("Returning!")
			break
		elif user_input == "E" or user_input == "e":
			print("Goodbye")
			sys.exit()
			break
		else:
			print("Please try again!")


print("""Welcome to the YouTube Converter!
Please select one of the options below:
1) Music Conversion
2) Video Conversion
3) Exit""")


while True:
	user_input = input("Select an option: ")

	if user_input == "1":
		print("Moving to Music Converter")
		music()
		menu_retry()
		print("Welcome back!")
	elif user_input == "2":
		print("Moving to Video Converter")
		video()
		menu_retry()
		print("Welcome back!")
	elif user_input == "3":
		print("Goodbye!")
		sys.exit()
		break
	else:
		print("Please try again!")

