# Jacob Meadows
# Computer Programming II, 6th Period
# 01 October 2018
import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.config(width=330, height=320)
        self.master.title("Pricing")
        super().__init__(self.master, width=330, height=320)
        self.place(x=0, y=0)

        self.list_boxes = dict()
        self.combo_boxes = dict()
        self.progress_bars = dict()
        self.labels = dict()
        self.progress_bars = dict()
        self.buttons = dict()
        self.str_vars = dict()
        self.vars = dict()
        self.texts = dict()
        self.scroll_bars = dict()
        self.widgets = [self.list_boxes, self.combo_boxes, self.progress_bars, self.labels, self.buttons, self.str_vars,
                        self.vars, self.texts, self.scroll_bars]
        self.widget_init()
        self.widget_check()

    def widget_init(self):
        self.vars["item_dict"] = {"Rabbit": 5.00, "Guinea Pig": 4.00, "Hamster": 2.00,
                                  "Ferret": 6.00, "Parrot": 20.00, "Dog": 10.00, "Cat": 10.00,
                                  "Lizard": 6.00, "Zebra": 80.00, "Pig": 30.00, "Cow": 40.00, "Tiger": 120.00,
                                  "Lion": 120.00, "Boar": 40.00, "Crab": 50.00}
        self.str_vars["item_str"] = tk.StringVar(value=list(self.vars["item_dict"].keys()))
        self.combo_boxes["shipping_combo_box"] = tk.ttk.Combobox(self, values=["UPS", "FedEx", "Express"])
        self.combo_boxes["shipping_combo_box"].place(x=5, y=5)
        self.list_boxes["top_list_box"] = tk.Listbox(self, height=10, selectmode="multiple",
                                                     listvariable=self.str_vars["item_str"])
        self.scroll_bars["top_list_scroll_bar"] = tk.ttk.Scrollbar(self, orient="vertical",
                                                                   command=self.list_boxes["top_list_box"].yview)
        self.scroll_bars["top_list_scroll_bar"].place(in_=self.list_boxes["top_list_box"], x=105, y=-1.5,
                                                      relheight=1.025)
        self.list_boxes["top_list_box"].config(yscrollcommand=self.scroll_bars["top_list_scroll_bar"].set)
        self.list_boxes["top_list_box"].place(x=5, y=80)
        self.labels["notes_label"] = tk.Label(self, text="Notes")
        self.labels["notes_label"].place(x=165, y=60)
        self.texts["notes_entry"] = tk.Text(self, width=15, height=10)
        self.texts["notes_entry"].place(x=145, y=80)
        self.buttons["submit_button"] = tk.Button(self, text="Submit", command=self.submit_command)
        self.buttons["submit_button"].place(x=105, y=260)
        self.buttons["clear_button"] = tk.Button(self, text="Clear", command=self.clear_command)
        self.buttons["clear_button"].place(x=155, y=260)
        self.labels["price_label"] = tk.Label(self, text="Price:")
        self.labels["price_label"].place(x=5, y=260)
        self.str_vars["price_str"] = tk.StringVar(value="$0.00")
        self.labels["price_label"] = tk.Label(self, textvariable=self.str_vars["price_str"])
        self.labels["price_label"].place(x=55, y=260)
        self.progress_bars["shipping_progress_bar"] = tk.ttk.Progressbar(self, orient="vertical", length=300, value=0)
        self.progress_bars["shipping_progress_bar"].place(x=280, y=5)

    def widget_check(self):
        if 100 not in self.progress_bars["shipping_progress_bar"].config("value"):
            if self.combo_boxes["shipping_combo_box"].get() != "" and \
                    self.list_boxes["top_list_box"].curselection() != ():
                self.progress_bars["shipping_progress_bar"].config(value=66)
            elif self.combo_boxes["shipping_combo_box"].get() != "" or \
                    self.list_boxes["top_list_box"].curselection() != ():
                self.progress_bars["shipping_progress_bar"].config(value=33)
            else:
                self.progress_bars["shipping_progress_bar"].config(value=0)
        else:
            if self.combo_boxes["shipping_combo_box"].get() == "" and \
                    self.list_boxes["top_list_box"].curselection() == ():
                self.progress_bars["shipping_progress_bar"].config(value=0)
            elif self.combo_boxes["shipping_combo_box"].get() == "" or \
                    self.list_boxes["top_list_box"].curselection() == ():
                self.progress_bars["shipping_progress_bar"].config(value=33)
        self.after(1, self.widget_check)

    def submit_command(self):
        if self.combo_boxes["shipping_combo_box"].get() != "" and self.list_boxes["top_list_box"].curselection() != ():
            self.progress_bars["shipping_progress_bar"].config(value=100)
            if "error_label" in self.labels:
                self.labels["error_label"].place_forget()
            self.str_vars["price_str"].set(
                f"""${sum([self.vars['item_dict'][self.list_boxes['top_list_box'].get(x)]
                for x in self.list_boxes['top_list_box'].curselection()])}"""
            )
        else:
            self.labels["error_label"] = tk.Label(self, text="Error, incomplete portions.")
            self.labels["error_label"].place(x=5, y=290)

    def clear_command(self):
        for widget in self.winfo_children():
            widget.place_forget()
        self.children.clear()
        for widget_dict in self.widgets:
            widget_dict.clear()
        self.widget_init()


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
