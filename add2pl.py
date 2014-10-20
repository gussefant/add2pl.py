#!/usr/bin/env python
#Script for adding songs to nyxmms2 playlist using fzf
import os
import subprocess
user_finder = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)    # Get the username
(user, err) = user_finder.communicate()                                         # for future use

music_dir = "/home/" + user.decode("utf-8").rstrip('\n') + "/Music" # The directory the script searches through. Default is "~/Music"
playlist_file = music_dir + "/playlist" # An intermediary file where the songs will be put prior to adding them to the playlist
fzf = "/home/" + user.decode("utf-8").rstrip('\n') + "/.fzf/fzf"    # The full path for junegunn's "fzf"-program

# Command that the script will run to allow the user pick desired songs. Finds all .mp3's
# in music_dir, sorts them, runs them through fzf and puts the choices in playlist_file.
song_chooser = "find "+music_dir+" -iname '*.mp3' | sort | " +fzf + " +s -e -m -0 > " + playlist_file

os.system(song_chooser) # Run command above
playlist = open(playlist_file, 'r') # Open playlist_file for reading
for song in playlist: # Loop through chosen songs...
    add_command = 'nyxmms2 add "' +song.rstrip('\n')+ '"' # ...construct a command for adding the song to the playlist...
    os.system(add_command) # ...and run the command
playlist.close() # Close playlist as we have finished reading it.
