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
        self.widgets["file_menu"] = tk.Menu(self.widgets["menu"], tearoff=0)
        self.widgets["file_menu"].add_command(label="Save", command=lambda: None)
        self.widgets["file_menu"].add_command(label="Exit", command=self.quit)
        self.widgets["help_menu"] = tk.Menu(self.widgets["menu"], tearoff=0)
        self.widgets["help_menu"].add_command(label="About", command=self.about_command)
        self.widgets["menu"].add_cascade(label="File", menu=self.widgets["file_menu"])
        self.widgets["menu"].add_cascade(label="Help", menu=self.widgets["help_menu"])
        self.master.config(menu=self.widgets["menu"])
        self.widgets["countries_str_var"] = tk.StringVar(value=("USA", "Canada"))
        self.widgets["countries_listbox"] = tk.Listbox(self, listvariable=self.widgets["countries_str_var"])
        self.widgets["countries_scrollbar"] = tk.Scrollbar(self)

    def about_command(self):
        self.widgets["about_toplevel"] = tk.Toplevel(self)
        self.widgets["about_toplevel"].title("About")
        self.widgets["about_message"] = tk.Message(self.widgets["about_toplevel"], text="About")
        self.widgets["about_message"].pack()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
