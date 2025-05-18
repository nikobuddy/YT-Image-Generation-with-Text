from PIL import Image, ImageDraw, ImageFont
import os
import re
import textwrap

# Load the background image
bg_path = "bg.png"
background = Image.open(bg_path).convert("RGBA")

# Constants
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)

# Topics list
topics = [
    "Environmental Protection and Conservation",
    "Role of Humans in Environmental Protection",
    
]

# Text area and font config
text_area_coords = (565, 298, 1150, 425)  # x1, y1, x2, y2
font_path = "DejaVuSans-Bold.ttf"
font_size = 30

# Load font
font = ImageFont.truetype(font_path, font_size)

def clean_filename(name):
    """Remove illegal filename characters."""
    return re.sub(r'[\\/:"*?<>|]+', "", name).lower().replace(" ", "_")

def draw_wrapped_text(draw, text, font, box, fill="white", max_lines=2):
    """Draw text inside a box, wrapping it to max_lines."""
    x1, y1, x2, y2 = box
    box_width = x2 - x1
    wrapped_lines = textwrap.wrap(text, width=25)  # Start with estimated width
    
    # Adjust to fit max lines and width
    for line_count in range(1, max_lines + 1):
        lines = textwrap.wrap(text, width=40 // line_count)
        if len(lines) <= max_lines:
            # Calculate total height
            line_height = sum([draw.textbbox((0, 0), l, font=font)[3] for l in lines])
            y_start = y1 + ((y2 - y1 - line_height) // 2)
            for i, line in enumerate(lines):
                text_width = draw.textbbox((0, 0), line, font=font)[2]
                x = x1 + ((box_width - text_width) // 2)
                y = y_start + i * (font_size + 5)
                draw.text((x, y), line, font=font, fill=fill)
            return

# Process all topics
for topic in topics:
    img = background.copy()
    draw = ImageDraw.Draw(img)

    # Draw wrapped topic in the text area
    draw_wrapped_text(draw, topic, font, text_area_coords)

    # Save the image
    safe_name = clean_filename(topic)
    output_path = os.path.join(output_folder, f"{safe_name}.png")
    img.save(output_path)

print("✅ All topic images created successfully.")
