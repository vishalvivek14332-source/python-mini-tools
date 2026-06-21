import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
}


def organize_folder():
    folder_path = folder_var.get()

    if not folder_path:
        messagebox.showerror("Error", "Please select a folder.")
        return

    moved_count = 0

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()
        destination = "Others"

        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                destination = category
                break

        destination_folder = os.path.join(folder_path, destination)
        os.makedirs(destination_folder, exist_ok=True)

        try:
            shutil.move(file_path, os.path.join(destination_folder, file))
            moved_count += 1
        except Exception as e:
            print(f"Error moving {file}: {e}")

    messagebox.showinfo(
        "Success",
        f"Organized {moved_count} files successfully!"
    )


def browse_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_var.set(folder)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("File Organizer")
root.geometry("500x220")
root.resizable(False, False)

title = tk.Label(
    root,
    text="📁 File Organizer",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

folder_var = tk.StringVar()

folder_entry = tk.Entry(
    root,
    textvariable=folder_var,
    width=50
)
folder_entry.pack(pady=5)

browse_btn = tk.Button(
    root,
    text="Browse Folder",
    command=browse_folder
)
browse_btn.pack(pady=5)

organize_btn = tk.Button(
    root,
    text="Organize Files",
    command=organize_folder,
    width=20,
    height=2
)
organize_btn.pack(pady=20)

root.mainloop()