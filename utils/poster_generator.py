from PIL import Image, ImageDraw, ImageFont
import os

def generate_poster(title, description, output_path="poster.png"):
    img = Image.new('RGB', (800, 400), color=(30, 30, 60))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((20, 20), title, font=font, fill=(255,255,255))
    d.text((20, 60), description, font=font, fill=(200,200,200))
    img.save(output_path)
    return output_path
