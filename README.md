# clipboard2text
Turns whatever text is readable from an image stored in the clipboard and then stores 
that text in the clipboard, overwriting the image.

#######################################################################################
Installation for Windows:

Install pyinstaller with the following command into the command prompt:

pip install pyinstaller

Then run the command below (which is also found in the "pyinstaller command.txt" file)
inside the working directory:

pyinstaller clipboard2text.py --noconsole --icon=clipboard2text.ico

#######################################################################################
Dependencies:

Pillow 6.1.0
pyperclip 1.8.1
pytesseract 0.3.6
