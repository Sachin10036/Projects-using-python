import pytesseract
from PIL import Image

# Make sure to point to the actual Tesseract executable, not the setup file.
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    img = Image.open('img.jpg')
    text = pytesseract.image_to_string(img)
    print(text)
    
convert()



