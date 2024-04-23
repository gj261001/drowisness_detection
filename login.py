import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

# User credentials (you can replace these with your own)
credentials = {
    'admin': '123',
    'user2': 'password2'
}

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        execute_drowsiness()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def execute_drowsiness():
    python_executable = sys.executable  # Get the path to the current Python interpreter
    subprocess.run([python_executable, "detect_drowsiness.py"])

# Create main window
root = tk.Tk()
root.title("Login Page")

# Create username label and entry
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# Create password label and entry
label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=5, pady=5)

# Create login button
button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
