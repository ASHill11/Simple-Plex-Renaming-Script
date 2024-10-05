# Simple-Plex-Renaming-Script
This is a simple script to procedurally rename all files in a given directory to Plex compliant names

For this script to work, a few assumptions are made

**1** - Your directory scheme is setup and named appropriately. Such as:  
>~\Shows\SHOWNAME\Season XX\Episode.mkv

>~\Shows\Fate Zero\Season 01\Fate Zero episode 1 [1080p].mp4

Any directory higher than \Shows\ does not matter.

**2** - The episodes are already in the correct order

**3** - All episodes are the same filetype. In other words, all share the same extension. The script will not attempt to modify files that do not share the extension of the targeted file.

