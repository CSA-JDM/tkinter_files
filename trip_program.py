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
        self.widgets["menu"] = tk.Menu(self)
        self.widgets["hello_menu"] = tk.Menu(self.widgets["menu"], tearoff=0)
        self.widgets["menu"].add_cascade(label="Hello!", menu=self.widgets["hello_menu"])
        self.widgets["hello_menu"].add_command(label="Hello!!", command=lambda: tk.Label(self, text="Hello!!!").pack())
        self.widgets["menu"].add_command(label="Quit!", command=self.quit)
        self.master.config(menu=self.widgets["menu"])


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
