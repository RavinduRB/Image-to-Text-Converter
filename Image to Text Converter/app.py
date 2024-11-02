import tkinter as tk
from tkinter import filedialog, Text, messagebox
from PIL import Image
import pytesseract

# Set the Tesseract command path here
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path if different

# Initialize the main app window
root = tk.Tk()
root.title("Image to Text Converter")
root.geometry("600x400")

# Function to open and select an image
def open_file():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )
    if file_path:
        extract_text(file_path)

# Function to extract text from the selected image
def extract_text(file_path):
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        display_text.delete(1.0, tk.END)  # Clear previous text
        display_text.insert(tk.END, text)  # Insert new text
    except Exception as e:
        messagebox.showerror("Error", f"Could not process the image: {e}")

# Button to open an image file
open_button = tk.Button(root, text="Open Image", command=open_file, font=("Arial", 12))
open_button.pack(pady=20)

# Text box to display extracted text
display_text = Text(root, wrap="word", font=("Arial", 10), width=60, height=15)
display_text.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
