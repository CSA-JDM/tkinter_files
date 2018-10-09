# Jacob Meadows
# Computer Programming II, 6th Period
# 01 October 2018
import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.config(width=330, height=320)
        self.master.title("Final Basic Widgets")
        super().__init__(self.master, width=330, height=320)
        self.place(x=0, y=0)

        self.widgets = dict()
        self.widget_init()

    def widget_init(self):
        self.widgets["print_scale"] = tk.Scale(self, from_=0, to=100, orient="horizontal")
        self.widgets["print_scale"].place(x=(self.config("width")[-1] - self.widgets["print_scale"].config("length")[-1])/2, y=0)
        self.widgets["print_spinbox"] = tk.Spinbox(self, from_=0, to=10)
        self.widgets["print_spinbox"].place(x=(self.config("width")[-1] - self.widgets["print_spinbox"].bbox(0)[-1])/2, y=50)
        self.widgets["ok_button"] = tk.Button(self, text="OK")
        self.widgets["ok_button"].place(x=0, y=80)
        self.widgets["close_button"] = tk.Button(self, text="Close")
        self.widgets["close_button"].place(x=0, y=110)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
