# Jacob Meadows
# Computer Programming, 6th Period
# September 10th, 2018
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.buttons = dict()

        self.buttons["ok_button"] = tk.Button(self, text="OK", command=self.button_command)
        self.buttons["ok_button"].pack()
        self.buttons["not_ok_button"] = tk.Button(self, text="NOT OK", command=self.button_command, state=tk.DISABLED)
        self.buttons["not_ok_button"].pack()

    def button_command(self):
        for button in self.buttons.values():
            if "normal" in button.config("state"):
                button.config(state="disabled")
            elif "disabled" in button.config("state"):
                button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
