# Jacob Meadows
# Computer Programming II, 6th Period
# September 19th, 2018
import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.config(width=240, height=185)
        self.master.title("Create User")
        self.config(width=1280, height=720)
        self.place(x=0, y=0)

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

        self.widget_init()

    def widget_init(self):
        self.str_vars["username_str"] = tk.StringVar()
        self.labels["username_label"] = tk.Label(self, text="Username:")
        self.labels["username_label"].place(x=5, y=5)
        self.entries["username_entry"] = tk.Entry(self, textvariable=self.str_vars["username_str"])
        self.entries["username_entry"].place(x=75, y=5)

        self.labels["password_label"] = tk.Label(self, text="Password:")
        self.labels["password_label"].place(x=5, y=35)
        self.str_vars["password_str"] = tk.StringVar()
        self.entries["password_entry"] = tk.Entry(self, textvariable=self.str_vars["password_str"], show="*")
        self.entries["password_entry"].place(x=75, y=35)

        self.labels["sex_label"] = tk.Label(self, text="Sex:")
        self.labels["sex_label"].place(x=5, y=65)
        self.int_vars["sex_int"] = tk.IntVar()
        self.radio_buttons["male_radio_button"] = tk.Radiobutton(self, text="Male", value=1,
                                                                 var=self.int_vars["sex_int"])
        self.radio_buttons["male_radio_button"].place(x=35, y=65)
        self.radio_buttons["female_radio_button"] = tk.Radiobutton(self, text="Female", value=2,
                                                                   var=self.int_vars["sex_int"])
        self.radio_buttons["female_radio_button"].place(x=95, y=65)

        self.int_vars["user_type_int"] = tk.IntVar()
        self.check_buttons["admin_check_button"] = tk.Checkbutton(self, text="Admin", onvalue=1,
                                                                  variable=self.int_vars["user_type_int"])
        self.check_buttons["admin_check_button"].place(x=5, y=95)
        self.check_buttons["user_check_button"] = tk.Checkbutton(self, text="User", onvalue=2,
                                                                 variable=self.int_vars["user_type_int"])
        self.check_buttons["user_check_button"].place(x=65, y=95)
        self.check_buttons["guest_check_button"] = tk.Checkbutton(self, text="Guest", onvalue=3,
                                                                  variable=self.int_vars["user_type_int"])
        self.check_buttons["guest_check_button"].place(x=115, y=95)

        self.combo_boxes["department_combo_box"] = tk.ttk.Combobox(self,
                                                                   values=["IT", "HR", "Sales", "Maintenance", "Other"],
                                                                   state="readonly")
        self.combo_boxes["department_combo_box"].place(x=5, y=125)

        self.buttons["submit_button"] = tk.Button(self, text="Submit", command=self.submit_command)
        self.buttons["submit_button"].place(x=5, y=155)

        self.buttons["clear_button"] = tk.Button(self, text="Clear", command=self.clear_command)
        self.buttons["clear_button"].place(x=65, y=155)

    def password_update(self):
        password_len = len(self.str_vars["password_str"].get())
        if len(self.vars["password_var"]) < password_len:
            self.vars["password_var"] += self.str_vars["password_str"].get()[-1]
        elif len(self.vars["password_var"]) > password_len:
            self.vars["password_var"] = self.vars["password_var"][:-1]
        self.entries["password_entry"].delete(0, tk.END)
        self.entries["password_entry"].insert(0, "*" * password_len if password_len > 0 else "")

    def clear_command(self):
        self.master.config(height=185)
        for widget in self.winfo_children():
            widget.place_forget()
        self.children.clear()
        for widget_dict in self.widgets:
            widget_dict.clear()
        self.widget_init()

    def submit_command(self):
        global database_data_txt, database_data
        self.master.config(height=215)
        if "submit_label" not in self.labels:
            for widget in self.winfo_children():
                widget.place_configure(y=widget.winfo_y() + 30)
            self.labels["submit_label"] = tk.Label(self)
            self.labels["submit_label"].place(x=5, y=5)
        if self.str_vars["username_str"].get() != "" and self.str_vars["password_str"].get() != "" and self.int_vars["sex_int"].get() != 0 and \
                self.int_vars["user_type_int"].get() != 0 and self.combo_boxes["department_combo_box"].get() != "":
            database_data_txt = open("database_data.txt", "w")
            database_data_txt.write(database_data +
                                    f"{self.str_vars['username_str'].get()} "
                                    f"{self.str_vars['password_str'].get()} "
                                    f"{'Male' if self.int_vars['sex_int'].get() == 1 else 'Female'} "
                                    f"{['Admin', 'User', 'Guest'][self.int_vars['user_type_int'].get() - 1]} "
                                    f"{self.combo_boxes['department_combo_box'].get()}\n")
            database_data_txt.close()
            database_data_txt = open("database_data.txt", "r")
            database_data = database_data_txt.read()
            database_data_txt.close()
            self.labels["submit_label"].config(text="User Created")
        elif "Error" not in self.labels["submit_label"].config("text"):
            self.labels["submit_label"].config(text="Error")


if __name__ == "__main__":
    try:
        database_data_txt = open("database_data.txt", "r")
    except FileNotFoundError:
        database_data_txt = open("database_data.txt", "w")
        database_data_txt.close()
        database_data_txt = open("database_data.txt", "r")
    database_data = database_data_txt.read()
    root = tk.Tk()
    App(root)
    root.mainloop()
