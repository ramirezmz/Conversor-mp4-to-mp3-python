from moviepy.editor import *
mp4_file = "1.mp4"

mp3_file = "audio.mp3"

videoClip = VideoFileClip(mp4_file)

audioclip = videoClip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

videoClip.close()
