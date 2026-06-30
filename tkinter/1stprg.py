from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("First program")
root.minsize(width=200,height=400)
root.maxsize(width=400,height=600)
img=Image.open(r"C:\Users\Rishabh Deb\Documents\30-08-25_python\tkinter\ritvik.jpg")
a1=ImageTk.PhotoImage(img)
v1=Label(root, image=a1)
v1.pack()
root.mainloop()