import music_tag
import os
from pathlib import Path

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print application header"""
    print("🎵 TagTune Music Editor")
    print("=" * 40)

def get_file_path(prompt, file_type):
    """Get valid file path from user"""
    while True:
        file_path = input(prompt).strip()
        
        # Remove quotes if user drag-and-drops file
        file_path = file_path.strip('"')
        
        if not file_path:
            print("❌ Please enter a file path")
            continue
            
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue
            
        if file_type == "audio" and not file_path.lower().endswith(('.mp3', '.m4a', '.flac')):
            print("❌ Please select an audio file (.mp3, .m4a, .flac)")
            continue
            
        if file_type == "image" and not file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            print("❌ Please select an image file (.jpg, .jpeg, .png)")
            continue
            
        return file_path

def main():
    clear_screen()
    print_header()
    
    try:
        # Get audio file
        print("\n📁 Step 1: Select Audio File")
        print("Supported formats: MP3, M4A, FLAC")
        print("Tip: You can drag and drop the file into the terminal")
        audio_file = get_file_path("Enter audio file path: ", "audio")
        
        # Get artwork file (optional)
        print("\n🖼️  Step 2: Select Album Artwork (Optional)")
        print("Supported formats: JPG, JPEG, PNG")
        print("Press Enter to skip adding artwork")
        artwork_file = input("Enter artwork file path: ").strip().strip('"')
        
        if artwork_file and not os.path.exists(artwork_file):
            print("❌ Artwork file not found, continuing without artwork...")
            artwork_file = None
        
        # Load audio file
        print(f"\n📥 Loading audio file: {os.path.basename(audio_file)}")
        audio = music_tag.load_file(audio_file)
        
        # Display current metadata
        print("\n📋 Current Metadata:")
        print(f"Artist: {audio['artist'] or 'Not set'}")
        print(f"Title: {audio['title'] or 'Not set'}")
        print(f"Album: {audio['album'] or 'Not set'}")
        
        # Get new metadata
        print("\n✏️  Step 3: Enter New Metadata")
        print("Press Enter to keep current value")
        
        current_artist = str(audio['artist']) if audio['artist'] else ""
        current_title = str(audio['title']) if audio['title'] else ""
        current_album = str(audio['album']) if audio['album'] else ""
        
        artist = input(f"Artist [{current_artist}]: ").strip()
        title = input(f"Title [{current_title}]: ").strip()
        album = input(f"Album [{current_album}]: ").strip()
        
        # Update metadata (only if user provided new values)
        if artist:
            audio['artist'] = artist
        if title:
            audio['title'] = title
        if album:
            audio['album'] = album
        
        # Add artwork if provided
        if artwork_file:
            try:
                with open(artwork_file, 'rb') as img_file:
                    audio['artwork'] = img_file.read()
                print("✅ Album artwork added")
            except Exception as e:
                print(f"❌ Error adding artwork: {e}")
        
        # Confirm changes
        print("\n📝 Summary of Changes:")
        print(f"Artist: {audio['artist']}")
        print(f"Title: {audio['title']}")
        print(f"Album: {audio['album']}")
        print(f"Artwork: {'Yes' if artwork_file else 'No'}")
        
        confirm = input("\n💾 Save these changes? (y/N): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            audio.save()
            print("✅ Metadata updated successfully!")
        else:
            print("❌ Changes discarded")
            
    except KeyboardInterrupt:
        print("\n\n👋 Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please make sure:")
        print("- The audio file is not open in another program")
        print("- You have write permissions for the file")
        print("- The file format is supported")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()