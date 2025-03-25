import os, sys
import shutil
from pathlib import Path

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
}

def organize_files(source_dir):
    desktop_path = Path(source_dir)
    target_dir = desktop_path / "Organized_Files"
    target_dir.mkdir(exist_ok=True)
    
    # Create category folders
    category_paths = {category: target_dir / category for category in FILE_CATEGORIES}
    for path in category_paths.values():
        path.mkdir(exist_ok=True)
    
    # Move files to respective folders
    for file in desktop_path.iterdir():
        if file.is_file():
            file_ext = file.suffix.lower()
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    shutil.copy(str(file), str(category_paths[category] / file.name))
                    print(f"Copied: {file} -> {category_paths[category] / file.name}")
                    break
    
if __name__ == "__main__":
    desktop = Path.home() / "Desktop"
    print(Path.home())
    print(desktop)
    # sys.exit()
    organize_files(desktop)
