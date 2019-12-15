import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=So54Khf7bB8")

vids= yt.streams.all()
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("Pick a stream: "))

parent_dir = "C:/Users/Zain/Videos/YT"
vids[vnum].download(parent_dir)
print('Complete!')