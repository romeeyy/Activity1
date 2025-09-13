from PIL import Image, ImageDraw, ImageFont
import random

# ================================
# Activity 1 – Trophy Poster Design
# BSCS 3B | Romelyn Pinoliad
# ================================

# Canvas
img = Image.new("RGB", (800, 950), "white")
draw = ImageDraw.Draw(img)

# --- Gradient Trophy Cup ---
for i in range(0, 250, 5):
    color = (255, 215 - i//10, 0)
    draw.ellipse((300-i//4, 200+i//8, 500+i//4, 450-i//8), fill=color, outline="black")

# --- Cup Shine (highlight) ---
draw.ellipse((350, 240, 390, 320), fill="yellow", outline=None)

# --- Trophy Stem ---
for i in range(0, 50, 2):
    color = (255, 200 - i//5, 0)
    draw.rectangle((370-i//5, 450+i, 430+i//5, 550+i), fill=color, outline="black")

# --- Handles ---
for offset in range(0, 20, 5):
    draw.arc((220-offset, 250, 320-offset, 420), start=90, end=270, fill="black", width=5)
    draw.arc((480+offset, 250, 580+offset, 420), start=-90, end=90, fill="black", width=5)

# --- Base ---
draw.rectangle((280, 600, 520, 650), fill="#8B4513", outline="black", width=5)
draw.rectangle((250, 650, 550, 700), fill="black", outline="black", width=5)

# --- Plaque (engraved plate) ---
draw.rectangle((320, 610, 480, 640), fill="#FFD700", outline="black", width=3)

# --- Award Text (on plaque) ---
award_text = "Best BSCS Spirit"
try:
    font = ImageFont.truetype("arialbd.ttf", 36)
except:
    font = ImageFont.load_default()

bbox = draw.textbbox((0, 0), award_text, font=font)
text_width = bbox[2] - bbox[0]
x = (800 - text_width) // 2
y = 730

# Shadow + Gold main text
draw.text((x+2, y+2), award_text, font=font, fill="black")
draw.text((x, y), award_text, font=font, fill="#FFD700")

# --- Title at the Top ---
title = "Intramurals 2025 Champion"
try:
    title_font = ImageFont.truetype("arialbd.ttf", 50)
except:
    title_font = ImageFont.load_default()

title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (800 - title_width) // 2
title_y = 40

# Shadow + Gold title
draw.text((title_x+3, title_y+3), title, font=title_font, fill="black")
draw.text((title_x, title_y), title, font=title_font, fill="#FFD700")

# --- Stars Around Trophy ---
try:
    star_font = ImageFont.truetype("arialbd.ttf", 30)
except:
    star_font = ImageFont.load_default()

star_positions = [(150, 180), (650, 180), (100, 400), (700, 400), (200, 100), (600, 100)]
for sx, sy in star_positions:
    draw.text((sx, sy), "★", font=star_font, fill="gold")

# --- Confetti (random celebration dots) ---
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
for _ in range(80):
    cx = random.randint(50, 750)
    cy = random.randint(50, 900)
    size = random.randint(3, 7)
    draw.ellipse((cx, cy, cx+size, cy+size), fill=random.choice(colors))


output_filename = "CSELEC3_3B_PinoliadRomelyn_Activity1.png"
img.save(output_filename)
img.show()

print(f" Trophy poster saved as {output_filename}")
