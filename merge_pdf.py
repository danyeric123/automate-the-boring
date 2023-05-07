from PyPDF2 import PdfFileMerger
import glob
from tkinter import Entry, Label, StringVar, Tk
from tkinter.filedialog import askopenfilename, askopenfilenames

Tk().withdraw()
filenames = askopenfilenames(
    title="Choose pdfs to merge", filetypes=[("PDF files", "*.pdf")]
)

merger = PdfFileMerger()

for file_ in filenames:
    merger.append(file_)


merger.write(f"merged.pdf")

merger.close()
