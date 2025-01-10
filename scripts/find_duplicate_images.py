import os
import shutil
import hashlib

def get_file_checksum(file_path):
    """Generate MD5 checksum for the given file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates(directory):
    """Find and return duplicate images based on file checksum."""
    valid_extensions = ('.jpg', '.jpeg', '.png', '.heic', '.mp4', '.mov')
    checksum_map = {}
    total_files = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(valid_extensions):
                total_files += 1
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_checksum = get_file_checksum(file_path)
                    if file_checksum in checksum_map:
                        checksum_map[file_checksum].append(file_path)
                    else:
                        checksum_map[file_checksum] = [file_path]
                print(f"Processed {total_files} files so far...")
    duplicates = [paths for paths in checksum_map.values() if len(paths) > 1]
    print(f"Found {len(duplicates)} sets of duplicates.")
    return duplicates

def move_files(originals_directory, duplicates_directory, duplicates):
    """Move original and duplicate images to their respective directories."""
    if not os.path.exists(originals_directory):
        os.makedirs(originals_directory)
    if not os.path.exists(duplicates_directory):
        os.makedirs(duplicates_directory)
    
    for duplicate_set in duplicates:
        # Find the file with the shortest name to keep as the original
        original_file = min(duplicate_set, key=lambda x: len(os.path.basename(x)))
        for file_path in duplicate_set:
            file_name = os.path.basename(file_path)
            if file_path == original_file:
                shutil.move(file_path, os.path.join(originals_directory, file_name))
                print(f"Moved original {file_name} to {originals_directory}")
            else:
                shutil.move(file_path, os.path.join(duplicates_directory, file_name))
                print(f"Moved duplicate {file_name} to {duplicates_directory}")

def main():
    source_directory = "E:\\OneDrive\\#Unsorted"
    originals_directory = "E:\\originals"
    duplicates_directory = "E:\\dups35"
    
    duplicates = find_duplicates(source_directory)
    
    move_files(originals_directory, duplicates_directory, duplicates)
    
    print(f"Moved original images to: {originals_directory}")
    print(f"Moved duplicate images to: {duplicates_directory}")

if __name__ == "__main__":
    main()
