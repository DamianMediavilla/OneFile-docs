"""
Este script, recorre los archivos en un directorio, revisa la extension de los archivos, y los mueve a diferentes capetas segun su tipo-
Si se trata de imágenes ademas, las comprime. Las imagenes nuevas son renombradas y guardadas, mientras las viejas son destruidas-

"""

from pickletools import optimize
import shutil
from PIL import Image
import os
import shutil

originFolder= "C:/Users/Damo/Desktop/OriginPy/"
imagesFolder= "C:/Users/Damo/Desktop/ImagesPy/"
musicFolder= "C:/Users/Damo/Desktop/MusicPy/"
textFolder= "C:/Users/Damo/Desktop/TextPy/"

if __name__=="__main__":
    for filename in os.listdir(originFolder):
        name,extension = os.path.splitext(originFolder + filename)
        if extension in (".jpg",".jpeg", ".png"):
            img = Image.open(originFolder + filename)
            img.save(imagesFolder + "compressed_" + filename, optimize=True, quality=60)
            os.remove(originFolder + filename)
        if extension in (".mp3", ".wav"):
            shutil.move(originFolder+filename, musicFolder+filename )
