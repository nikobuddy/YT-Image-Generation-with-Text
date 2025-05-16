from PIL import Image, ImageDraw, ImageFont
import os

# Load the background image
bg_path = "bg.png"
background = Image.open(bg_path).convert("RGBA")

# Constants
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)

# List of topics (add more as needed)
topics = [
    "Rainwater Harvesting",
    "Waste Management",
    "Air Pollution",
    "Solar Energy"
]

# Text placement configuration
text_area_coords = (555, 258, 1150, 405)  # x1, y1, x2, y2
font_path = "DejaVuSans-Bold.ttf"  # Make sure this font is accessible in the same directory or give full path
font_size = 48

# Load font
font = ImageFont.truetype(font_path, font_size)

for topic in topics:
    # Create a copy of the background image
    img = background.copy()
    draw = ImageDraw.Draw(img)

    # Calculate bounding box for text
    bbox = draw.textbbox((0, 0), topic, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate center position
    text_x = text_area_coords[0] + (text_area_coords[2] - text_area_coords[0] - text_width) // 2
    text_y = text_area_coords[1] + (text_area_coords[3] - text_area_coords[1] - text_height) // 2

    # Draw text on image
    draw.text((text_x, text_y), topic, font=font, fill="white")

    # Save image
    safe_topic = topic.lower().replace(" ", "_")
    output_path = os.path.join(output_folder, f"{safe_topic}.png")
    img.save(output_path)

print("✅ All topic images generated successfully!")
