import tkinter as tk

def muevoArriba(self):
    print("voy a mover hacia arriba")

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
lienzo.create_rectangle(
    100,
    100,
    200,
    200,
    fill="red", 
    outline="black"
)
ventana.bind("<w>",muevoArriba)
ventana.mainloop()