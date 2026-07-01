from tkinter import *
from tkinter import messagebox
victus=Tk()
victus.geometry("500x500")
victus.title("Radio Button program")

v=IntVar()
rb=Radiobutton(victus,text="Python",value=1,variable=v)
rb.pack(pady=20)

rb2=Radiobutton(victus,text="Java",value=2,variable=v)
rb2.pack(pady=20)

def edtech():
    value = v.get()
    if value == 0:
        messagebox.showwarning("Caution", "Please select an option")
    else:
        selected_option = "Python" if value == 1 else "Java"
        messagebox.showinfo("Successful", f"You selected: {selected_option}")
        print(selected_option)

b1=Button(victus,text="submit",command=edtech)
b1.pack(pady=20)

victus.mainloop()