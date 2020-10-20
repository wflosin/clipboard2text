# clipboard2text.py
# William Losin
# 2020-10-20

"""
Turns whatever text is readable from an image stored in the clipboard
and then stores that text in the clipboard, overwriting the image.

"""

from pytesseract import image_to_string, pytesseract
from PIL import ImageGrab, Image
import pyperclip
from os import remove

pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

BMP_image = ImageGrab.grabclipboard()
if BMP_image:
    BMP_image.save("clipboard.png", "png")

    png_image = Image.open("clipboard.png")

    text = image_to_string(png_image)

    pyperclip.copy(text)

    remove("clipboard.png")
