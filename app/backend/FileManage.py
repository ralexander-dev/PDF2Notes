import os

"""
    Check for the existence of necessary folders.
    **args:
        ~ folder - Path to a src folder containing PDFs, or a dest folder to store converted documents.
    **return:
        ~ None
"""
def checkFolderExistence(folder):

    if not os.path.exists(folder):

        select = (input(f"'{folder}' does not exist. Create it? (Y or N)")).lower()

        while (select != 'y') and (select != 'n'):
            select = (input("Invalid entry. Please enter 'Y' or 'N'. ")).lower()
        if select == 'y':
            os.makedirs(folder)
            print(f"The destination folder has been created. The path is {os.path.abspath(folder)}")
        else:
            print("Program cannot proceed without the missing i/o folder. Terminating...")
            exit(0)

"""
    List PDFs within the source folder for the user to select. Append the path to the selected PDF, then return it. 
    **args:
        ~ src_folder - Path to the source folder.
    **return:
        ~ pdfPath - Path to the .pdf file to be converted. 
"""
def getPDFList(src_folder):
    pdfList = []
    
    for i, fileName in enumerate(os.listdir(src_folder)):
        if fileName.endswith('.pdf'):
            pdfList.append(fileName)
            print(f"{i+1}) {fileName}")
        
    select = int(input("Enter the item number of the PDF to convert (0 to Exit): "))
    if select == 0: {exit(0)}
    print(pdfList)
    pdfPath = os.path.join(src_folder, pdfList[select-1])
    print(pdfPath)
    return pdfPath

"""
    Create a .docx file, carrying over the name of the source PDF.
    **args:
        ~ src_folder - Path to the source folder.
        ~ pdfPath - Path to the .pdf file to be converted.
        ~ dest_folder - Path to the destination folder.
    **return:
        ~ docx_path - Path to the new docx. 
"""
def createDocx(src_folder, pdfPath, dest_folder):
    select = (input("Enter the name of the new .docx file: (Leave Blank to Keep PDF Name)"))
    docxPath = pdfPath.replace('.pdf', '.docx')
    if select == '':
        docxPath = pdfPath.replace('.pdf', '.docx')
        docxPath = docxPath.replace(src_folder, dest_folder)
    else:
        docxPath = os.path.join(dest_folder, select + '.docx')
    return docxPath
