from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)
e1=Entry(root,width=20,bd=5,font=('Arial',20))
e1.pack()
root.mainloop()