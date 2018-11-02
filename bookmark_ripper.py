from PyPDF2 import PdfFileReader

with open(filename, 'rb') as f:
  p = PdfFileReader(f)

bookmarkdata = p.outlines
