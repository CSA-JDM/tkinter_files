# Jacob Meadows
# Computer Programming II, 6th Period
# 01 October 2018
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.config(width=1280, height=720)
        super().__init__(self.master, width=1280, height=720)
        self.place(x=0, y=0)

        self.list_boxes = dict()
        self.str_vars = dict()

        self.list_boxes["top_list_box"] = tk.Listbox(self)
        self.list_box_update(self.list_boxes["top_list_box"], "Python 3.6\nPython 3.7")
        self.list_boxes["top_list_box"].place(x=0, y=0)

    def list_box_update(self, list_box, text):
        if isinstance(text, str):
            for string in text.split("\n"):
                list_box.insert(len(list_box.get(0, tk.END)), string)
        elif isinstance(text, list) or isinstance(text, tuple):
            for string in text:
                list_box.insert(len(list_box.get(0, tk.END)), string)

    def __str__(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
