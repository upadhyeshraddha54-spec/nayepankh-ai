from PIL import Image, ImageDraw, ImageFont
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import re

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
client = InferenceClient(token=HF_TOKEN)

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000027BF"
    "\U0001F1E6-\U0001F1FF"
    "\u2700-\u27BF"
    "\u2300-\u23FF"
    "]+",
    flags=re.UNICODE,
)

def strip_emoji(text):
    return EMOJI_PATTERN.sub("", text).strip()

def load_font(paths, size):
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def center_x(draw, text, font, width):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    return (width - text_width) / 2

def create_poster(topic, location, date, time, venue):

    prompt = f"""
    realistic NGO campaign background photo for {topic},
    emotional atmosphere, realistic people, cinematic lighting,
    modern photography, premium instagram campaign style,
    abstract background, empty space for text overlay
    """

    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-schnell",
        negative_prompt="text, words, letters, typography, captions, signage, banners, watermark, logo"
    )

    WIDTH, HEIGHT = 1080, 1350
    bg = image.resize((WIDTH, HEIGHT)).convert("RGBA")

    # Base dark overlay over whole image
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 160))
    bg = Image.alpha_composite(bg, overlay)
    draw = ImageDraw.Draw(bg)

    # Fonts
    title_font = load_font([
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ], 60)
    text_font = load_font([
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ], 36)
    small_font = load_font([
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ], 28)

    # ---- NGO NAME ----
    ngo_text = strip_emoji("NAYEPANKH NGO")
    draw.text((center_x(draw, ngo_text, small_font, WIDTH), 60),
              ngo_text, fill=(255, 215, 0), font=small_font)

    # ---- TITLE BLOCK (solid backing so background text can't show through) ----
    display_title = topic.upper()
    if len(display_title) > 25:
        display_title = display_title[:25] + "..."

    title_bbox = draw.textbbox((0, 0), display_title, font=title_font)
    title_h = title_bbox[3] - title_bbox[1]
    title_y = 200

    # Solid band behind title + tagline
    draw.rectangle([(0, title_y - 30), (WIDTH, title_y + title_h + 130)], fill=(0, 0, 0, 220))

    draw.text((center_x(draw, display_title, title_font, WIDTH), title_y),
              display_title, fill="white", font=title_font)

    # ---- TAGLINE ----
    tagline = strip_emoji("Together We Can Make Change")
    draw.text((center_x(draw, tagline, text_font, WIDTH), title_y + title_h + 30),
              tagline, fill=(255, 215, 0), font=text_font)

    # ---- INFO BOX ----
    box_top, box_bottom = 880, 1330
    box_left, box_right = 70, 1010
    draw.rounded_rectangle([(box_left, box_top), (box_right, box_bottom)],
                            radius=35, fill=(0, 0, 0, 200))

    line_gap = 60
    start_y = box_top + 40

    fields = [
        f"Location: {location}",
        f"Date: {date}",
        f"Time: {time}",
        f"Venue: {venue}",
    ]

    for i, line in enumerate(fields):
        line = strip_emoji(line)
        draw.text((box_left + 50, start_y + i * line_gap),
                  line, fill="white", font=text_font)

    # ---- CTA BUTTON (fits inside box, below the fields) ----
    btn_y_top = start_y + len(fields) * line_gap + 20
    btn_y_bottom = btn_y_top + 70
    if btn_y_bottom > box_bottom - 20:
        btn_y_bottom = box_bottom - 20
        btn_y_top = btn_y_bottom - 70

    draw.rounded_rectangle([(360, btn_y_top), (720, btn_y_bottom)],
                            radius=25, fill=(255, 102, 0))

    cta = "JOIN NOW"
    draw.text((center_x(draw, cta, small_font, WIDTH), btn_y_top + 18),
              cta, fill="white", font=small_font)

    file_path = "poster.png"
    bg.convert("RGB").save(file_path)
    return file_path