# app/ocr.py
import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def read_plate(img):
    results = reader.readtext(img)
    for (bbox, text, prob) in results:
        if prob > 0.5:
            return text.strip()
    return None
