from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

ffmpeg_extract_subclip("audio.mp3", 0, 60, targetname="result/shorter_audio.mp3")
