from PIL import Image, ImageDraw, ImageFont
import os

# Load the background image
bg_path = "bg.png"
background = Image.open(bg_path).convert("RGBA")

# Constants
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)

# Sample topic for demonstration
sample_topic = "Rainwater Harvesting"

# Text placement configuration
text_area_coords = (555, 258, 1150, 405)  # x1, y1, x2, y2
font_path = "DejaVuSans-Bold.ttf"
font_size = 48

# Create new image with topic text
img = background.copy()
draw = ImageDraw.Draw(img)

# Load font
font = ImageFont.truetype(font_path, font_size)

# Calculate text size and position
text = sample_topic
text_width, text_height = draw.textsize(text, font=font)
text_x = text_area_coords[0] + (text_area_coords[2] - text_area_coords[0] - text_width) // 2
text_y = text_area_coords[1] + (text_area_coords[3] - text_area_coords[1] - text_height) // 2

# Draw text
draw.text((text_x, text_y), text, font=font, fill="white")

# Save the image
output_path = os.path.join(output_folder, "sample_output.png")
img.save(output_path)

output_path
