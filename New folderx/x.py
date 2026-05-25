from PyPDF2 import PdfMerger
import glob, os

folder = r"C:\Users\Rishabh Deb\Downloads\New folderw"
pdfs = glob.glob(os.path.join(folder, "*.pdf"))

merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)

merger.write(os.path.join(folder, "merged.pdf"))
merger.close()