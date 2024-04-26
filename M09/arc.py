import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 250, fill = "black")

C.pack()
top.mainloop()
