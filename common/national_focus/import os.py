import os
import re

# Path to the folder you want to scan
ROOT_FOLDER = "/Users/benjaminyang/Documents/Paradox Interactive/Hearts of Iron IV/mod/TPMP/common/national_focus"

# Pattern to match: mio:NAME = { ... }
# DOTALL allows matching across multiple lines
pattern = re.compile(
    r'^\s*mio:\S+\s*=\s*\{.*?\}\s*',
    re.DOTALL | re.MULTILINE
)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = re.subn(pattern, '', content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed {count} mio block(s) from {filepath}")

def scan_folder(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):  # Adjust if needed
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    scan_folder(ROOT_FOLDER)

