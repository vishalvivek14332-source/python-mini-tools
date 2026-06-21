import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())

        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        chars = string.ascii_letters

        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        if len(chars) == 0:
            messagebox.showerror("Error", "No characters selected!")
            return

        password = "".join(random.choice(chars) for _ in range(length))

        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")


# ---------------- UI SETUP ---------------- #

window = tk.Tk()
window.title("Password Generator")
window.geometry("350x250")
window.resizable(False, False)

# Title
tk.Label(window, text="🔐 Password Generator", font=("Arial", 16)).pack(pady=10)

# Length input
tk.Label(window, text="Password Length:").pack()
length_entry = tk.Entry(window)
length_entry.insert(0, "12")
length_entry.pack()

# Options
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(window, text="Include Digits", variable=digits_var).pack()
tk.Checkbutton(window, text="Include Symbols", variable=symbols_var).pack()

# Button
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

# Result display
result_var = tk.StringVar()

tk.Entry(window, textvariable=result_var, width=30, justify="center").pack(pady=5)

# Run app
window.mainloop()