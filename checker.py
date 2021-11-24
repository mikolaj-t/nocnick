import io
import requests
import pytesseract
from PIL import Image

def check(url: str) -> str:
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    text = pytesseract.image_to_string(image)

    # little hack, cause every string ends with an unnecessary non-letter char
    return text[:-1]