#!/usr/bin/env python
#Script for adding songs to nyxmms2 playlist
import os
import subprocess
user_finder = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)
(user, err) = user_finder.communicate()
music_dir = "/home/" + user.decode("utf-8").rstrip('\n') + "/Music"
playlist_file = music_dir + "/playlist"
fzf = "/home/" + user.decode("utf-8").rstrip('\n') + "/.fzf/fzf"
playlist = open(playlist_file, 'r')
song_chooser = "find "+music_dir+" -iname '*.mp3' | sort | " +fzf + " +s -e -m -0 > " + playlist_file
os.system(song_chooser)
for song in playlist:
    add_command = 'nyxmms2 add "' +song.rstrip('\n')+ '"'
    os.system(add_command)
playlist.close()
