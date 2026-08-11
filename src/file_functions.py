import os
import shutil
from pathlib import Path

def copy_file_contents(src_dir: str, dst_dir: str) -> None:
    if not os.path.exists(src_dir):
        raise Exception("Source directory does not exist")
    
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)      

    for src_file in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, src_file)
        if os.path.isfile(src_file_path):
            shutil.copy(src_file_path, dst_dir)
        else:
            dst_dir_path = os.path.join(dst_dir, src_file)
            copy_file_contents(src_file_path, dst_dir_path)


def clean_file(dir: str) -> None:
    if os.path.exists(dir):
        shutil.rmtree(dir)     

def write_to_html_file(content: str, dst_path: str) -> None:
    file_path = Path(dst_path)

    if file_path.suffix.lower() != ".html":
        file_path = file_path.with_suffix(".html")

    file_path.parent.mkdir(parents=True, exist_ok=True)
   
    file_path.write_text(content, encoding="utf-8")

def read_from_file(file_path):
    content = ""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content
