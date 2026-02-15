# 📂simple file organizer using python
Automatically organizes files into folders based on file types in one execution

## 🔐FEATURES-
-sorts images,documents,videos.
-creates individual folders for every file types  based on their extensions.
-Moves unknown files to others.

## How to run-
```python
organizer.py
```

### Before
Downloads/
   photo.jpg
   photo2.png
   resume.pdf
   weird.hfjf
### After
Downloads/
   images/
     photo.jpg
     photo2.png
   Documents/
     resume.pdf
   others/
     weird.hfjf

## 📖Libraries used
-OS
 for the program to interact with the operating system
-shutil
 to shift the utilities during the program execution
-sys
 for the program to interact with the command line and take the folder path