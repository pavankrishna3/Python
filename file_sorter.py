import os
import shutil

directory  = r"C:\Users\pavan\OneDrive\Desktop\test"

image = (".jpg", ".png", ".gif", "jpeg",".svg",".webp")

video = (".mp4",".mov",".avi",".mkv","webm")

docs = (".pdf",".docx",".doc")

list = os.listdir(directory)

for i in list:
    
    if i.lower().endswith(image):
        img_path =  directory +"\Images"
        if os.path.exists(img_path):
            source = os.path.join(directory,i)
            destination = os.path.join(img_path,i)  
            shutil.move(source,destination)
        else:
            os.mkdir(img_path)
    if i.lower().endswith(video):
        vid_path = directory +"\Videos"
        if os.path.exists(vid_path):
            source = os.path.join(directory,i)
            destination = os.path.join(vid_path,i)  
            shutil.move(source,destination)
        else:
            os.mkdir(vid_path)
    if i.lower().endswith(docs):
        doc_path = directory +"\Docs"
        if os.path.exists(doc_path):
            source = os.path.join(directory,i)
            destination = os.path.join(doc_path,i)  
            shutil.move(source,destination)
        else:
            os.mkdir(doc_path)
   

    




