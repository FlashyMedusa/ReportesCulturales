# 🐍 Código Pythonizado por Flashy Meduza 🐍

import os
import shutil

def safe_copy_file(src_path, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    base_name = os.path.basename(src_path)
    dest_path = os.path.join(dest_dir, base_name)
    counter = 1
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(base_name)
        dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
        counter += 1
    shutil.copy2(src_path, dest_path)
    return dest_path

def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass
