# To install pyperclip use the command "pip3 install pyperclip"
import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
for line in range(len(lines)):
    lines[line] = '*' + lines[line]
pyperclip.copy(text)
