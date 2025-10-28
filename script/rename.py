import os
import random

target = ["acestep", "diffrhythm2", "diffrhythmplus", "levo", "lyrics", "prompt"]

base_dir = "./samples/audio"

base_files = [i.strip().replace(".lrc", "") for i in os.listdir(os.path.join(base_dir, "lyrics"))]
random.shuffle(base_files)
filemap = {i: f"{idx:03}" for idx, i in enumerate(base_files)}

for i in target:
    ext = ".mp3" if i in ["acestep", "diffrhythm2", "diffrhythmplus", "levo", "prompt"] else ".lrc"
    for k, v in filemap.items():
        try:
            os.rename(
                os.path.join(base_dir, i, k + ext),
                os.path.join(base_dir, i, v + ext)
            )
        except:
            pass
