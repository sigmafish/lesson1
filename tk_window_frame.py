from tkinter import *

if __name__ == "__main__":
    # create a window instance
    root = Tk()
    root.title("Window: Frame")
##    # Label is a class for build texts, padx/pady: padding of x/y to uperlayer
##    Label(root, text="Label is a class for build texts").pack(padx=100, pady=10)
    for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
        fm=Frame(root, borderwidth=2, relief=relief)
        Label(fm, text=relief, width=10).pack(side=LEFT)
        # packing the frame
        fm.pack(side=LEFT, padx=5, pady=5)
    # entry of window
    root.mainloop()