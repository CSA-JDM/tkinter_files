# Jacob Meadows
# Computer Programming II, 6th Period
# September 26th, 2018
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.config(width=200, height=60)
        self.master.title("Simple Grid")
        self.config(width=200, height=60)
        self.place(x=0, y=0)
        self.grid_propagate(0)

        self.frames = dict()
        self.labels = dict()
        self.buttons = dict()
        self.check_buttons = dict()
        self.combo_boxes = dict()
        self.entries = dict()
        self.radio_buttons = dict()
        self.str_vars = dict()
        self.int_vars = dict()
        self.vars = dict()
        self.widgets = [self.labels, self.buttons, self.check_buttons, self.combo_boxes, self.entries,
                        self.radio_buttons, self.str_vars, self.int_vars, self.vars]

        self.frames["main_frame"] = tk.Frame(self)
        self.frames["main_frame"].grid(column=0, row=0)
        self.labels["name_label"] = tk.Label(self.frames["main_frame"], text="Name")
        self.labels["name_label"].grid(column=0, row=0)
        self.str_vars["name_str"] = tk.StringVar()
        self.entries["name_entry"] = tk.Entry(self.frames["main_frame"], textvariable=self.str_vars["name_str"])
        self.entries["name_entry"].grid(column=1, row=0, columnspan=3)
        self.buttons["cancel_button"] = tk.Button(self.frames["main_frame"], text="Cancel", command=self.clear_name)
        self.buttons["cancel_button"].grid(column=0, row=1, pady=5)
        self.buttons["clear_button"] = tk.Button(self.frames["main_frame"], text="Clear", command=self.clear_name)
        self.buttons["clear_button"].grid(column=1, row=1, pady=5)
        self.buttons["submit_button"] = tk.Button(self.frames["main_frame"], text="Submit", command=self.clear_name)
        self.buttons["submit_button"].grid(column=2, row=1, pady=5)

        for column in range(self.grid_size()[0]):
            self.grid_columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.grid_rowconfigure(row, weight=1)

        self.update_frame()

    def clear_name(self):
        self.str_vars["name_str"].set("")

    def update_frame(self):
        if self.config("width")[-1] != self.master.geometry().split("x")[0]:
            self.config(width=self.master.geometry().split("x")[0])
        if self.config("height")[-1] != self.master.geometry().split("y")[0]:
            self.config(height=self.master.geometry().split("x")[1].split("+")[0])
        self.after(1, self.update_frame)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
