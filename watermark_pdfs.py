import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from io import BytesIO
from PIL import Image

INPUT_FOLDER = "input_pdfs"
OUTPUT_FOLDER = "output_pdfs"
WATERMARK_IMAGE = "watermark.png"

def create_image_watermark(page_width, page_height):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(page_width, page_height))

    # Load the watermark image
    watermark_img = Image.open(WATERMARK_IMAGE)
    wm_width, wm_height = watermark_img.size

    img_width = 2.5 * inch  # Increased width
    img_height = (wm_height / wm_width) * img_width  # Maintain aspect ratio

    image = ImageReader(watermark_img)

    margin_x = 0.3 * inch
    margin_y = 0.3 * inch

    positions = [
        (margin_x, page_height - img_height - margin_y),                     # top-left
        (page_width - img_width - margin_x, page_height - img_height - margin_y),  # top-right
        (margin_x, margin_y),                                                # bottom-left
        (page_width - img_width - margin_x, margin_y),                       # bottom-right
    ]

    for x, y in positions:
        can.drawImage(image, x, y, width=img_width, height=img_height, mask='auto')

    can.save()
    packet.seek(0)
    return PdfReader(packet)

def apply_watermark_to_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)

        watermark_pdf = create_image_watermark(width, height)
        watermark_page = watermark_pdf.pages[0]

        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_path, "wb") as f_out:
        writer.write(f_out)

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".pdf")]

    for filename in pdf_files:
        input_pdf_path = os.path.join(INPUT_FOLDER, filename)
        output_pdf_path = os.path.join(OUTPUT_FOLDER, filename)

        print(f"Watermarking: {filename}")
        apply_watermark_to_pdf(input_pdf_path, output_pdf_path)

    print("✅ All PDFs watermarked with enlarged image successfully.")

if __name__ == "__main__":
    main()
