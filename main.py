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
    "Environmental Education",
    "Environmental Protection Organizations (India & Global)",
    "Practices for Environmental Protection",
    "Environmental Resources and Organizations",
    "Study of any one National/International Environmental Organization",
    "Visit and Report on Local Environmental NGO",
    "Plastic Pollution and Its Effects on the Environment",
    "Impact of Microplastics on the Environment",
    "Say No to Plastic Campaign",
    "Plastic Waste Disposal and Recycling",
    "Solid Waste Management (Local and General)",
    "Medical Waste Management",
    "E-Waste Management",
    "Waste Management (General Overview)",
    "Industrial Waste and Pollution",
    "Recycling of Treated Sewage and Waste Materials",
    "Water Security and Scarcity",
    "Water Pollution and Conservation",
    "Study of Local Water Resources or Dam",
    "Watershed Management",
    "Watershed Development Programme (Visit/Report)",
    "Water Conservation and Management",
    "Local Water Resources Survey",
    "Organic Farming and Use of Biofertilizers",
    "Inorganic Farming and Chemical Fertilizers",
    "Mixed Farming Practices",
    "Agricultural Pollution",
    "Sustainable Agriculture",
    "Study of Mixed Organic Practices",
    "Biodiversity (General Overview)",
    "Mangrove Biodiversity and Conservation",
    "Conservation of Biodiversity",
    "Conservation Biology",
    "Marine Ecosystem",
    "Study of Local Flora",
    "Loss of Biodiversity",
    "Global Warming",
    "Greenhouse Effect",
    "Solar Energy",
    "Wind Energy",
    "Thermal Power Plants (India/Maharashtra/Impact)",
    "Energy Audit",
    "Carbon Footprint",
    "Natural Disasters (India and Maharashtra)",
    "Man-made / Industrial Disasters",
    "Disaster Management (Including Floods, Earthquakes)",
    "Air Pollution (Vayu Pradushan)",
    "Noise Pollution",
    "Industrial Accidents and Disasters",
    "Nobel Peace Prize Winners (Environmental Focus)",
    "Study of at Least Two Environmental Nobel Laureates",
    "Environmental Movements in India",
    "Swachh Bharat Abhiyan",
    "Ecotourism and Eco-awareness Campaigns",
    "Say No to Plastic Movement",
    "Statewise Tribal Communities in India",
    "Tribal Communities Working Towards Environmental Protection",
    "Study of Local Community Traditions Related to Nature",
    "Local Community and Cultural Practices (Interview Elders)",
    "National Parks of India (Overview)",
    "Five National Parks of Maharashtra (Tabular Form)",
    "Forest and Natural Resource Conservation",
    "Environmental Impact of Plastic Bottles",
    "Effects of Plastic on Human Health (e.g., Cancer Risk)",
    "Sustainable Industries (Fashion, Bags, Cosmetics)",
    "Role of Environmental Laws and Policies"
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
