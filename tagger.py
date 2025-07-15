import argparse
from mutagen.id3 import (
    ID3, TIT2, TPE1, TALB, TYER, TCON, COMM, APIC, ID3NoHeaderError
)
from mutagen.mp3 import MP3
from PIL import Image
import io
import os
import csv

def resize_image(image_path):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        img.thumbnail((600, 600))
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='JPEG')
        return byte_arr.getvalue()

def tag_mp3(file_path, title, artist, album, year, genre, comment, cover_path):
    if not file_path.endswith('.mp3'):
        print("⚠️ Only MP3 files are supported.")
        return

    audio = MP3(file_path, ID3=ID3)

    try:
        audio.add_tags()
    except ID3NoHeaderError:
        pass

    if title:
        audio.tags["TIT2"] = TIT2(encoding=3, text=title)
    if artist:
        audio.tags["TPE1"] = TPE1(encoding=3, text=artist)
    if album:
        audio.tags["TALB"] = TALB(encoding=3, text=album)
    if year:
        audio.tags["TYER"] = TYER(encoding=3, text=str(year))
    if genre:
        audio.tags["TCON"] = TCON(encoding=3, text=genre)
    if comment:
        audio.tags["COMM"] = COMM(encoding=3, lang="eng", desc="desc", text=comment)
    if cover_path and os.path.isfile(cover_path):
        img_data = resize_image(cover_path)
        audio.tags["APIC"] = APIC(
            encoding=3, mime="image/jpeg", type=3, desc="Cover", data=img_data
        )

    audio.save()
    print(f"\n✅ Tagged '{file_path}' successfully!")

def read_tags(file_path):
    if not os.path.exists(file_path):
        print("❌ File not found.")
        return
    if not file_path.endswith('.mp3'):
        print("⚠️ Only MP3 files are supported.")
        return

    audio = MP3(file_path, ID3=ID3)
    tags = audio.tags

    if not tags:
        print("ℹ️ No metadata tags found in this file.")
        return

    print("\n🎵 Metadata for:", file_path)
    print("-" * 30)
    print("🎼 Title   :", tags.get("TIT2", "—").text[0] if tags.get("TIT2") else "—")
    print("🎤 Artist  :", tags.get("TPE1", "—").text[0] if tags.get("TPE1") else "—")
    print("💿 Album   :", tags.get("TALB", "—").text[0] if tags.get("TALB") else "—")
    print("📅 Year    :", tags.get("TYER", "—").text[0] if tags.get("TYER") else "—")
    print("🎧 Genre   :", tags.get("TCON", "—").text[0] if tags.get("TCON") else "—")
    print("📝 Comment :", tags.get("COMM::eng", "—").text[0] if tags.get("COMM::eng") else "—")
    print("🖼️ Cover Art:", "✅ Yes" if "APIC:" in tags or "APIC:Cover" in tags else "❌ No")
    print("-" * 30)

def extract_all_metadata_to_csv(directory, output_csv="music_metadata.csv"):
    if not os.path.isdir(directory):
        print("❌ Directory not found.")
        return

    mp3_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))

    if not mp3_files:
        print("📂 No MP3 files found in the directory.")
        return

    print(f"🔍 Found {len(mp3_files)} MP3 files. Extracting metadata...")

    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['File Path', 'Title', 'Artist', 'Album', 'Year', 'Genre', 'Comment', 'Cover Art']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for path in mp3_files:
            try:
                audio = MP3(path, ID3=ID3)
                tags = audio.tags or {}

                writer.writerow({
                    'File Path': path,
                    'Title': tags.get("TIT2", "").text[0] if tags.get("TIT2") else "",
                    'Artist': tags.get("TPE1", "").text[0] if tags.get("TPE1") else "",
                    'Album': tags.get("TALB", "").text[0] if tags.get("TALB") else "",
                    'Year': tags.get("TYER", "").text[0] if tags.get("TYER") else "",
                    'Genre': tags.get("TCON", "").text[0] if tags.get("TCON") else "",
                    'Comment': tags.get("COMM::eng", "").text[0] if tags.get("COMM::eng") else "",
                    'Cover Art': "Yes" if "APIC:" in tags or "APIC:Cover" in tags else "No"
                })
            except Exception as e:
                print(f"⚠️ Error reading {path}: {e}")

    print(f"✅ Metadata written to {output_csv}")

def prompt_for_missing(arg, prompt_text):
    return arg if arg else input(f"{prompt_text}: ").strip()

def main():
    parser = argparse.ArgumentParser(description="🎶 Tag, read, or export metadata of MP3 files.")
    parser.add_argument("--file", help="Path to the MP3 file")
    parser.add_argument("--read", action="store_true", help="Read and display metadata")
    parser.add_argument("--title", help="Song title")
    parser.add_argument("--artist", help="Artist name")
    parser.add_argument("--album", help="Album name")
    parser.add_argument("--year", help="Year of release")
    parser.add_argument("--genre", help="Genre")
    parser.add_argument("--comment", help="Comment or note")
    parser.add_argument("--cover", help="Path to cover image (jpg/png)")
    parser.add_argument("--dumpcsv", help="Scan a folder and export all MP3 metadata to CSV")

    args = parser.parse_args()

    if args.dumpcsv:
        extract_all_metadata_to_csv(args.dumpcsv)
        return

    if args.read:
        file_path = prompt_for_missing(args.file, "🎵 Enter path to MP3 file")
        read_tags(file_path)
        return

    file_path = prompt_for_missing(args.file, "🎵 Enter path to MP3 file")
    title     = prompt_for_missing(args.title, "🎼 Title")
    artist    = prompt_for_missing(args.artist, "🎤 Artist")
    album     = prompt_for_missing(args.album, "💿 Album")
    year      = prompt_for_missing(args.year, "📅 Year")
    genre     = prompt_for_missing(args.genre, "🎧 Genre")
    comment   = prompt_for_missing(args.comment, "📝 Comment (optional)")
    cover     = prompt_for_missing(args.cover, "🖼️ Cover image path (optional)")

    tag_mp3(file_path, title, artist, album, year, genre, comment, cover)

if __name__ == "__main__":
    main()
