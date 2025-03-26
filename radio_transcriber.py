import sys
import os
import whisper
from pydub import AudioSegment
import ntpath


# Check for input argument
if len(sys.argv) < 2:
    print("Usage: python transcribe_radio.py <path_to_wav_file>")
    sys.exit(1)
    
# Get MP3 file path from argv
audio_path = sys.argv[1]
    
# Check if file exists
if not os.path.isfile(audio_path):
    print(f"File not found: {audio_path}")
    sys.exit(1)
    
if not sys.argv[1].endswith(".wav") < 2:
    print("File must be WAV!")
    sys.exit(1)

# Get filname from path
file_name = ntpath.basename(audio_path).removesuffix(".wav")

# Convert file from MP3 to WAV
AudioSegment.from_wav(audio_path).export(f"{file_name}.mp3", format="mp3")

# Load Whisper model
model = whisper.load_model("turbo")

# Transcribe
print(f"Transcribing: {audio_path}")
result = model.transcribe(audio_path)
text = result["text"]

# Create output path with .txt extension
base_name = os.path.splitext(os.path.basename(audio_path))[0]
output_path = f"{base_name}.txt"

# Write to file
with open(output_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Transcription saved to: {output_path}")
