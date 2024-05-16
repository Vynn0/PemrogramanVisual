import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()
data = [
    ["Vino", 20, 10000000000],
    ["Widi", 20, 9999999999],
    ["Darrel", 20, 213912391],
    ["Zega", 21, 913182313],
    ["Bintang", 20, 129292131],
]

index = 0
def read_data():
    for index, line in enumerate(data):
        tree.insert('', tk.END, iid = index,
                    text = line[0], values = line[1:])
columns = ("age", "salary")

tree = ttk.Treeview(root, columns = columns, height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text = 'Name')
tree.heading('age', text = 'Age')
tree.heading('salary', text = 'Salary')

read_data()
root.mainloop()