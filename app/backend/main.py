import GPT
import FileManage as fm
import Reader as Read

GPT.configure()
src_folder = 'C:\\Users\\Alex\\PDFs'
dest_folder = 'C:\\Users\\Alex\\ConvertedPDFs'

print("This program converts your educational PDFs into AI generated notes.")
print("We'll begin by making sure the correct folders are setup...")

fm.checkFolderExistence(src_folder)
print("Source Folder Status: Ready")
fm.checkFolderExistence(dest_folder)
print("Destination Folder Status: Ready")

print("Available PDFs: ")
pdfPath = fm.getPDFList(src_folder)
docxPath = fm.createDocx(src_folder, pdfPath, dest_folder)
Read.myReader(pdfPath, docxPath)
