import fitz  # PyMuPDF
from PyPDF2 import PdfWriter, PdfReader

# Step 1: Filter out image-only pages
doc = fitz.open("Jonathan-Livingston-Seagull.pdf")
printable_pages = []

for i, page in enumerate(doc):
    text = page.get_text().strip()
    images = page.get_images()
    if text or not images:
        printable_pages.append(i)

# Step 2: Write those pages into a new PDF
reader = PdfReader("Jonathan-Livingston-Seagull.pdf")
writer = PdfWriter()

for i in printable_pages:
    writer.add_page(reader.pages[i])

output_path = "printable_pages.pdf"
with open(output_path, "wb") as f:
    writer.write(f)
