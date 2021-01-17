import PyPDF2
import sys
pdf = 'Lecture_Schedule2.pdf'
sys.stdout = open('output.txt','wt')
pFObject = open(pdf, 'rb')
pdfR = PyPDF2.PdfFileReader(pFObject)
c = pdfR.numPages
for i in range(c):
    page = pdfR.getPage(i)
    print(page.extractText())
