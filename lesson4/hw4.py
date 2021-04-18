import os
from pathlib import Path

def sort_files(path):
    pictures = []   #('JPEG', 'PNG', 'JPG', 'SVG')
    video = []      #('AVI', 'MP4', 'MOV', 'MKV')
    documents = []  #('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    music = []      #('MP3', 'OGG', 'WAV', 'AMR')
    archives = []   #('ZIP', 'GZ', 'TAR');
    others = []     #unknown
    fileExtensions = []
    fileExtensionsUnknown = []

    for root, subFolder, files in os.walk(path):
        for item in files:
            fileName = os.path.join(item)
            fileExtension = os.path.splitext(item)[1]
            if item.endswith(('.jpeg', '.png','.jpg','.svg')):
                pictures.append(fileName)
                fileExtensions.append(fileExtension)
            elif item.endswith(('.avi', '.mp4','.mov','.mkv')):
                video.append(fileName)
                fileExtensions.append(fileExtension)
            elif item.endswith(('.doc', '.docx','.txt','.pdf','.xlsx','.pptx')):
                documents.append(fileName)
                fileExtensions.append(fileExtension)
            elif item.endswith(('.mp3', '.ogg','.wav','.amr')):
                music.append(fileName)
                fileExtensions.append(fileExtension)
            elif item.endswith(('.zip', '.gz','.tar')):
                archives.append(fileName)
                fileExtensions.append(fileExtension)
            else:
                others.append(fileName)
                fileExtensionsUnknown.append(fileExtension)
    fileExtensions = list(dict.fromkeys(fileExtensions))
    fileExtensionsUnknown = list(dict.fromkeys(fileExtensionsUnknown))
    
    print(f"pictures = {pictures}")
    print(f"video = {video}")
    print(f"documents = {documents}")
    print(f"music = {music}")
    print(f"archives = {archives}")
    print(f"others = {others}")
    print(f"fileExtensions = {fileExtensions}")
    print(f"fileExtensionsUnknown = {fileExtensionsUnknown}")
    return pictures, video, documents, music, archives, others, fileExtensions, fileExtensionsUnknown

path = Path('/Users/GRO/Downloads')
sort_files(path)