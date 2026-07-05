from pathlib import Path
import shutil
from datetime import datetime
from config import FILE_TYPES

def category_for(ext):
    ext = ext.lower()
    for cat, exts in FILE_TYPES.items():
        if ext in exts:
            return cat
    return "Others"

def unique_path(path: Path):
    if not path.exists():
        return path
    i = 1
    while True:
        new = path.with_name(f"{path.stem}_{i}{path.suffix}")
        if not new.exists():
            return new
        i += 1

def organize(folder):
    folder = Path(folder)
    moved = 0
    log_lines = []
    for item in folder.iterdir():
        if item.is_file():
            cat = category_for(item.suffix)
            dest_dir = folder / cat
            dest_dir.mkdir(exist_ok=True)
            dest = unique_path(dest_dir / item.name)
            shutil.move(str(item), str(dest))
            moved += 1
            log_lines.append(f"{item.name} -> {cat}")
    log = folder / "logs"
    log.mkdir(exist_ok=True)
    with open(log/"organizer.log","a",encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write("\n".join(log_lines))
        f.write("\n")
    return moved
