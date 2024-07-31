# -Modules used-
# os
# mutagen.mp3 MP3

# -Variable Tracker-
# folderPath
# index
# action 
# playing : Boolean

# -List Tracker-
# musicList



# Code for mp3 rpi walkmam

# All Modules
#from mutagen.mp3 import MP3 # BACKUP Module for playing sound
from pygame import mixer 

import os
from os import walk # Module for file navigation


# Initialise File Managment
if not os.path.exists("musicFolder"): # Creates new file if no 'musicFolder' found
    os.mkdir("musicFolder")
    print("No RaspIWalk Music Folder")
    print("Created New Music Folder!")
    print("Be sure to populate musicFolder with your songs to be able to listen to them!")
else:
    print("Existing Music Folder Found!")
    
folderPath = os.getcwd() + '\musicFolder' # Gets folder path of python file and adds on the music folder
print(f"Folder Path: {folderPath}")


# Initiialise Music Player
musicList = [] # list to store all music files
songIndex = 0 # index when file navigating

for path in os.listdir(folderPath): # Populate list of songs inside Music Player Folder
    musicList.append(path)
    
print("\n",musicList) # And print list
musicListLength = len(musicList) - 1

currentSong = musicList[songIndex] # currentSong = The song inside the list that matches the index

mixer.init()
mixer.music.load(str(folderPath)+ "/" + str(currentSong))
volume = 0.3
mixer.music.set_volume(volume) 
mixer.music.play()
mixer.music.pause()

print('''

__________                       .__ __      __        .__   __    
\______   \_____    ____________ |__/  \    /  \_____  |  | |  | __
 |       _/\__  \  /  ___/\____ \|  \   \/\/   /\__  \ |  | |  |/ /
 |    |   \ / __ \_\___ \ |  |_> >  |\        /  / __ \|  |_|    < 
 |____|_  /(____  /____  >|   __/|__| \__/\  /  (____  /____/__|_ \
        ''')

# Current use instructions
print("\n- INSTRUCTIONS -\nNumber Inputs is as follows:") 
print("1. Skip Song\n2.Previous Song\n3. Pause/Play Song\n4. Volume Up\n5. Volume Down")

# Functions
def newSong(index):
    mixer.music.pause() # Pause current song
    currentSong = musicList[songIndex] 
    print(f"Now Playing {currentSong}.")
    mixer.music.load(str(folderPath)+ "/" + str(currentSong)) # May not be best way of load MP3 files but works
    mixer.music.play()

# Modules for button inputs
playing = False

while True:
    action = int(input("1,2,3 : "))
    
    if action == 1: #Skip song
        if songIndex != musicListLength:
            playing = True
            songIndex = songIndex + 1
            newSong(songIndex)
        else:
            print("Index is at the end of song list.")
        
    elif action == 2: #Previous Song
        if songIndex >= 1:
            playing = True
            songIndex = songIndex - 1
            newSong(songIndex)
        else:
            print("Index is at 0. Can't go lower")
        
    elif action == 3: # 
        if playing == True: # Pause Song
            mixer.music.pause()
            playing = False
            print(f"Paused {currentSong}.\n")
            
        elif playing == False: # Play Song
            mixer.music.unpause()
            playing = True
            print(f"Playing {currentSong}.\n")
            
    elif action == 4: # Increase Volume
        if volume <= 1.0:
            volume += 0.1
            mixer.music.set_volume(volume)
            print(f"Increased Volume : {volume}")
        else:
            print("Max Volume!")
    
    elif action == 5:
        if volume >= 0.1:
            volume -= 0.1
            mixer.music.set_volume(volume)
            print(f"Decreased Volume : {volume}")
        else:
            print("Min Volume!")
        
    
    print(f"Current index is {songIndex}")
    
    

