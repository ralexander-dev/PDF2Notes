from docx import Document

def saveNotes(docxPath, text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(docxPath)
