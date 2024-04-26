from tkinter import *
from tkinter import messagebox

root = Tk()
frame = Frame(root)
frame.pack()

root.geometry("1080x720")
def helloCallBack():
    msg = messagebox.showinfo( "Hello Python", "Hello to you too mate")
B = Button(root, text = "Hello Bro", command = helloCallBack)
B.place(x = 540, y = 50)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(root, text = "Music", variable = CheckVar1, bg = "blue", onvalue = 1, offvalue = 0, height = 5, width = 20, )
C2 = Checkbutton(root, text = "Video", variable = CheckVar2, bg = "red", onvalue = 1, offvalue = 0,height= 5, width = 20 )

C1.place(x = 50, y = 500)
C2.place(x = 50, y = 600)

L1 = Label(root, text = "User Name")
L1.place(x = 300, y = 300)
E1 = Entry(root, bd = 5)
E1.place(x = 500, y = 300)

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

X = Button(frame, text = "This is X Frame!", fg = "red")
X.place(x = 100, y = 400)

Lb1 = Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Java")
Lb1.place(x = 700, y = 0)

root.mainloop()