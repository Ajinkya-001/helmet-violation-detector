import easyocr
import cv2

reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image, bbox):
    x1, y1, x2, y2 = map(int, bbox)
    cropped = image[y1:y2, x1:x2]
    results = reader.readtext(cropped)
    return results[0][1] if results else "UNKNOWN"
