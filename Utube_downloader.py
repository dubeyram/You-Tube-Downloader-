from __future__ import unicode_literals
import youtube_dl
ydl_opts= { }
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([' Paste Your Link Here! '])
    
 # You can paste a single video Link & also the whole playlist Link .
