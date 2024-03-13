from pathlib import Path
import os

path = str(Path.cwd()) + "\Muzica"
folder_path = Path(path)
folder_contents = folder_path.iterdir()

for audio in folder_contents:
    try:
        src = str(audio)
        dest = str(audio.with_suffix(".mp3"))
        os.rename(src, dest)
    except:
        print("Rename failed")