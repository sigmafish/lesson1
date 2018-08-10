from tkinter import *

btn1=None

def setFrame(window):
    global btn1
    xf=Frame(window, relief=GROOVE, borderwidth=5)
    # Label defines on container frame xf
    Label(xf, text="This is a LED control interface").pack(padx=100, pady=10)
    # expand: expands the space which distrubed by container of element 
    # fill: fill the element to its space which distrubed by container
    btn1=Button(xf, text="ON")
    btn1.pack(side=LEFT, expand=YES, fill=X)
    Button(xf, text="OFF").pack(side=RIGHT, expand=YES, fill=X)
    
    # packing the frame must after the packing of elements in frame
    xf.pack(padx=10, pady=50)

if __name__ == "__main__":
    # create a window instance
    root = Tk()
    root.title("Window: Button")
##    # Label defines on container root window
##    Label(root, text="My first button window").pack(pady=10)
    setFrame(root)
    print(type(btn1))
    # entry of window
    root.mainloop()

