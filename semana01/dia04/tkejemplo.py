from tkinter import Tk, LabelFrame, Label, Entry, Button
from tkinter import messagebox

'''
Con esta librería tkinter podemos definir interfaces gráficas.
Se han usado las siguientes clases en el ejemplo:
Tk -> Ventana: Ventana donde se crean los demás objetos
LabelFrame -> Marco: Agrupador de otros objetos
Label -> Etiqueta: Textos o frases descriptivos
Entry -> Entrada: Cuadros de texto para capturar valores
Button -> Botón: Botones para responder a eventos externos
'''

def probar():
    messagebox.showinfo("Saludo","Hola " + txtNombre.get())

app = Tk()
app.title('Académico: Mi primera interfaz') 
app.geometry('380x200') #Tamaño de la ventana: Ancho x Alto

frmPrincipal = LabelFrame(app, text="Alumno")
frmPrincipal.grid(row=0, column=0, columnspan=4, pady=10)

lblNombre = Label(frmPrincipal, text="Nombre: ")
lblNombre.grid(pady=5, row=1, column=0)
txtNombre = Entry(frmPrincipal, width=40)
txtNombre.grid(padx=5, row=1, column=1)

lblEmail = Label(frmPrincipal, text="Email: ")
lblEmail.grid(pady=5, row=2, column=0)
txtEmail = Entry(frmPrincipal, width=40)
txtEmail.grid(padx=5, row=2, column=1)

lblCelular = Label(frmPrincipal, text="Celular: ")
lblCelular.grid(pady=5, row=3, column=0)
txtCelular = Entry(frmPrincipal, width = 40)
txtCelular.grid(padx=5, row=3, column=1)

btnRegistrar = Button(frmPrincipal, text="Probar", command=probar, width=50)
btnRegistrar.grid(padx=10, pady=10, row=4, column=0, columnspan=2)

app.mainloop() #Muestra la ventana