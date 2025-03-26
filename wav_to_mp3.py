from pydub import AudioSegment

AudioSegment.from_wav("/input/file.wav").export("/output/file.mp3", format="mp3")