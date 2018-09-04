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
                                     command=lambda: print("Red button!"))
        self.blue_button.pack(expand=True, fill=tk.BOTH)

        self.red_button = tk.Button(self.red_button_frame, text="RED", fg="red", bg="blue",
                                    command=lambda: print("Blue button!"))
        self.red_button.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    root = App()
    root.mainloop()
