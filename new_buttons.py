# Jacob Meadows
# Computer Programming, 6th Period
# August 29th, 2018
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.top_text_frame = tk.Frame(self)
        self.top_text_frame.pack()

        self.blue_button_frame = tk.Frame(self, width=100, height=100)
        self.blue_button_frame.pack_propagate(0)
        self.blue_button_frame.pack()

        self.red_button_frame = tk.Frame(self, width=100, height=100)
        self.red_button_frame.pack_propagate(0)
        self.red_button_frame.pack()

        self.top_text = tk.Label(self.top_text_frame, text="The colored buttons window!")
        self.top_text.pack()

        self.blue_button = tk.Button(self.blue_button_frame, text="BLUE", fg="blue", bg="red",
                                     command=lambda: self.button_commands("blue_button"))
        self.blue_button.pack(expand=True, fill=tk.BOTH)

        self.red_button = tk.Button(self.red_button_frame, text="RED", fg="red", bg="blue",
                                    command=lambda: self.button_commands("red_button"))
        self.red_button.pack(expand=True, fill=tk.BOTH)

    def button_commands(self, button_name):
        if getattr(self, button_name).cget("fg") == "red":
            getattr(self, button_name).config(bg="red", fg="blue")
        elif getattr(self, button_name).cget("fg") == "blue":
            getattr(self, button_name).config(bg="blue", fg="red")


if __name__ == "__main__":
    root = App()
    root.mainloop()
