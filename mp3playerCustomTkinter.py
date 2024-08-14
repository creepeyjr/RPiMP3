# -Modules used-
# os
# mutagen.mp3 MP3
# 

# -Variable Tracker-
# folderPath
# index
# action 
# songState : Boolean
# musicListLength

# -List Tracker-
# musicList

# -Functions List-
# newSong(index)
# pausePlay()



# Code for mp3 rpi walkmam

# All Modules
from pygame import mixer # MP3 Player

import os
from os import walk # Module for file navigation

import customtkinter # GUI Interface

# Screen Display Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")
customtkinter.set_window_scaling(1) # Scale Window, but may not be relevant since screen is locked on full by default.
customtkinter.set_widget_scaling(1) # Scale Widgets (Waveshare 3.5 : 0.4) or Regular Screen (0.8 - 1)

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.attributes('-fullscreen', True)
app.title("WalkPi GUI")

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
 __      __        .__   __   __________.__ 
/  \    /  \_____  |  | |  | _\______   \__|
\   \/\/   /\__  \ |  | |  |/ /|     ___/  |
 \        /  / __ \|  |_|    < |    |   |  |
  \__/\  /  (____  /____/__|_ \|____|   |__|
       \/        \/          \/             
''')

# Variables for button inputs
songState = False

# Functions
def newSong(index): # When called, takes updated index and changes song to said index
    mixer.music.pause() # Pause current song
    currentSong = musicList[songIndex] 
    print(f"Now Playing {currentSong}.")
    mixer.music.load(str(folderPath)+ "/" + str(currentSong)) # May not be best way of load MP3 files but works
    mixer.music.play()

def pausePlay():
    global songState
    if songState == True:
        mixer.music.pause()
        songState = False
    else:
        mixer.music.unpause()
        songState = True

def skipSong():
    global songIndex
    if songIndex != musicListLength: # Only runs if song index is not at the end of the song list
        songIndex = songIndex + 1 # Going one up in song index
        newSong(songIndex) # Calling function to play new song
        songState = True # Song is playing, so logic updated
    else:
        print("PLACEHOLDER : REACHED END OF SONG LIST")

def previousSong():
    global songIndex
    if songIndex >= 1: # Only runs if song index is not at 1 or lower
        songIndex = songIndex - 1 # Going down one in song index
        newSong(songIndex) # Calling function to play new song
        songState = True # Song is playing, so logic updated
    else:
        print("PLACEHOLDER : AT THE BEGINNING OF SONGLIST")


# GUI Widgets Declaration
songTitle = customtkinter.CTkLabel(
    master = app,
    text = "Current Song",
    text_color = "#DBE7C9",
    font = ("Helvetica", 98)
)

playButton = customtkinter.CTkButton( # Button for Pausing and Playing current song
    master = app,
    text = "Play",
    command = lambda: pausePlay(),
)

skipButton = customtkinter.CTkButton(
    master = app,
    text = "Skip Song",
    command = lambda: skipSong()
)

previousButton = customtkinter.CTkButton(
    master = app,
    text = "Previous Song",
    command = lambda: previousSong()
)

# Placing and Positioning Widgets
songTitle.pack(padx = 15, pady = 30)
playButton.pack(padx = 15, pady = 30)
skipButton.pack(padx = 15, pady = 30)
previousButton.pack(padx = 15, pady = 30)
    
app.mainloop() # Main GUI App Loop

