import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    username = username_entry.get()
    messagebox.showinfo("Generated Credentials", f"Username: {username}\nPassword: {password}")

def main():
    global length_entry, username_entry
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("400x300")
    window.configure(bg="#F6D167")
    header_frame = tk.Frame(window, bg="#F8A170", pady=20)
    header_frame.pack(fill=tk.X)
    header_font = Font(family="Arial", size=24, weight="bold")
    header_label = tk.Label(header_frame, text="Password Generator", font=header_font, fg="#FFFFFF", bg="#F8A170")
    header_label.pack()
    username_label = tk.Label(window, text="Enter your username:", font=("Arial", 14), fg="#FF7F50")
    username_label.pack(pady=10)
    username_entry = tk.Entry(window, font=("Arial", 12))
    username_entry.pack()
    length_label = tk.Label(window, text="Enter the length of password needed:", font=("Arial", 14), fg="#FF7F50")
    length_label.pack(pady=10)
    length_entry = tk.Entry(window, font=("Arial", 12))
    length_entry.pack()
    generate_button = tk.Button(window, text="Generate Password", font=("Arial", 14, "bold"), fg="#FFFFFF", bg="#FF7F50", padx=10, pady=5, command=generate_password)
    generate_button.pack(pady=20)
    window.mainloop()

if __name__ == "__main__":
    main()
