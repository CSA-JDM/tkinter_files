# Jacob Meadows
# Computer Programming, 6th Period
# August 27th, 2018
import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.quit_button = tk.Button(self.frame, text="Quit", fg="red", command=self.frame.quit)
        self.quit_button.pack(side=tk.LEFT)

        self.hello_button = tk.Button(self.frame, text="Hello", command=self.say_hi)
        self.hello_button.pack(side=tk.LEFT)

    @staticmethod
    def say_hi():
        print("Hi there, everyone!")


if "__main__" == __name__:
    root = tk.Tk()
    App(root)
    root.mainloop()
    root.destroy()
