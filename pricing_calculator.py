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
        self.combo_boxes = dict()
        self.progress_bars = dict()
        self.labels = dict()
        self.buttons = dict()
        self.str_vars = dict()
        self.widgets = [self.list_boxes, self.combo_boxes, self.progress_bars, self.labels, self.buttons, self.str_vars]

        self.widget_init()
        self.submit_check()

    def widget_init(self):
        self.list_boxes["top_list_box"] = tk.Listbox(self)
        self.list_box_update(self.list_boxes["top_list_box"], "Python 3.6\nPython 3.7")
        self.list_boxes["top_list_box"].place(x=0, y=0)
        self.buttons["submit_button"] = tk.Button(self, text="Submit")
        self.buttons["submit_button"].place(x=5, y=500)
        self.buttons["clear_button"] = tk.Button(self, text="Clear")
        self.buttons["clear_button"].place(x=100, y=500)

    def submit_check(self):
        if None is not None:
            if "disabled" in self.buttons["submit_button"].config("state"):
                self.buttons["submit_button"].config(state="normal")
            else:
                self.buttons["submit_button"].config(state="disabled")
        self.after(1, self.submit_check)

    def clear_command(self):
        self.master.config(height=185)
        for widget in self.winfo_children():
            widget.place_forget()
        self.children.clear()
        for widget_dict in self.widgets:
            widget_dict.clear()
        self.widget_init()

    @staticmethod
    def list_box_update(list_box, text):
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
