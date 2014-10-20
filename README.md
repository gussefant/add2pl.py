add2pl.py - fzf+nyxmms2 = Add to playlist (add2pl)
==================================================

A relatively simple python script that uses junegunn's [fzf (Fuzzy finder for your shell)](https://github.com/junegunn/fzf) to add songs to a [nyxmms2](https://xmms2.org/wiki/Main_Page) playlist.

Requirements
------------

add2pl.py requires:
	-[fzf (Fuzzy finder for your shell)](https://github.com/junegunn/fzf)
	-[nyxmms2](https://xmms2.org/wiki/Main_Page)
	-Python (>= 3.0)
fzf requires Ruby (>= 1.8.5)

Usage
-----

1. Run script
```sh
./add2pl.py
```
2. Start typing the title(s)/name(s) of the song(s)/artist(s)/album(s) you are looking for
3. Navigate to song using arrow keys and press <enter> to select a song, and/or <tab> to select several and <enter> to finish
4. The selected songs have been added to the playlist, start playback if not already started
```sh
nyxmms2 play
```

Contact
-------

Karl August Høivik
gussefant@gmail.com
