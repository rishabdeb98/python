from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)

lb=Listbox(root,width=20)
lb.pack()
l1=["python","java","c++","ruby","javascript"]
for i in l1:
    lb.insert(END,i)
root.mainloop()  