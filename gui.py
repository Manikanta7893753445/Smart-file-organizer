import tkinter as tk
from tkinter import filedialog, messagebox
from file_utils import organize

def browse():
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)

def run():
    folder = entry.get().strip()
    if not folder:
        messagebox.showerror("Error","Select a folder.")
        return
    moved = organize(folder)
    messagebox.showinfo("Done", f"Organized {moved} files.")

root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("500x140")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root,text="Browse",command=browse).pack()
tk.Button(root,text="Organize Files",command=run).pack(pady=10)

root.mainloop()
