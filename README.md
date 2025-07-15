# 🎵 TuneTag

**TuneTag** is a lightweight, command-line tool for tagging and managing metadata for your MP3 files. It’s perfect for unreleased tracks, downloaded archives, DJ edits, or that chaotic "Music" folder full of vibe-y but unnamed files.

Organize your sound. Tag it like you mean it.

---

## Features

- Add or update MP3 tags (title, artist, album, year, genre, comments)
- Embed custom cover art
- View metadata of existing songs
- Export all MP3 metadata in a folder to CSV
- Interactive prompts or command-line automation — your choice
- Designed for unreleased tracks, leaks, DJ sets, SoundCloud rips, etc.

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/TuneTag.git
cd TuneTag

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
````


##  Usage Instructions

###  1. Tag a Song Interactively

```bash
python tagger.py
```

You’ll be prompted to enter title, artist, album, year, genre, comment, and cover art path.

---

###  2. Tag with Command-Line Arguments

```bash
python tagger.py --file "track.mp3" --title "Unreleased Banger" --artist "Elly" --album "Secret Stash" --year 2025 --genre "Soul" --cover "cover.jpg"
```

---

### 3. Read Metadata from a Song

```bash
python tagger.py --read --file "mystery.mp3"
```

Displays tags like title, artist, album, genre, comment, and whether it has cover art.

---

### 4. Export All MP3 Metadata to CSV

```bash
python tagger.py --dumpcsv "C:/Users/user/Music"
```

This scans a folder recursively and writes metadata of every `.mp3` file to a CSV called `music_metadata.csv`.

---


