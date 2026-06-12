from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)

cb=Checkbutton(root,text="Male")
cb.pack()
root.mainloop()  