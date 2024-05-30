import tkinter as tk
from tkinter import ttk, colorchooser

class MathGraphicsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Visual Matematika")
        
        # Create a canvas for drawing
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(padx=10, pady=10)
        
        # Create a frame for options
        self.options_frame = ttk.Frame(root)
        self.options_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.shape_var = tk.StringVar(value="Line")
        self.color_var = tk.StringVar(value="black")
        
        # Add widgets to the options frame
        self.create_options_widgets()
        
    def create_options_widgets(self):
        # Shape selection
        ttk.Label(self.options_frame, text="Shape:").grid(row=0, column=0, padx=5, pady=5)
        shape_menu = ttk.Combobox(self.options_frame, textvariable=self.shape_var, values=["Line", "Rectangle", "Circle"])
        shape_menu.grid(row=0, column=1, padx=5, pady=5)
        shape_menu.bind("<<ComboboxSelected>>", self.update_options)
        
        # Color selection
        ttk.Label(self.options_frame, text="Color:").grid(row=0, column=2, padx=5, pady=5)
        color_menu = ttk.Combobox(self.options_frame, textvariable=self.color_var, values=["red", "green", "blue", "yellow", "magenta", "white"])
        color_menu.grid(row=0, column=3, padx=5, pady=5)
        
        # Shape-specific options
        self.option_frame = ttk.Frame(self.options_frame)
        self.option_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.update_options()
        
        # Draw button
        draw_button = ttk.Button(self.options_frame, text="Draw", command=self.draw_shape)
        draw_button.grid(row=2, column=0, columnspan=4, pady=10)
        
    def update_options(self, event=None):
        # Clear previous options
        for widget in self.option_frame.winfo_children():
            widget.destroy()
        
        shape = self.shape_var.get()
        
        if shape == "Line":
            self.create_line_options()
        elif shape == "Rectangle":
            self.create_rectangle_options()
        elif shape == "Circle":
            self.create_circle_options()
            
    def create_line_options(self):
        ttk.Label(self.option_frame, text="X1:").grid(row=0, column=0, padx=5, pady=5)
        self.x1_entry = ttk.Entry(self.option_frame)
        self.x1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Y1:").grid(row=0, column=2, padx=5, pady=5)
        self.y1_entry = ttk.Entry(self.option_frame)
        self.y1_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="X2:").grid(row=1, column=0, padx=5, pady=5)
        self.x2_entry = ttk.Entry(self.option_frame)
        self.x2_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Y2:").grid(row=1, column=2, padx=5, pady=5)
        self.y2_entry = ttk.Entry(self.option_frame)
        self.y2_entry.grid(row=1, column=3, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Width:").grid(row=2, column=0, padx=5, pady=5)
        self.width_entry = ttk.Entry(self.option_frame)
        self.width_entry.grid(row=2, column=1, padx=5, pady=5)
        
    def create_rectangle_options(self):
        ttk.Label(self.option_frame, text="X1:").grid(row=0, column=0, padx=5, pady=5)
        self.x1_entry = ttk.Entry(self.option_frame)
        self.x1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Y1:").grid(row=0, column=2, padx=5, pady=5)
        self.y1_entry = ttk.Entry(self.option_frame)
        self.y1_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="X2:").grid(row=1, column=0, padx=5, pady=5)
        self.x2_entry = ttk.Entry(self.option_frame)
        self.x2_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Y2:").grid(row=1, column=2, padx=5, pady=5)
        self.y2_entry = ttk.Entry(self.option_frame)
        self.y2_entry.grid(row=1, column=3, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Outline Width:").grid(row=2, column=0, padx=5, pady=5)
        self.outline_width_entry = ttk.Entry(self.option_frame)
        self.outline_width_entry.grid(row=2, column=1, padx=5, pady=5)
        
    def create_circle_options(self):
        ttk.Label(self.option_frame, text="Center X:").grid(row=0, column=0, padx=5, pady=5)
        self.center_x_entry = ttk.Entry(self.option_frame)
        self.center_x_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Center Y:").grid(row=0, column=2, padx=5, pady=5)
        self.center_y_entry = ttk.Entry(self.option_frame)
        self.center_y_entry.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(self.option_frame, text="Radius:").grid(row=1, column=0, padx=5, pady=5)
        self.radius_entry = ttk.Entry(self.option_frame)
        self.radius_entry.grid(row=1, column=1, padx=5, pady=5)
        
    def draw_shape(self):
        shape = self.shape_var.get()
        color = self.color_var.get()
        
        if shape == "Line":
            x1 = int(self.x1_entry.get())
            y1 = int(self.y1_entry.get())
            x2 = int(self.x2_entry.get())
            y2 = int(self.y2_entry.get())
            width = int(self.width_entry.get())
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
        elif shape == "Rectangle":
            x1 = int(self.x1_entry.get())
            y1 = int(self.y1_entry.get())
            x2 = int(self.x2_entry.get())
            y2 = int(self.y2_entry.get())
            outline_width = int(self.outline_width_entry.get())
            self.canvas.create_rectangle(x1, y1, x2, y2, outline=color, width=outline_width)
        elif shape == "Circle":
            center_x = int(self.center_x_entry.get())
            center_y = int(self.center_y_entry.get())
            radius = int(self.radius_entry.get())
            self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathGraphicsApp(root)
    root.mainloop()
