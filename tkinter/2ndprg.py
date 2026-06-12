from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)

f1=Frame()
f1.pack()
f2=Frame()
f2.pack(side=BOTTOM)
l1=Label(f1,text="Username")
l1.pack()
l2=Label(f2,text="Bottom")
l2.pack()
root.mainloop()  