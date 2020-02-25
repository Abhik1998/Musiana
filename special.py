import os
import subprocess
import ast
import utils.utilities as util
import random

dictStr = os.popen(
    'bash -c "python audioAnalysis.py classifyFolder -i /mnt/e/test5/ --model svm --classifier models/svmGenreRecog '
    '--details | tee /dev/stderr | grep {*}"').read()

dictdict = ast.literal_eval(dictStr)

import emotions 

emotion_mode = emotions.emotion_mode

print("\nChoosing a song for "+ emotion_mode + " mood")              # print the value of emotion_mode from emotions.py

songs = []                          

for song, genre in dictdict.items():          
    if emotion_mode == "neutral":
        songs.append(song)

    elif emotion_mode == "sad":
        if genre == "blues" or genre == "jazz" or genre == "classical" or genre == "country":
            songs.append(song)

    elif emotion_mode == "happy":
        if genre == "rock" or genre == "metal" or genre == "pop":
            songs.append(song)

    elif emotion_mode == "angry":
        if genre == "metal" or genre == "rock":
            songs.append(song)

    elif emotion_mode == "surprised":
        if genre == "hiphop" or genre == "disco":
            songs.append(song)

    elif emotion_mode == "disgust":
        if genre == "raggae" or genre == "metal" or genre == "rock":
            songs.append(song)

try:
    finalPath = util.changeToWindows(random.choice(songs))            
    print('\nPlaying ' + finalPath)
    util.playMedia(finalPath)                                
except IndexError:
    print("\numm... no song for this mood... ):")
