from tkinter import *

if __name__ == "__main__":
    # create a window instance
    root = Tk()
    root.title("Window: Button")
    # Label is a class for build texts, padx/pady: padding of x/y
    Label(root, text="My first button window").pack(pady=10)
    Button(root, text="Button 1").pack(side=LEFT)
    Button(root, text="Button 2").pack(side=LEFT)

    # entry of window
    root.mainloop()
