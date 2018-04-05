from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def convertToImage(text):
    unicode_text = text
    font = ImageFont.truetype("arial.ttf", 28, encoding="unic")
    text_width, text_height = font.getsize(unicode_text)
    canvas = Image.new('RGB', (text_width + 10, text_height + 10), "orange")
    draw = ImageDraw.Draw(canvas)
    draw.text((7, 7), text, 'white', font)
    canvas.save("date_image.png", "PNG")