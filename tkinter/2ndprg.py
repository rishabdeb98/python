from tkinter import *
from tkinter import messagebox
lens=Tk()
lens.geometry("400x400")

v=StringVar()

def edtech():
    if v.get()=="":
        messagebox.showwarning("Caution","Its empty")
    else:
        messagebox.showinfo("successfull",v.get())

e1=Entry(lens,text="Enter text",width=30,textvariable=v)
e1.pack(pady=10)

b1=Button(lens,text="Submit",command=edtech)
b1.pack(pady=10)

lens.mainloop()