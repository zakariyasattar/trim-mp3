from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

song_data = [
    ["00:00", "Mike Noise", "Low Earth Orbit"],
    03:26 SHAP3S - Swell
    06:17 Shortwire - Reconfig
    09:59 DOOMROAR - Sagittarius (Ft. ALISON)
    13:37 Com Truise - Hyperlips
    18:18 Emil Rottmayer - Descend
    22:26 DOOMROAR - The Discovery (Ft. Krosia)
    26:20 HOME - I See You
    29:02 Unnamed - Sundown
    30:59 Emil Rottmayer - K.E.Y.S
    35:00 HOME - Billiards
    37:56 Mitch Murder - Mirage
]

for data in song_data:
    previous_end_time = 
    ffmpeg_extract_subclip("cybercity.mp3", convertToMilli(data[0]), 60, targetname = data[2] + ".mp3")
