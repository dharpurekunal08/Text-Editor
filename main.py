# ************************************
# Python Text Editor
# ************************************
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *

def change_text_color():
    color = colorchooser.askcolor(title="Pick a text color")
    if color:
        text_area.config(fg=color[1])

def change_background_color():
    color = colorchooser.askcolor(title="Pick a background color")
    if color:
        text_area.config(bg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))

def new_file():
    text_area.delete(1.0, END)
    window.title("Untitled")

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])
    if file:
        try:
            window.title(os.path.basename(file))
            with open(file, "r") as file_content:
                text_area.delete(1.0, END)
                text_area.insert(1.0, file_content.read())
        except Exception as e:
            showerror("Error", f"Failed to open file: {e}")

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if file:
        try:
            window.title(os.path.basename(file))
            with open(file, "w") as file_content:
                file_content.write(text_area.get(1.0, END))
        except Exception as e:
            showerror("Error", f"Failed to save file: {e}")

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About", "This is a text editor created by Kunalll!")

def exit_editor():
    if askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()

# Create main window
window = tk.Tk()
window.title("KD Editor++")

#favicon
img = PhotoImage(file="notepad.png")
window.iconphoto(window, img)

# Set window size and position
window_width = 800
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Text area
text_area = Text(window, wrap="word", undo=True)
text_area.pack(fill="both", expand=True)

# Scrollbar
scroll_bar = Scrollbar(window, command=text_area.yview)
scroll_bar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scroll_bar.set)

# Menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# Format menu
format_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Change Text Color", command=change_text_color)
format_menu.add_command(label="Change Background Color", command=change_background_color)
format_menu.add_separator()

# Font menu
font_menu = Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font", menu=font_menu)

# Get available font families
font_families = font.families()
font_name = StringVar(window)
for family in font_families:
    font_menu.add_radiobutton(label=family, variable=font_name,
                               command=change_font, value=family)

# Font size submenu
font_size_menu = Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font Size", menu=font_size_menu)

# Define font sizes
font_size = IntVar(window)
font_sizes = [8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36, 40]
for size in font_sizes:
    font_size_menu.add_radiobutton(label=str(size), variable=font_size,
                                    command=change_font, value=size)

# Set default font and size
font_name.set("Arial")
font_size.set(12)
text_area.config(font=(font_name.get(), font_size.get()))

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Run the application
window.mainloop()
