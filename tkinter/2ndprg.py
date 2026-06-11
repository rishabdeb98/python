from tkinter import *

root=Tk()
root.title("Entry Widget")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)

l1=Label(root,text="Employee Name",fg="red",bg="yellow",font="Arial 20 bold")
l1.place(x=0,y=10)
v=StringVar()
def edtech():
    x=v.get()
    print(x)
    l2.config(text=x)

e1=Entry(root,bd=5,font="Arial 20 bold",textvariable=v)
e1.place(x=0,y=50)

b1=Button(root,text="submit",fg="white",bg="blue",font="Arial 20 bold",command=edtech)
b1.place(x=0,y=100)

l2=Label(root,text="Nothing",fg="red",bg="yellow",font="Arial 20 bold")
l2.place(x=5,y=160)

root.mainloop()  