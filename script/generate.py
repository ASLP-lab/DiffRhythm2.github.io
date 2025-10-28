import os
"""
<tr>
<td class="is-vcentered" width="12%" style="text-align: center;">
  Rock, Pop
</td>
<td width="30%" style="text-align: left;">
  <div class="card lyrics-card">
    <header class="card-header">
      <p class="card-header-title">Lyrics</p>
      <div class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fas fa-angle-down arrow" aria-hidden="true"></i>
        </span>
      </div>
    </header>
    <div class="card-content collapsible">
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
      <p>Lorem ipsum dolor sit amet...</p>
      <p>Aliquam tincidunt mauris eu risus...</p>
      <p>Vestibulum auctor dapibus neque...</p>
    </div>
  </div>
</td>
<td class="is-vcentered" width="12%" style="text-align: center;">
  <audio controls="">
    <source src="static/audio_sample/yue/02.mp3" type="audio/wav">
  </audio>
</td>
<td class="is-vcentered" width="12%" style="text-align: center;">
  <audio controls="">
    <source src="static/audio_sample/diffrhythm/02.mp3" type="audio/wav">
  </audio>
</td>
<td class="is-vcentered" width="12%" style="text-align: center;">
  <audio controls="">
    <source src="static/audio_sample/acestep/02.mp3" type="audio/wav">
  </audio>
</td>
<td class="is-vcentered" width="12%" style="text-align: center;">
  <audio controls="">
    <source src="static/audio_sample/overview/02.mp3" type="audio/wav">
  </audio>
</td>
</tr>
"""

def build_audio(category, audio_name):
    return f"""<td class="is-vcentered" width="12%" style="text-align: center;">
  <audio controls="">
    <source src="samples/{category}/{audio_name}" type="audio/wav">
  </audio>
</td>"""


def build_text_prompt(prompt):
    return f"""<td class="is-vcentered" width="12%" style="text-align: center;">
  {prompt}
</td>"""


def build_audio_prompt(audio_name):
    return build_audio("audio/prompt", audio_name)

def build_lyrics(lyrics):
    lyrics = lyrics.split("\n")
    lyrics = [f"<p>{i.strip()}</p>" for i in lyrics]
    lyrics = "\n".join(lyrics)
    return f"""<td width="30%" style="text-align: left;">
  <div class="card lyrics-card">
    <header class="card-header">
      <p class="card-header-title">Lyrics</p>
      <div class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fas fa-angle-down arrow" aria-hidden="true"></i>
        </span>
      </div>
    </header>
    <div class="card-content collapsible">
      {lyrics}
    </div>
  </div>
</td>"""

def build_row(audio_name, lyrics, targets, text_prompt=None):
    prompt_col = build_text_prompt(text_prompt) if text_prompt is not None else build_audio_prompt(audio_name)
    lyrics_col = build_lyrics(lyrics)
    target_cols = [build_audio(i, audio_name) for i in targets]
    all_col = [prompt_col + lyrics_col] + target_cols
    col = "\n".join(all_col)
    return f"""<tr>
  {col}
</tr>"""

if __name__ == "__main__":
  target = ["diffrhythmplus", "acestep", "levo", "diffrhythm2"]
  base_dir = "./samples/audio"
  target = ["audio/" + i for i in target]
  base_files = [i.strip().replace(".lrc", "") for i in os.listdir(os.path.join(base_dir, "lyrics"))]

  tr = []
  for i in base_files:
    # with open(os.path.join(base_dir, "prompt", i+".lrc")) as f:
    #   prompt = f.read().strip()
    with open(os.path.join(base_dir, "lyrics", i+".lrc")) as f:
      lrc = f.read().strip()
    tr.append(build_row(i+".mp3", lrc, target))
  with open("tmp_table", "w") as f:
    f.write("\n".join(tr))


