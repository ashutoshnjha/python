

#It mereges pdf files. Script verified with Python 2.7.17 && Python 3.6.9
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

__author__ = "Ashutosh Narayan Jha"
__copyright__ = "Copyright 2019, http://www.ignitedpeople.com/"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Ashutosh Narayan Jha"
__status__ = "Development"

filePathDirectory="/home/ashu/pdf_slips"

outPutFileName = "ashu_combined.pdf"

#Get all the PDFs to merge
pdfFiles = []
for filename in os.listdir(filePathDirectory):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

#Sort it by name.
pdfFiles.sort()

pdfMergerObj = PdfFileMerger()
 
# Iterate all files and append to merger.
for filename in pdfFiles:
    filename = os.path.join(filePathDirectory, filename)
    print("Reading: " + filename);
    pdfMergerObj.append(PdfFileReader(filename, 'rb'))
 
#Write combined output
pdfMergerObj.write(outPutFileName)
