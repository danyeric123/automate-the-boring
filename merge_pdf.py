from PyPDF2 import PdfFileMerger
import glob

files = glob.glob('pdfs/*.pdf')
merger = PdfFileMerger()

for file_ in files:
  merger.append(file_)

merger.write('merged.pdf')
merger.close()