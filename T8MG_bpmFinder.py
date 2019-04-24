# T8MG.io BPM Finder
# iamkinglouisiv@gmail.com

import librosa as lb

audio_path = 'drvive:path/to/file.wav

y, sr = lb.load(audio_path, sr=44100)

onset_env = lb.onset.onset_strength(y, sr=sr)
tempo = lb.beat.tempo(onset_envelope=onset_env, sr=sr)
tempo = int(tempo)

print('The track speed is ' + str(tempo) + ' beats per minutes.')




