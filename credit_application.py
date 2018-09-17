# Jacob Meadows
# Computer Programming, 6th Period
# September 14th, 2018
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        master.title("Credit Application")
        super().__init__(master)
        self.pack()
        self.config(width=1280, height=720)

        self.frames = dict()
        self.labels = dict()
        self.buttons = dict()
        self.radio_buttons = dict()
        self.entries = dict()
        self.int_vars = dict()
        self.str_vars = dict()

        self.labels["title_label"] = tk.Label(self, text="Credit Application")
        self.labels["title_label"].grid(column=0, row=0, columnspan=3, sticky="n")
        self.labels["name_label"] = tk.Label(self, text="Name")
        self.labels["name_label"].grid(column=1, row=1, sticky="w")
        self.labels["age_label"] = tk.Label(self, text="Age")
        self.labels["age_label"].grid(column=1, row=3, sticky="w")

        self.int_vars["loan_int"] = tk.IntVar()

        self.radio_buttons["car_radio_button"] = tk.Radiobutton(self, text="Car",
                                                                variable=self.int_vars["loan_int"], value=1)
        self.radio_buttons["car_radio_button"].grid(column=0, row=2, sticky="w")
        self.radio_buttons["house_radio_button"] = tk.Radiobutton(self, text="House",
                                                                  variable=self.int_vars["loan_int"], value=2)
        self.radio_buttons["house_radio_button"].grid(column=0, row=3, sticky="w")
        self.radio_buttons["personal_radio_button"] = tk.Radiobutton(self, text="Personal",
                                                                     variable=self.int_vars["loan_int"], value=3)
        self.radio_buttons["personal_radio_button"].grid(column=0, row=4, sticky="w")

        self.str_vars["name_str"] = tk.StringVar()
        self.entries["name_entry"] = tk.Entry(self, width=20, textvariable=self.str_vars["name_str"])
        self.entries["name_entry"].grid(column=1, row=2, sticky="w")
        self.str_vars["age_str"] = tk.StringVar()
        self.entries["age_entry"] = tk.Entry(self, width=5, textvariable=self.str_vars["age_str"])
        self.entries["age_entry"].grid(column=1, row=4, sticky="w")

        self.buttons["submit_button"] = tk.Button(self, text="Submit", state="disabled", command=self.submit_choices)
        self.buttons["submit_button"].grid(column=2, row=5)

        self.submit_check()

    def submit_check(self):
        if 0 not in [self.radio_buttons[x].getvar(self.radio_buttons[x].config("variable")[-1])
                     for x in self.radio_buttons.keys()]\
                and "" not in [self.entries[x].getvar(self.entries[x].config("textvariable")[-1])
                               for x in self.entries.keys()]:
            if "disabled" in self.buttons["submit_button"].config("state"):
                self.buttons["submit_button"].config(state="normal")
        else:
            self.buttons["submit_button"].config(state="disabled")
        self.after(1, self.submit_check)

    def submit_choices(self):
        global credit_info, credit_info_txt
        values = [[x, self.radio_buttons[x].getvar(self.radio_buttons[x].config("variable")[-1])]
                  for x in self.radio_buttons.keys()]
        credit_info_info = credit_info.split("\n")
        credit_info_info = [x.split(", ") for x in credit_info_info]
        credit_info_txt = open("credit_info.txt", "w")
        loan_option = values[values[-1][-1]-1][0].split("_")[0].title()
        name = [self.entries["name_entry"].getvar(self.entries["name_entry"].config("textvariable")[-1])][0]
        age = [self.entries["age_entry"].getvar(self.entries["age_entry"].config("textvariable")[-1])][0]
        credit_info_info = [", ".join(x) for x in credit_info_info]
        credit_info_info = "\n".join(credit_info_info)
        credit_info_info += f"{loan_option}, {name}, {age}\n"
        credit_info_txt.write(credit_info_info)
        credit_info_txt.close()
        credit_info_txt = open("credit_info.txt", "r")
        credit_info = credit_info_txt.read()
        credit_info_txt.close()


if __name__ == "__main__":
    try:
        credit_info_txt = open("credit_info.txt", "r")
    except FileNotFoundError:
        credit_info_txt = open("credit_info.txt", "w")
        credit_info_txt.close()
        credit_info_txt = open("credit_info.txt", "r")
    credit_info = credit_info_txt.read()
    credit_info_txt.close()

    root = tk.Tk()
    App(root)
    root.mainloop()
