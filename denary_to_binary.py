def display():
	user_input = float(input("Enter a denary value: "))
	denarytobinary(user_input)


def denarytobinary(user_input):
	if user_input > 1:
		denarytobinary(user_input // 2)
	print(user_input % 2, end='')


def main():
	display()

main()
