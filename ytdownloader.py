from pytube import YouTube, Playlist

# jaką playlistę pobrać
my_playlist = Playlist(input("wklej link do playlisty: "))  # to jest lista z linkami do filmików

# od jakiego numeru zacząć pobierać
start_numering_from = int(input("od którego numeru zacząć numerować: "))

# gdzie zapisać plik
folder_name = input("do jakiego folderu zapisać plik: ")
if folder_name == "":
    path = "E:/YouTube"
else:
    path = "E:/YouTube/" + folder_name

# wykonaj operacje na kazdym video z playlisty
idx = 0
for video_url in my_playlist:
    idx += 1
    yt_video = YouTube(video_url)  # tworzę obiekt yt_video, na którym będę potem działać

    # pod jaką nazwą zapisać plik
    new_filename = ("000" + str(start_numering_from))[-3:] + " " + yt_video.title
    print("pobieram plik numer:", idx, new_filename)
    start_numering_from += 1

    # pobierz plik o nowej nazwie do lokalizacji path
    yt_video.streams.get_by_itag(18).download(filename=new_filename, output_path=path)
    # itag może  być 18 (360p) lub 22 (720p) lub 140(audio)
