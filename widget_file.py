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

        self.str_vars["top_str"] = tk.StringVar(value="Python 3.7\n Python 3.6")
        self.list_boxes["top_list_box"] = tk.Listbox(self, listvariable=self.str_vars["top_str"])
        self.list_boxes["top_list_box"].place(x=0, y=0)
        # self.str_vars["top_str"].get().split("\n") < is how you connect the exported index to the string var value.

        self.list_box_update()

    def list_box_update(self):
        for list_box in self.list_boxes.values():
            self.str_vars.values()[]
        self.after(1, self.list_box_update)

    def __str__(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
