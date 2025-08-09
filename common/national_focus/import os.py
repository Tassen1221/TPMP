import os
import re

# Path to the folder you want to scan
ROOT_FOLDER = "/Users/benjaminyang/Documents/Paradox Interactive/Hearts of Iron IV/mod/TPMP/history/units"

# Regex pattern to match the target line
pattern = re.compile(r'^\s*industrial_manufacturer\s*=\s*mio:\S+\s*$', re.MULTILINE)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = re.subn(pattern, '', content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed {count} matching line(s) from {filepath}")

def scan_folder(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            # Change extension filter if needed
            if file.endswith(".txt"):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    scan_folder(ROOT_FOLDER)
