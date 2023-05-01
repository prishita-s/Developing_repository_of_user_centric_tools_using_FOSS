import tkinter as tk
from tkinter import filedialog
import subprocess
import PyPDF2
from docx import Document

root = tk.Tk()
root.title("PDF to DOC & DOC to PDF Converter")

def convert_to_doc():
    input_file = filedialog.askopenfilename(title="Select PDF File", filetypes=(("PDF Files", "*.pdf"),))
    pdf_file = open(input_file, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    docx_document = Document()
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        docx_document.add_paragraph(text)
    docx_document.save('output.docx')
    output_label.configure(text='Conversion successful!')

def convert_to_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
    if file_path:
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf")
        if output_file:
            subprocess.call(["pandoc", file_path, "-o", output_file], shell=True)
            output_label.configure(text='Conversion successful!')

pdf_to_doc_button = tk.Button(root, text="Convert PDF to DOC", command=convert_to_doc,bg ="#E8D579")
pdf_to_doc_button.pack(pady=10)

doc_to_pdf_button = tk.Button(root, text="Convert DOC to PDF", command=convert_to_pdf,bg ="#E8D579")
doc_to_pdf_button.pack(pady=10)

output_label = tk.Label(root, text='')
output_label.pack()
root.geometry("200x150")
root.title("File Format Convertor")
root.config(background = "black")
root.eval('tk::PlaceWindow . center')
root.mainloop()
