import tkinter as tk

ventana = tk.Tk()

lienzo = tk.Canvas(ventana)
lienzo.pack()
lienzo.create_oval(
    10, 
    10, 
    50, 
    50, 
    fill="blue", 
    outline="black")

ventana.mainloop()