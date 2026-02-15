# 📂simple file organizer using python
Automatically organizes files into folders based on file types in one execution

## 🔐FEATURES-
-sorts images,documents,videos.<br>
-creates individual folders for every file types  based on their extensions.<br>
-Moves unknown files to others.<br>

## How to run-
```python
python organizer.py
```

### Before
Downloads/<br>
   photo.jpg<br>
   photo2.png<br>
   resume.pdf<br>
   weird.hfjf<br>
### After
Downloads/<br>
   images/<br>
     photo.jpg<br>
     photo2.png<br>
   Documents/<br>
     resume.pdf<br>
   others/<br>
     weird.hfjf<br>

## 📖Libraries used
-OS<br>
 for the program to interact with the operating system<br>
-shutil<br>
 to shift the utilities during the program execution<br>
-sys<br>
 for the program to interact with the command line and take the folder path<br>
