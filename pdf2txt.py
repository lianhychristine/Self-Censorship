###### Convert PDF to Text using Python ######

# install the module via Terminal
# pip install PyPDF2

# importing required modules
import PyPDF2

# open a pdf file object
pdfFileObj = open(r'E:\RA\Self-Censorship\pdf2txt\reports\Technologies Equity Research Report.pdf', 'rb')  # PDF_file path

# create a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# print number of pages in the pdf file
lenDoc = len(pdfReader.pages)
print("Number of Pages in current doc:", lenDoc)

# extract text from each page
doc = []
i = 0
while i < lenDoc:
    pageObj = pdfReader.pages[i]  # create a page object
    page = pageObj.extract_text()  # extract text from the page
    doc.append(page+'\n')
    print("Current No. of page:", i)
    i = i + 1
else:
    print("Totol No. of pages in the document:", lenDoc)
    print(doc)  # display the whole document corpus

# write the corpus into a text file
file1 = open(r"E:\RA\Self-Censorship\pdf2txt\Technologies Equity Research Report_convertedtext.txt","w", encoding='utf-8')  # text_file path
file1.writelines(doc)

# closing the pdf file object
pdfFileObj.close()

# closing the text file object
file1.close()
