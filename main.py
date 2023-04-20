from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("txt-files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")


for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    title = filename.title()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=title, ln=1)

    with open(filepath, "r") as file:
        content = file.read()
    pdf.set_font(family="Arial", size=14)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")


