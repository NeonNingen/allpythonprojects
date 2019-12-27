import pytube

def video():
	user_input = input("Enter a YouTube url: ")
	yt = pytube.YouTube(user_input)

	vids= yt.streams.all()
	for i in range(len(vids)):
		print(i,'. ',vids[i])

	vnum = int(input("Pick a stream: "))
	parent_dir = "C:/Users/Zain/Videos/YT"
	vids[vnum].download(parent_dir)
	print('Complete!')