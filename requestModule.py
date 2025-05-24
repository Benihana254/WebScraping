# Downloads Romeo and Juliet and Saves it on the deskTop
from os import makedirs
import requests,shutil,os
response = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# the next block attempt to catch any runtime errors
try:
    response.raise_for_status()
except Exception as exc:
    print(f'Sorry programme crashed error code; {exc}') # 'Exception' catches general error while exc catches the specific one

with open('Romeo', 'w', encoding='utf-8') as novel:
    novel.write(response.text)
    os.startfile('Romeo')
old_path = (os.path.abspath('Romeo'))
new_path = r'C:\Users\gh\Desktop\Romeo_and_Juliet'
os.makedirs(new_path, exist_ok=True)
shutil.move(old_path, new_path)
print('Download Complete!')
# os.startfile(.join(new_path,'Romeo.txt')