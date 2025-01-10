import os
from collections import defaultdict

def count_files_by_extension(directory):
    """Count files by their extension in the given directory recursively."""
    extension_count = defaultdict(int)
    for root, _, files in os.walk(directory):
        for file in files:
            extension = os.path.splitext(file)[1].lower()
            extension_count[extension] += 1
    return dict(extension_count)

def main():
    directory = "E:\\OneDrive\\#Unsorted"
    counts = count_files_by_extension(directory)
    for extension, count in counts.items():
        print(f"{extension}: {count} files")

if __name__ == "__main__":
    main()
