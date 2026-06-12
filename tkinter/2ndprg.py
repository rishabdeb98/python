from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)

rb1=Radiobutton(root,text="Python",value=1)
rb1.pack()

rb2=Radiobutton(root,text="Java",value=2)
rb2.pack()

root.mainloop()  