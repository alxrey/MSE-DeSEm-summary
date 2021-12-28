from PIL import ImageGrab
from glob import glob
import re
import pyperclip




im = ImageGrab.grabclipboard()
index = -1
if(im is not None):
    files = glob('img_*.*')
    for f in files:
        m = re.search('(?<=img_)([0-9]+)', f)
        index = max(int(m.group(0)), index)
    im.save(f'img_{index+1}.png', 'PNG')
    width = float(input("\nwidth="))
    text = f'\\begin{{figure}}[H]\n\centering\n\includegraphics[width={width:.2f}cm]{{img_{index+1}.png}}\n\end{{figure}}'
    print(f"Copied text to clipboard :\n\n{text}\n\n")
    pyperclip.copy(text)
else:
    print("No image in clipboard")