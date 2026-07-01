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

def reset():
    global count
    count=0
    l1.config(text=f"Current Count {count}")
    
l1=Label(root,text="Current count=0")
l1.pack(pady=20)

b1=Button(root,text="Click Me to Add by 1",command=add_one)
b1.pack(pady=20)

s1=Button(root,text="Click Me to Substract by 1",command=sub_one)
s1.pack(pady=20)

r1=Button(root,text="Reset",command=reset)
r1.pack(pady=20)

root.mainloop()