import PyPDF2 as pdf
import GPT
import Writer as wr

"""
    This function reads a PDF and extracts text from each page. It then calls the GPT API to generate notes from the text before saving the notes to a .docx file.
"""
def myReader(pdfPath, docxPath):
    # Open PDF file
    pdfFile = open(pdfPath, 'rb')
    pdfReader = pdf.PdfReader(pdfFile)
    pdfText = ""

    # For each page in PDF...
    for pageNum in range(len(pdfReader.pages)):
        
        # Extract text from PDF page
        page = pdfReader.pages[pageNum]
        pdfText = page.extract_text()
        
        # Check for unreadable or blank pages
        if pdfText == "":
            print("No text could be extracted from the document. Ensure that the file is an original PDF and not a scanned document.")
            return 1
        # if readable, call GPT API to translate page
        else:
            gptReply = GPT.CustomGPT(pdfText)

        # Write GPT notes to .docx
        wr.saveNotes(docxPath, gptReply)
        print(f"Completed Page: {(pageNum+1):d} of {len(pdfReader.pages):d}")
    pdfFile.close() # Close PDF file
    return 0

