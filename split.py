from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from mutagen.easyid3 import EasyID3
import os

path_to_mp3 = "cybercity.mp3"

song_data = [
    ["00:00", "Mike Noise", "Low Earth Orbit"],
    ["03:26", "SHAP3S", "Swell"],
    ["06:17", "Shortwire", "Reconfig"],
    ["09:59", "DOOMROAR", "Sagittarius"],
    ["13:37", "Com Truise", "Hyperlips"],
    ["18:18", "Emil Rottmayer", "Descend"],
    ["22:26", "DOOMROAR", "The Discovery"],
    ["26:20", "HOME", "I See You"],
    ["29:02", "Unnamed", "Sundown"],
    ["30:59", "Emil Rottmayer", "K.E.Y.S"],
    ["35:00", "HOME", "Billiards"],
    ["37:56", "Mitch Murder", "Mirage"]
]

def convertToSecs(time):
    breakdown = time.split(":")
    return (int(breakdown[0]) * 60) + int(breakdown[1])

def addMetadata():
    with os.scandir("results") as it:
        for entry in it:
            if entry.name.endswith(".mp3") and entry.is_file():
                audio = EasyID3(entry.path)

                for y in range(len(song_data)):
                    if(song_data[y][2] == entry.name.split(".")[0]):
                        audio['title'] = song_data[y][2]
                        print(entry.path + " = " + song_data[y][2])
                        audio['artist'] = song_data[y][1]
                audio.save()

for x in range(len(song_data)):
    data = song_data[x]

    if(x+1 >= len(song_data)):
        nextEnd = convertToSecs("42:17")
    else:
        nextEnd = convertToSecs(song_data[x+1][0])

    ffmpeg_extract_subclip(path_to_mp3, convertToSecs(data[0]), nextEnd, targetname = "results/" + data[2] + ".mp3")

addMetadata()
# TODO:

# DONE:
# format all song_data data
# write convertToSecs function
# add function to edit metadata of mp3 to add artist (data[1])
