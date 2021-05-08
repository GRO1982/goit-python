import os
import re
import shutil
from pathlib import Path
​
​
def normalize(text):
​
    CYRILLIC = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "є", "і", "ї", "ґ")
    LATIN = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ja", "je", "ji", "g")
    TRANS = {}
​
    for c, l in zip(CYRILLIC, LATIN):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.capitalize()
    clear_text = re.sub(r'[^\w\s]', '_', text.translate(TRANS))
    return clear_text
​
​
def sort_files(path):
    for root, folders, files in os.walk(path):        
        for folder in folders:
            new_folder = normalize(folder)
            os.rename(f'{root}\{folder}', f'{root}\{new_folder}')
        for item in files:
            new_file = normalize(os.path.splitext(item)[0]) + os.path.splitext(item)[1]
            new_dir = normalize(os.path.splitext(item)[0])
            if item.endswith(('.jpeg', '.png','.jpg','.svg')):
                os.makedirs(os.path.join(path, 'images'), exist_ok=True)
                os.replace(f'{root}\{item}', f'{path}\images\{new_file}')
            elif item.endswith(('.doc', '.docx','.txt','.pdf','.xlsx','.pptx')):
                os.makedirs(os.path.join(path, 'documents'), exist_ok=True)
                os.replace(f'{root}\{item}', f'{path}\documents\{new_file}')
            elif item.endswith(('.mp3', '.ogg','.wav','.amr')):
                os.makedirs(os.path.join(path, 'audio'), exist_ok=True)
                os.replace(f'{root}\{item}', f'{path}\\audio\{new_file}')
            elif item.endswith(('.avi', '.mp4','.mov','.mkv')):
                os.makedirs(os.path.join(path, 'video'), exist_ok=True)
                os.replace(f'{root}\{item}', f'{path}\\video\{new_file}')
            elif item.endswith(('.zip', '.gz','.tar')):
                shutil.unpack_archive(f'{path}\{new_file}', f'{path}\\archives\{new_dir}')
                os.remove(f'{path}\{new_file}')
            else:
                os.rename(f'{root}\{item}', f'{root}\{new_file}')
        if not folders and not files:
            os.rmdir(root)
​
​
path = Path('/Users/GRO/Downloads')
sort_files(path)
