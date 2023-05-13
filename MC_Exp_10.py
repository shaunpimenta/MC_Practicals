import tkinter as tk
from tkinter import colorchooser

class FontModifier:
    def __init__(self, master):
        self.master = master
        master.title("Font Modifier")
        
        self.font_size = tk.Scale(master, from_=10, to=50, orient=tk.HORIZONTAL, label="Font Size", command=self.update_font)
        self.font_size.pack()
        
        self.font_color_button = tk.Button(master, text="Font Color", command=self.choose_color)
        self.font_color_button.pack()
        
        self.label = tk.Label(master, text="Hello, world!", font=("Arial", 20))
        self.label.pack()
        
    def update_font(self, value):
        self.label.config(font=("Arial", int(value)))
        
    def choose_color(self):
        color = colorchooser.askcolor()[1]
        self.label.config(fg=color)

root = tk.Tk()
my_gui = FontModifier(root)
root.mainloop()