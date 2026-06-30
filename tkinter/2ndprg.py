from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)

v=StringVar()
def edtech():
    if v.get()=="":
        messagebox.

e1=Entry(root,bd=5,font=("calibri",20),width=20,textvariable=v)
e1.pack()

b1=Button(root,text="Submit",command=edtech)
root.mainloop()  