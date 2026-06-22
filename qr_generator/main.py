import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode


def generate_qr():
    data = text_entry.get()

    if not data:
        messagebox.showerror("Error", "Please enter text or a URL.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )

    if not file_path:
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    messagebox.showinfo(
        "Success",
        f"QR Code saved successfully!\n\n{file_path}"
    )


# GUI
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x220")
root.resizable(False, False)

title = tk.Label(
    root,
    text="🔳 QR Code Generator",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Label(
    root,
    text="Enter Text or URL:"
).pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=10)

generate_btn = tk.Button(
    root,
    text="Generate QR Code",
    command=generate_qr,
    width=20,
    height=2
)
generate_btn.pack(pady=20)

root.mainloop()