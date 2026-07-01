from tkinter import *
victus=Tk()
victus.geometry("500x500")
victus.title("Radio Button program")

v=IntVar()
rb=Radiobutton(victus,text="Python",value=1,variable=v)
rb.pack(pady=20)

rb2=Radiobutton(victus,text="Java",value=2,variable=v)
rb2.pack(pady=20)

def edtech():
    value=v.get()
    print(value)

b1=Button(victus,text="submit",command=edtech)
b1.pack(pady=20)

victus.mainloop()