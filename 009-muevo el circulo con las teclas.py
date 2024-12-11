import tkinter as tk

def muevoArriba(self):
    print("voy a mover hacia arriba")
    lienzo.move(circulo,0,-10)
def muevoIzquierda(self):
    print("voy a mover hacia la izquierda")
    lienzo.move(circulo,-10,0)
def muevoAbajo(self):
    print("voy a mover hacia abajo")
    lienzo.move(circulo,0,10)
def muevoDerecha(self):
    print("voy a mover hacia la derecha")
    lienzo.move(circulo,10,0)

ventana = tk.Tk()

lienzo = tk.Canvas(ventana)
lienzo.pack()
circulo = lienzo.create_oval(
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
ventana.bind("<a>",muevoIzquierda)
ventana.bind("<s>",muevoAbajo)
ventana.bind("<d>",muevoDerecha)
ventana.mainloop()