###### Convert Multiple PDFs to TXTs using Python #######
############## (as of: 26 April 2023) ###################



# 1. Set up the following directory structure:
"""
    main.py
    pdfs
      ├─a.pdf
      ├─b.pdf
      └─c.pdf
    txts
"""


# 2. Install the module via Terminal
    # pip install PyPDF2


# 3. Main function
def main():

    from pathlib import Path
    import PyPDF2

    # create a list of converted PDF documents
    lst = []

    for path in Path("pdfs").glob("*.pdf"):

        # open a pdf file to be converted
        with path.open('rb') as file:
            # create a pdf_reader object
            pdfReader = PyPDF2.PdfReader(file)
            # no. of pages in the pdf object
            lenDoc = len(pdfReader.pages)
            # extract text from each page
            doc = []
            i = 0
            while i < lenDoc:
                # create a page object
                pageObj = pdfReader.pages[i]
                # extract text from the page
                page = pageObj.extract_text()
                doc.append(page + '\n')
                i = i + 1
            else:
                print("Document Name:", path.name)
                print("Total No. of pages in the document:", lenDoc)

        # write the corpus into a text file
        with open("txts/{}.txt".format(path.stem), 'w', encoding='utf-8') as file1:
            file1.writelines(doc)

        # update the list of converted documents
        lst.append(path.name + '\n')

    with open("List_of_Converted_Reports.txt", 'w', encoding='utf-8') as file2:
        file2.writelines(lst)

    return 0


# 4. Call the function
if __name__ == "__main__":
    import sys
    sys.exit(main())



###### END ######
