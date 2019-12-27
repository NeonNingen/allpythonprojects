import os
import subprocess
from pytube import YouTube

def music():
	user_input = input("Input the youtube url: ")
	data = YouTube(user_input)
	for i in data.streams.all():
		print(i)

	song = data.streams.filter(only_audio=True).first()
	parent_dir = "C:/Users/Zain/Music/YT"
	song.download(parent_dir)

	new_filename = input("Enter filename (including extension): ")

	default_filename = song.default_filename  
	subprocess.call([                               
    	'ffmpeg',
    	'-i', os.path.join(parent_dir, default_filename), 
    	os.path.join(parent_dir, new_filename)
	])

	print("Finished, Enjoy!")