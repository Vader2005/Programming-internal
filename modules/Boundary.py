from tkinter import *
from tkinter import messagebox

def error():
    messagebox.showerror("Error", "The closing price cannot exceed $500")

error()
