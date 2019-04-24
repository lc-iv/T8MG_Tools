# T8MG.io BPM Finder
# e-mail: louismconley@gmail.com

import librosa as lb

# Create path variable pointing to where you file.wav is located
audio_path = 'drvive:path/to/file.wav

# Load file.wav with at a sample rate of 44.1 khz (Album Quality)
y, sr = lb.load(audio_path, sr=44100)

# Analyze audio transients to find pace of overall audio (bpm's)
onset_env = lb.onset.onset_strength(y, sr=sr)
tempo = lb.beat.tempo(onset_envelope=onset_env, sr=sr)
tempo = int(tempo)

# Print results!
print('The track speed is ' + str(tempo) + ' beats per minutes.')




