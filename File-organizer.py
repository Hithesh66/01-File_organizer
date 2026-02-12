#organize the  files in a folder based on their file type according to their extensions.
# by creating folders for each types.
# Hithesh-13/02/2026 

import os
import shutil
import sys
FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp",".jfif"],
    "documents": [".pdf", ".doc", ".docx", ".txt"],
    "videos": [".mp4", ".avi", ".mov",".mkv",".MKV Video File (VLC) (.mkv)",".srt"],
    "audio": [".mp3", ".wav", ".flac",".m4a"],
    "applications": [".exe",".zip",".iso"]
}


def organizer(source_folder):
    if not os.path.exists(source_folder):
        print(f'the folder {source_folder} does not exists')
        return
    
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):
            file_type = os.path.splitext(file)[1].lower()
            moved = False

            for folder_name, extensions in FILE_TYPES.items():
                if file_type in extensions:
                    folder_path = os.path.join(source_folder, folder_name)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path,file))
                    print(f"moved {file} => {folder_name}")
                    moved = True
                    break
            if not moved:
                others_path = os.path.join(source_folder, 'others')
                os.makedirs(others_path, exist_ok=True)
                shutil.move(file_path, os.path.join(others_path,file))
                print(f"moved {file} => others")
    print("files organized successfully")

if __name__ == "__main__":
    folder = input("enter the path of the folder to organize =>")
    organizer(folder)
                                



    