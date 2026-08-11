import os
import shutil

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
            dst_dir_path = os.path.normpath(os.path.join(dst_dir, src_file))
            copy_file_contents(src_file_path, dst_dir_path)

def clean_file(dir: str) -> None:
    if not os.path.exists(dir):
        os.rmtree(dir)     


        
