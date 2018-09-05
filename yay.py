# Jacob Meadows
# Computer Programming II, 6th Period
# September 4th, 2018
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(width=1280, height=720)
        self.pack_propagate(0)
        self.name = "Jacob"

        self.frames = {}
        self.labels = {}
        self.buttons = {}
        self.entries = {}

        self.frames["button_frame"] = tk.Frame(self)
        self.frames["button_frame"].pack(side=tk.LEFT)

        self.labels["output_label"] = tk.Label(self, text="Here")
        self.labels["output_label"].pack(side=tk.TOP)

        self.buttons["yay_button"] = tk.Button(self.frames["button_frame"], text="Yay!")
        self.buttons["yay_button"].grid(column=0, row=0, sticky=tk.W)

        self.buttons["boo_button"] = tk.Button(self.frames["button_frame"], text="Boo!")
        self.buttons["boo_button"].grid(column=0, row=1, sticky=tk.W)

        self.buttons["happy_button"] = tk.Button(
            self.frames["button_frame"], text="I'm Happy"
        )
        self.buttons["happy_button"].grid(column=0, row=2, sticky=tk.W)

    def __str__(self):
        pass


if __name__ == "__main__":
    root = App()
    root.mainloop()
    var = f"My name is {self.name}, I'm really, really, really happy!!!!!!!!1"  # todo make function