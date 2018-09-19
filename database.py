# Jacob Meadows
# Computer Programming II, 6th Period
# September 19th, 2018
import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.config(width=1280, height=720)
        self.master.title("Create User")
        self.config(width=1280, height=720)
        self.place(x=0, y=0)

        self.labels = dict()
        self.buttons = dict()
        self.entries = dict()
        self.radio_buttons = dict()
        self.str_vars = dict()
        self.int_vars = dict()
        self.vars = dict()

        self.labels["username_label"] = tk.Label(self, text="Username:")
        self.labels["username_label"].place(x=5, y=5)
        self.entries["username_entry"] = tk.Entry(self)
        self.entries["username_entry"].place(x=75, y=5)

        self.labels["password_label"] = tk.Label(self, text="Password:")
        self.labels["password_label"].place(x=5, y=35)
        self.str_vars["password_str"] = tk.StringVar()
        self.entries["password_entry"] = tk.Entry(self, textvariable=self.str_vars["password_str"])
        self.vars["password_var"] = ""
        self.entries["password_entry"].bind("<Key>", lambda event: self.after(1, self.password_update))
        self.entries["password_entry"].place(x=75, y=35)

        self.labels["sex_label"] = tk.Label(self, text="Sex:")
        self.labels["sex_label"].place(x=5, y=65)
        self.int_vars["sex_int"] = tk.IntVar()
        self.radio_buttons["male_radio_button"] = tk.Radiobutton(self, text="Male", value=1)
        self.radio_buttons["male_radio_button"].place(x=35, y=65)
        self.radio_buttons["female_radio_button"] = tk.Radiobutton(self, text="Female", value=2)
        self.radio_buttons["female_radio_button"].place(x=95, y=65)

    def password_update(self):
        password_len = len(self.str_vars["password_str"].get())
        if len(self.vars["password_var"]) < password_len:
            self.vars["password_var"] += self.str_vars["password_str"].get()[-1]
        elif len(self.vars["password_var"]) > password_len:
            self.vars["password_var"] = self.vars["password_var"][:-1]
        self.entries["password_entry"].delete(0, tk.END)
        self.entries["password_entry"].insert(0, "*" * password_len if password_len > 0 else "")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
