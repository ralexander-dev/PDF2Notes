import GPT
import customtkinter as ctk
import Reader as Read
import tkinter as tk

ctk.set_default_color_theme("theme.json")
# Define GUI elements
class Root(ctk.CTk):
    # Define window attributes
    def __init__(self):
        super().__init__()
        self.title("PDF2Notes")
        self.geometry("800x800")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Define labels
        self.mainHeader = Label(self, 
            "This application allows you to convert PDFs to notes using the GPT-3 API. Simply select a PDF file and a location to save the notes.")

        # Define buttons
        self.readInSelectButton = Button(self, "Select PDF")
        self.runButton = Button(self, "Create Notes")

    # Define button actions
    def handle_PDF_Selection(self):
        # define event actions
        def on_click():
            try:
                # Present file dialog to user
                srcPath = tk.filedialog.askopenfile(mode='r', filetypes=[('PDF', '*.pdf')])
                srcPath.close() # Close the file to prevent file access errors
                self.runButton.configure(state="normal") # Enable the run button
                srcPath = srcPath.name # Store the file path in srcPath
                return srcPath 
            except AttributeError:
                return None
            
        # call on_click function so that its return value is stored in srcPath
        srcPath = on_click()
        if srcPath:
            self.readInSelectButton.selectedPath = srcPath # Store the file path in the button object

    def handle_docx_Selection(self):
        # define event actions
        def on_click():
            try:
                # Present file dialog to user
                destPath = tk.filedialog.asksaveasfile(mode='w', filetypes=[('Document', '*.docx')])
                destPath.close() # Close the file to prevent file access errors
                destPath = destPath.name # Store the file path in srcPath
                return destPath
            except AttributeError:
                return None
            
        # call on_click function so that its return value is stored in destPath
        destPath = on_click()
        if destPath:
            self.runButton.selectedPath = destPath # Store the file path in the button object

            readStatus = Read.myReader(self.readInSelectButton.selectedPath, self.runButton.selectedPath) # Call the PDF reader, passing both paths. Reader will call docx writer.
            if readStatus == 1:
                print("Error: No text could be extracted from the document. Ensure that the file is an original PDF and not a scanned document.")
                tk.messagebox.showerror("Error", "No text could be extracted from the document. Ensure that the file is an original PDF and not a scanned document.")
            else:
                print("Notes have been successfully created.")
                tk.messagebox.showinfo("Success", "Notes have been created and saved.")
                self.runButton.configure(state="disabled") # Disable the run button, as the user must select a new PDF to run the program again.
    # Load GUI elements
    def load(self):
        self.readInSelectButton.grid(row=1, column=0, padx=30, pady=50)
        self.readInSelectButton.configure(command=self.handle_PDF_Selection)

        self.runButton.grid(row=1, column=1, padx=30, pady=50)
        # Setup button to be disabled until a PDF is selected
        self.runButton.configure(command=self.handle_docx_Selection, state="disabled")

        self.mainHeader.grid(row=0, column=0, columnspan=2, padx=30, pady=50)

# Define button class
class Button(ctk.CTkButton):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.grid(sticky="nsew")
        self.configure(font=("Helvetica", 20))

class Label(ctk.CTkLabel):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.grid(sticky="nsew")
        self.configure(font=("Helvetica", 20))

# GPT API setup
GPT.configure()

# Run application
app = Root()
app.load()
app.mainloop()
