# Jacob Meadows
# Computer Programming, 6th Period
# September 19th, 2018
import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, master):
        master.title("Simple Combobox")
        super().__init__(master)
        self.pack()
        self.config(width=1280, height=720)

        self.frames = dict()
        self.labels = dict()
        self.buttons = dict()
        self.combo_boxes = dict()
        self.entries = dict()
        self.int_vars = dict()
        self.str_vars = dict()

        self.labels["title_label"] = tk.Label(self, text="Choice")
        self.labels["title_label"].grid(column=0, row=0, columnspan=3, sticky="n")
        self.labels["season_label"] = tk.Label(self)
        self.labels["season_label"].grid(column=0, row=2)

        self.combo_boxes["seasons_combo_box"] = tk.ttk.Combobox(self, state="readonly", postcommand=self.focus_set,
                                                                values=["Spring", "Summer", "Fall", "Winter", "N/A"])
        self.combo_boxes["seasons_combo_box"].grid(column=0, row=1)

        self.combo_boxes["seasons_combo_box"].bind("<<ComboboxSelected>>", self.season_label_update)

    def season_label_update(self, event):
        self.labels["season_label"].config(text=self.combo_boxes["seasons_combo_box"].get())
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
