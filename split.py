from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from mutagen.easyid3 import EasyID3
import os

path_to_mp3 = "cybercity.mp3"

song_data = [
    ["0:00", "Fantom '87", "Pay Phone"]
    ["5:50", "Chris Keya", "Hotlines"]
    ["9:00", "Ferus Melek", "Octoparis"]
    ["12:26", "H A G H O R R O R", "Machine Talk"]
    ["18:45", "Jeremiah Kane", "Capri Rage"]
    ["23:22", "Straplocked", "Fast Drop"]
    ["27:02", "SIDE SCROLLER", "VGA Nights"]
    ["32:35", "Alex Vith", "Technical Liturgy"]
    ["39:06", "Zane Alexander", "V o i d"]
    ["43:00", "Retouch", "Alighting"]
    ["45:10", "ZAYAZ", "Elegia"]
    ["48:25", "LɅNights", "Outlands"]
    ["51:00", "CJ Burnett", "West Side Drive"]
    ["54:16", "SCAR", "Resistance"]
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
