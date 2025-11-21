# 🎵 TagTune

**TagTune** is a lightweight, command-line tool for tagging and managing metadata for your MP3 files. It’s perfect for unreleased tracks, downloaded archives, DJ edits, or that chaotic "Music" folder full of vibe-y but unnamed files.

Organize your sound. Tag it like you mean it.

---

## Features

- Add or update MP3 tags (title, artist, album, year, genre, comments)
- Embed custom cover art
- View metadata of existing songs
- Designed for unreleased tracks, leaks, DJ sets, SoundCloud rips, etc.


# 🎵 Music Metadata Editor

A simple, user-friendly Python application to edit music file metadata (ID3 tags) including artist, title, album, and album artwork.

## ✨ Features

- Edit artist, title, and album information
- Add or replace album artwork
- Support for MP3, M4A, and FLAC files
- Support for JPG, JPEG, and PNG artwork
- Preserve existing metadata when updating
- Simple drag-and-drop file selection

## 🛠️ Installation

### 1. Install Python
Make sure you have Python 3.6 or higher installed:
```bash
python --version
```

### 2. Install Required Package
```bash
pip install music-tag
```

### 3. Download the Script
Download `tagtune.py` to your computer.

## 🚀 Usage

1. **Run the script**:
   ```bash
   python tagtune.py
   ```

2. **Follow the prompts**:
   - Select your audio file (MP3, M4A, FLAC)
   - Select album artwork (optional, JPG/PNG)
   - Enter new metadata (press Enter to keep current values)
   - Confirm changes

3. **File Selection Tip**: You can drag and drop files directly into the terminal!

## 📁 Supported Formats

### Audio Files
- MP3 (.mp3)
- M4A (.m4a) 
- FLAC (.flac)

### Artwork Files
- JPEG (.jpg, .jpeg)
- PNG (.png)

## 🎯 Example Usage

```
🎵 Music Metadata Editor
========================================

📁 Step 1: Select Audio File
Supported formats: MP3, M4A, FLAC
Tip: You can drag and drop the file into the terminal
Enter audio file path: /Users/name/Music/song.mp3

🖼️  Step 2: Select Album Artwork (Optional)
Supported formats: JPG, JPEG, PNG
Press Enter to skip adding artwork
Enter artwork file path: /Users/name/Pictures/album_cover.jpg

📋 Current Metadata:
Artist: Unknown Artist
Title: Unknown Title
Album: Unknown Album

✏️  Step 3: Enter New Metadata
Press Enter to keep current value
Artist [Unknown Artist]: The Beatles
Title [Unknown Title]: Here Comes The Sun
Album [Unknown Album]: Abbey Road

📝 Summary of Changes:
Artist: The Beatles
Title: Here Comes The Sun
Album: Abbey Road
Artwork: Yes

💾 Save these changes? (y/N): y
✅ Metadata updated successfully!
```

## ⚠️ Troubleshooting

### Common Issues:

1. **"File not found"**: Check the file path and make sure the file exists
2. **"Permission denied"**: Close the file in other programs (like music players)
3. **Artwork not showing**: Some music players may require restart to see new artwork
4. **Metadata not updating**: Ensure you have write permissions for the file

### Requirements:
- Python 3.6+
- music-tag package
- Write access to the music files

## 🔧 Technical Details

This tool uses the `music-tag` Python library to read and write ID3 tags and other audio metadata formats. Changes are written directly to the audio files.


## 🎯 **Key Improvements:**

1. **User-Friendly Interface**: Clear step-by-step prompts
2. **Drag & Drop Support**: Users can drag files into terminal
3. **Preserve Existing Data**: Shows current values, Enter to keep
4. **Error Handling**: Comprehensive error messages and validation
5. **Optional Artwork**: Artwork is optional, not required
6. **Confirmation Step**: Users can review before saving
7. **Cross-Platform**: Works on Windows, Mac, and Linux
8. **Clear Documentation**: Easy-to-follow README with examples
