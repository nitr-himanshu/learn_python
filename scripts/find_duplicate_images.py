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
    valid_extensions = ('.jpg', '.jpeg', '.png', '.heic')
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

def move_duplicates(duplicates, base_output_directory):
    """Move duplicate images to separate folders with numeric names."""
    folder_count = 1
    for duplicate_set in duplicates:
        output_directory = os.path.join(base_output_directory, str(folder_count))
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        for file_path in duplicate_set:
            # Move each file in the duplicate set to the output directory
            file_name = os.path.basename(file_path)
            shutil.move(file_path, os.path.join(output_directory, file_name))
        print(f"Moved set {folder_count} of duplicates.")
        folder_count += 1

def main():
    source_directory = "E:\\OneDrive\\#Unsorted"
    base_output_directory = "E:\\dups"
    duplicates = find_duplicates(source_directory)
    move_duplicates(duplicates, base_output_directory)
    print(f"Moved duplicate images to separate folders in: {base_output_directory}")

if __name__ == "__main__":
    main()
