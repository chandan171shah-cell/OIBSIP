import tkinter as tk
from tkinter import messagebox
import random
random.choice("abc123@#$")
import string
string.ascii_letters   # A-Z,a-z
string.digits          # 0-9
string.punctuation     # !@#$%
import pyperclip
pyperclip.copy("generate_password")

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        characters = ""
        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type!")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length!")

# Function to copy password to clipboard
def copy_password():
    password = result_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# ----------------Tkinter GUI Design ----------------
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Random Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

# Password length input
tk.Label(root, text="Enter Password Length:", font=("Arial", 10)).pack()
length_entry = tk.Entry(root, width=10, justify='center')
length_entry.pack(pady=5)

# Checkboxes for character types
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=letters_var).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="Include Symbols (!@#$%^&*)", variable=symbols_var).pack(anchor="w", padx=80)

# Buttons
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", width=20).pack(pady=10)

# Result entry box
result_entry = tk.Entry(root, width=35, font=("Arial", 12), justify='center')
result_entry.pack(pady=10)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="#2196F3", fg="white", width=20).pack(pady=5)

# Footer
tk.Label(root,font=("Arial", 8, "italic")).pack(side="bottom", pady=10)

root.mainloop()