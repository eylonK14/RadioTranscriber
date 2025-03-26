from pydub import AudioSegment

AudioSegment.from_wav("/home/eylon/gqrx_20250326_165603_97500000.wav").export("/home/eylon/gqrx_20250326_165603_97500000.mp3", format="mp3")
