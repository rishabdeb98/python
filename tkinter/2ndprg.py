from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)
v=IntVar()
def edtech():
    print(v.get())

rb1=Radiobutton(root,text="Python",value=1,variable=v)
rb1.pack()

rb2=Radiobutton(root,text="Java",value=2,variable=v)
rb2.pack()

e1=Button(root,text="Submit",command=edtech)
e1.pack()
root.mainloop()  