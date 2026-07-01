from tkinter import *
victus=Tk()

victus.geometry("400x400")
f1=Frame()
f1.pack()

f2=Frame()
f2.pack(side=BOTTOM)

l1=Label(f1,text="Great Learning")
l1.pack()

l2=Label(f2,text="Bottom")
l2.pack()
victus.mainloop()