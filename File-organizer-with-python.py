# At first, use 'os' & 'shutil'.
import os
import shutil

# Logic of file-organizer include organzie_files.
def organzie_files(directory):
    file_types ={
        'images':['.jpg', '.jpeg','.png', '.gif'],
        'videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'documents':['.pdf', 'docx', '.txt', 'pptx'],
        'application':['.exe'],
        'other':[]
    }

    for subdir in file_types:
        os.makedirs(os.path.join(directory,subdir), exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            file_moved = False
            for category, extension, in file_types.items():
                if file_extension in extension:
                    shutil.move[file_path,os.path.join(directory,category,filename)]
                    file_moved = True
                    break
            if not file_moved:
                shutil.move(file_path, os.path.join(directory,'other', filename))

    print("file organization completed!")

# Put address in front of 'directory_path' variable and then this project have path to organize.
directory_path = ''
organzie_files(directory_path)





