from tkinter import *

root=Tk()
root.geometry("400x400")
count=0

def add_one():
    global count
    count=count+1
    l1.config(text=f"Current count {count}")

def sub_one():
    global count
    count=count-1
    l1.config(text=f"Current count {count}")

l1=Label(root,text="Current count=0")
l1.pack(pady=20)

b1=Button(root,text="Click Me to Add by 1",command=add_one)
b1.pack(pady=20)

s1=Button(root,text="Click Me to Substract by 1",command=sub_one)
s1.pack()

root.mainloop()