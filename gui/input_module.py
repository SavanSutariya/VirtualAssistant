import tkinter as tk
from tkinter import simpledialog
def gui_input(arg):
    application_window = tk.Tk()
    return simpledialog.askstring("Input", arg, parent=application_window)