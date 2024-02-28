import random
import pyperclip
import tkinter as tk

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerics = "0123456789"
sp_chars = "!@#$%&*?"

Use_for = lower_case + upper_case + numerics + sp_chars

def generate_password():
    try:
        length_for_pass = int(length_entry.get())  # Get the length from the Entry widget
        global password 
        password = "".join(random.sample(Use_for, length_for_pass))
        password_display.config(text=password, fg="#ffffff", bg="#41B3A3")
    except ValueError:
        password_display.config(text="Invalid input", fg="red")  # Handle non-integer input

def copy_password():
    pyperclip.copy(password)  # Copy the displayed password

root = tk.Tk()
root.title("Password Generator")

title = tk.Label(root, text="Password Generator", font=("Helvetica", 20))
title.pack(pady=10)

length_label = tk.Label(root, text="Enter password length: ")
length_label.pack()

length_entry = tk.Entry(root)  # Entry widget for password length from user
length_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy", command=copy_password)
copy_button.pack(pady=5)

password_display = tk.Label(root, text="", font=("Helvetica", 18), background="#41B3A3", foreground="#ffffff")
password_display.pack(pady=20)

root.mainloop()

