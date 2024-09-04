# Main.py

import tkinter as tk
from tkinter import Frame

class MainMenu(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Main Menu")
        # Adicione widgets e lógica aqui
