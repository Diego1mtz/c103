import sys
import time
import random 
import os
import shutil
from watchdog.observers import Observer
from whatchdog.events from FileSystemEventHandler

# Agrega la ruta de tu carpeta 

from_dir="C:\Users\diego\Downloads"

# Crea una carpeta "document_file" en tu escritorio y actualiza la ruta correspondiente 

to_dir="C:\Users\diego\OneDrive\Escritorio\Document_Fila"

dir_tree={
    "Image_Files":['.jpg','.jpeg','.png','.gif','.jfif'],
    "Video_Files":['.mpg','.mp2','.mpeg','.mpe','.mpv','.mp4','.m4p','.avi','.mov'],
    "Document_Files":['.ppt','.xls','.xlsx','.csv','.pdf','.txt'],
    "Setup_Files":['.exe','.bin','.cmd','.msi','.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension=os.path.splitText(event.src_path)

        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name =os.path.basename(event.src_path)

                print("dwscargando"+ file_name)

                path1=from_dir+'/'+file_name
                path2=to_dir+'/'+key
                path3=to_dir+'/'+key+'/'+file_name

                if os.path.exists(path2):

                    print("el directorio existe")
                    print("moviendo"+file_name+"...")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("Creando directorio")
                    os.makedirs(path2)
                    print("moviendo"+file_name+"...")
                    shutil.move(path1,path3)
                    time.sleep(1)


