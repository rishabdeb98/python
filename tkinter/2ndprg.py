from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("My second program")
img = Image.open(r"C:\Users\Rishabh Deb\Documents\30-08-25_python\tkinter\ritvik.jpg")
x1 = ImageTk.PhotoImage(img)
r2 = Label(root, image=x1)
r2.pack()
root.mainloop()