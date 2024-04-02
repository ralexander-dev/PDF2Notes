import PyPDF2 as pdf
import pyautogui as pg
import GPT
import Writer as wr

def myReader(pdfPath, docxPath):
    pdfFile = open(pdfPath, 'rb')
    pdfReader = pdf.PdfReader(pdfFile)
    pdfText = ""

    for pageNum in range(len(pdfReader.pages)):

        page = pdfReader.pages[pageNum]
        pdfText = page.extract_text()
        
        if pdfText == "":
            print("No text could be extracted from the document. Ensure that the file is an original PDF and not a scanned document.")
        else:
            gptReply = GPT.CustomGPT(pdfText)

        checkFirstPage(pageNum)
        wr.saveNotes(docxPath, gptReply)
        print(f"Completed Page: {(pageNum+1):d} of {len(pdfReader.pages):d}")
    pdfFile.close()

def checkFirstPage(pageNum):
    if pageNum == 0:
        isReady = input("Press 'Enter' to begin.")
