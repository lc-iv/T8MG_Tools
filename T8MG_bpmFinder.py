# T8MG.io BPM Finder
# e-mail: louismconley@gmail.com

import librosa as lb
import pyttsx3


# Create path variable pointing to where you file.wav is located
audio_path  = 'drvive:path/to/file.wav'
# Create audio engine for talk back
engine      = pyttsx3.init()

# Load file.wav with at a sample rate of 44.1 khz (Album Quality)
y, sr       = lb.load(audio_path, sr=44100)

# Analyze audio transients to find pace of overall audio (bpm's)
onset_env   = lb.onset.onset_strength(y, sr=sr)
tempo       = lb.beat.tempo(onset_envelope=onset_env, sr=sr)
tempo       = int(tempo)
response    = 'The track speed is ' + str(tempo) + ' beats per minute.'

engine.say(response, 'en')
engine.runAndWait()

# Print results!
print(response)




