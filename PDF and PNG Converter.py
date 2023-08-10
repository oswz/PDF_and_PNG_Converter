import os
from tkinter import Tk, Button, Label, Entry, filedialog, Radiobutton, StringVar
from pdf2image import convert_from_path
from fpdf import FPDF

def pdf_to_png(pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        image.save(image_path, "PNG")

def img_to_pdf(img_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf = FPDF()
    pdf.add_page()
    pdf.image(img_path, x=10, y=10, w=190)  # You might need to adjust the dimensions (:
    pdf.output(os.path.join(output_folder, "output.pdf"))

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Image Files", "*.png *.jpg")])
    if file_path:
        file_entry.delete(0, "end")
        file_entry.insert(0, file_path)

def convert_files():
    conversion_type = conversion_type_var.get()
    file_path = file_entry.get()

    if not file_path or not os.path.exists(file_path):
        status_label.config(text="Please select a valid file.")
        return

    output_folder = filedialog.askdirectory()
    if not output_folder:
        status_label.config(text="Output folder not selected.")
        return

    if conversion_type == "pdf_to_png":
        pdf_to_png(file_path, output_folder)
    elif conversion_type == "png_to_pdf":
        img_to_pdf(file_path, output_folder)
    
    status_label.config(text="Conversion complete.")


root = Tk()
root.title("PDF and PNG Converter by oswz")


root.geometry("400x200")  
root.resizable(False, False)  

conversion_type_var = StringVar()
conversion_type_var.set("pdf_to_png")

file_label = Label(root, text="File Path:")
file_label.pack()

file_entry = Entry(root, width=50)
file_entry.pack()

browse_button = Button(root, text="Browse", command=select_file)
browse_button.pack()

conversion_radio_pdf_to_png = Radiobutton(root, text="Convert PDF to PNG", variable=conversion_type_var, value="pdf_to_png")
conversion_radio_png_to_pdf = Radiobutton(root, text="Convert PNG to PDF", variable=conversion_type_var, value="png_to_pdf")

conversion_radio_pdf_to_png.pack()
conversion_radio_png_to_pdf.pack()

convert_button = Button(root, text="Convert", command=convert_files)
convert_button.pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
