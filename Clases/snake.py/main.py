import  tkinter as tk

#ventana principal
ventana = tk.Tk()
#configuracion de ventana
ventana.title("Mi ventana")
ventana.geometry("400x300")

#creacion de etiqueta
etiqueta = tk.Label(ventana, text="Hola, Mundo!")
etiqueta.pack()

#crear boton 
boton = tk.Button(ventana, text="Click aqui")
boton.pack()

#entrada de texto
entrada=tk.Entry(ventana)
entrada.pack()

#creacion de cuadro de texto multiple
cuadro_texto= tk.Text(ventana, height=5, width=30)
cuadro_texto.pack()

#casilla
casilla=tk.Checkbutton(ventana, text="Aceptar terminos y conidiciones")
casilla.pack()

#creacion de una barra de progreso
barra_progreso=tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL)
barra_progreso.pack()

#----------------
ventana.mainloop()
