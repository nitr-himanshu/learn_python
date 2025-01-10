import os
import shutil

def move_files_recursively(src_directory, dest_directory):
    """Move all files from src_directory to dest_directory recursively."""
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)
    
    total_files = 0
    for root, _, files in os.walk(src_directory):
        for file in files:
            total_files += 1
            src_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_directory, file)
            shutil.move(src_file_path, dest_file_path)
            print(f"Moved {file} to {dest_directory}")
    
    print(f"Total files moved: {total_files}")

def main():
    src_directory = "E:\\dups"
    dest_directory = "E:\\iimmgg"
    move_files_recursively(src_directory, dest_directory)
    print(f"All files moved from {src_directory} to {dest_directory}")

if __name__ == "__main__":
    main()
