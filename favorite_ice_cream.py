# Jacob Meadows
# Computer Programming, 6th Period
# September 11th, 2018
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.config(width=1280, height=720)

        self.frames = dict()
        self.labels = dict()
        self.buttons = dict()
        self.check_buttons = dict()
        self.entries = dict()
        self.int_vars = dict()

        self.labels["title_label"] = tk.Label(self, text="Checkbuttons")
        self.labels["title_label"].pack()

        self.int_vars["chocolate_state"] = tk.IntVar()
        self.check_buttons["chocolate_check_button"] = tk.Checkbutton(self, text="Chocolate",
                                                                      variable=self.int_vars["chocolate_state"])
        self.check_buttons["chocolate_check_button"].pack()
        self.int_vars["vanilla_state"] = tk.IntVar()
        self.check_buttons["vanilla_check_button"] = tk.Checkbutton(self, text="Vanilla",
                                                                    variable=self.int_vars["vanilla_state"])
        self.check_buttons["vanilla_check_button"].pack()
        self.int_vars["mint_state"] = tk.IntVar()
        self.check_buttons["mint_check_button"] = tk.Checkbutton(self, text="Mint",
                                                                 variable=self.int_vars["mint_state"])
        self.check_buttons["mint_check_button"].pack()
        self.int_vars["cookie_state"] = tk.IntVar()
        self.check_buttons["cookie_check_button"] = tk.Checkbutton(self, text="Cookie",
                                                                   variable=self.int_vars["cookie_state"])
        self.check_buttons["cookie_check_button"].pack()
        self.int_vars["strawberry_state"] = tk.IntVar()
        self.check_buttons["strawberry_check_button"] = tk.Checkbutton(self, text="Strawberry",
                                                                       variable=self.int_vars["strawberry_state"])
        self.check_buttons["strawberry_check_button"].pack()

        self.buttons["submit_button"] = tk.Button(self, text="Submit", state="disabled", command=self.submit_choices)
        self.buttons["submit_button"].pack(side="right")
        self.buttons["clear_button"] = tk.Button(self, text="Clear", state="disabled", command=self.clear_choices)
        self.buttons["clear_button"].pack(side="right")

        self.clear_and_submit_check()

    def clear_and_submit_check(self):
        if 1 in [self.int_vars[f'{x.split("_")[0]}_state'].get() for x in self.check_buttons.keys()]:
            if "disabled" in self.buttons["submit_button"].config("state") and\
                    "disabled" in self.buttons["clear_button"].config("state"):
                self.buttons["submit_button"].config(state="normal")
                self.buttons["clear_button"].config(state="normal")
        else:
            self.buttons["submit_button"].config(state="disabled")
            self.buttons["clear_button"].config(state="disabled")
        self.after(1, self.clear_and_submit_check)

    def submit_choices(self):
        global favorite_ice_txt, favorite_ice_info
        values = [[x, self.int_vars[f'{x.split("_")[0]}_state'].get()] for x in self.check_buttons.keys()]
        favorite_ice_flavors = favorite_ice_info.split("\n")
        favorite_ice_flavors = [x.split(": ") for x in favorite_ice_flavors]
        for name, value in values:
            if value == 1:
                favorite_ice_flavors[
                    [x for x in range(len(favorite_ice_flavors)) if favorite_ice_flavors[x][0] == name.split("_")[0]][
                        0]][1] = int(favorite_ice_flavors[[x for x in range(len(favorite_ice_flavors))
                                                           if favorite_ice_flavors[x][0] == name.split("_")[0]][0]][1])
                favorite_ice_flavors[[x for x in range(len(favorite_ice_flavors))
                                      if favorite_ice_flavors[x][0] == name.split("_")[0]][0]][1] += 1
                favorite_ice_flavors[[x for x in range(len(favorite_ice_flavors))
                                      if favorite_ice_flavors[x][0] == name.split("_")[0]][0]][1] = \
                    str(favorite_ice_flavors[[x for x in range(len(favorite_ice_flavors))
                                              if favorite_ice_flavors[x][0] == name.split("_")[0]][0]][1])
        favorite_ice_txt = open("favorite_ice.txt", "w")
        favorite_ice_flavors = [": ".join(x) for x in favorite_ice_flavors]
        favorite_ice_flavors = "\n".join(favorite_ice_flavors)
        favorite_ice_txt.write(favorite_ice_flavors)
        favorite_ice_txt.close()
        favorite_ice_txt = open("favorite_ice.txt", "r")
        favorite_ice_info = favorite_ice_txt.read()
        favorite_ice_txt.close()

    def clear_choices(self):
        for x in self.check_buttons.keys():
            self.int_vars[f'{x.split("_")[0]}_state'].set(0)


if __name__ == "__main__":
    try:
        favorite_ice_txt = open("favorite_ice.txt", "r")
    except FileNotFoundError:
        favorite_ice_txt = open("favorite_ice.txt", "w")
        favorite_ice_txt.write("chocolate: 0\n"
                               "vanilla: 0\n"
                               "mint: 0\n"
                               "cookie: 0\n"
                               "strawberry: 0")
        favorite_ice_txt.close()
        favorite_ice_txt = open("favorite_ice.txt", "r")
    favorite_ice_info = favorite_ice_txt.read()
    favorite_ice_txt.close()

    root = tk.Tk()
    App(root)
    root.mainloop()
