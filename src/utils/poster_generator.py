from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
from datetime import datetime
import qrcode
from typing import Optional

def generate_poster(
    title: str,
    description: str,
    logo_path: Optional[str] = None,
    rating: Optional[float] = None,
    studio: Optional[str] = None,
    genre: Optional[str] = None,
    season: Optional[str] = None,
    trailer_url: Optional[str] = None,
    output_path: str = "poster.png",
    bg_color: tuple = (30, 30, 60),
    channel_name: Optional[str] = None,
    post_type: Optional[str] = None,
    timestamp: Optional[str] = None
) -> str:
    """
    Generate a custom poster image with title, description, and other optional elements.
    Adds a small 'AutoPost by AnimeBot' line and improved spacing for polish.
    Optionally adds channel name, post type, and custom timestamp for Discord channel context.
    """
    width, height = 900, 500
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Background theme by genre/season
    if genre:
        genre_colors = {
            "action": (40, 40, 80),
            "romance": (80, 40, 60),
            "comedy": (60, 80, 40),
            "horror": (60, 0, 0),
            "fantasy": (40, 60, 80),
            "slice of life": (80, 80, 60),
        }
        img.paste(Image.new('RGB', (width, height), genre_colors.get(genre.lower(), bg_color)), (0, 0))
    if season:
        season_colors = {
            "spring": (180, 220, 255),
            "summer": (255, 240, 180),
            "fall": (255, 200, 120),
            "winter": (200, 220, 255),
        }
        overlay = Image.new('RGBA', (width, height), season_colors.get(season.lower(), (0,0,0,0)) + (40,))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

    # Blurred circle accent
    circle = Image.new('L', (400, 400), 0)
    ImageDraw.Draw(circle).ellipse((0, 0, 400, 400), fill=255)
    blurred = circle.filter(ImageFilter.GaussianBlur(40))
    img.paste((80, 80, 180), (width-420, 20), blurred)

    # Load fonts
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'Montserrat-Bold.ttf')
    font_title = ImageFont.truetype(font_path, 44) if os.path.exists(font_path) else ImageFont.load_default()
    font_desc = ImageFont.truetype(font_path, 28) if os.path.exists(font_path) else ImageFont.load_default()
    font_small = ImageFont.truetype(font_path, 20) if os.path.exists(font_path) else ImageFont.load_default()
    font_tiny = ImageFont.truetype(font_path, 14) if os.path.exists(font_path) else ImageFont.load_default()

    # Draw title with shadow
    shadow_offset = 2
    draw.text((40+shadow_offset, 40+shadow_offset), title, font=font_title, fill=(0,0,0,128))
    draw.text((40, 40), title, font=font_title, fill=(255, 255, 255))

    # Draw description (auto-wrap, improved spacing)
    def draw_multiline_text(draw, text, position, font, fill, max_width, line_spacing=6):
        lines = []
        words = text.split()
        while words:
            line = ''
            while words and draw.textsize(line + words[0], font=font)[0] < max_width:
                line += words.pop(0) + ' '
            lines.append(line)
        y = position[1]
        for line in lines:
            draw.text((position[0], y), line, font=font, fill=fill)
            y += font.getsize(line)[1] + line_spacing
    draw_multiline_text(draw, description, (40, 120), font_desc, (200, 220, 255), width-200, line_spacing=10)

    # Draw logo if provided
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((100, 100))
        img.paste(logo, (width-140, 30), logo)

    # Draw rating stars if provided
    if rating is not None:
        star = u"\u2B50"
        stars = star * int(round(rating))
        draw.text((40, 200), f"Rating: {stars} ({rating}/10)", font=font_desc, fill=(255, 215, 0))

    # Draw studio/network branding
    if studio:
        draw.text((40, height-80), f"Studio: {studio}", font=font_small, fill=(180,220,255))

    # Draw genre/season tags
    tag_x = width-300
    if genre:
        draw.text((tag_x, height-80), f"#{genre.title()}", font=font_small, fill=(255,180,120))
    if season:
        draw.text((tag_x, height-50), f"{season.title()} Season", font=font_small, fill=(120,180,255))

    # Draw QR code if trailer_url provided
    if trailer_url:
        qr = qrcode.make(trailer_url)
        qr = qr.resize((80, 80))
        img.paste(qr, (width-100, height-100))

    # Draw channel name and post type at the top left for Discord context
    y_offset = 10
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'Montserrat-Bold.ttf')
    font_tag = ImageFont.truetype(font_path, 18) if os.path.exists(font_path) else ImageFont.load_default()
    tag_text = ""
    if channel_name:
        tag_text += f"#{channel_name}  "
    if post_type:
        tag_text += f"[{post_type}]"
    if tag_text:
        draw.text((20, y_offset), tag_text, font=font_tag, fill=(180, 200, 255))

    # Draw timestamp (custom or now)
    now = timestamp or datetime.now().strftime('%Y-%m-%d %H:%M')
    draw.text((width-260, height-40), f"Generated: {now}", font=font_small, fill=(180,180,200))

    # Draw 'AutoPost by AnimeBot' in tiny font
    draw.text((width-260, height-22), "AutoPost by AnimeBot", font=font_tiny, fill=(160,160,180))

    # Draw a border
    border_color = (120, 180, 255)
    draw.rectangle([0, 0, width-1, height-1], outline=border_color, width=4)

    img.save(output_path)
    return output_path
