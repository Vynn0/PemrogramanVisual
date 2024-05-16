import tkinter as tk

root = tk.Tk()

Frameku = tk.Frame(root, bg = 'cyan')
Frameku.place(relwidth = 0.8, relheight = 0.8)

Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'black', fg = 'white')
Tombolku.pack()

Entryku = tk.Entry(Frameku, bg = 'white')
Entryku.pack()

root.mainloop()