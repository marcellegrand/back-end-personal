from tkinter import *
from tkinter import messagebox

def registrar():
    messagebox.showinfo("Saludo","Hola " + txtNombre.get())

app = Tk()
app.title('Académico') 
app.geometry('500x500') #Tamaño de la ventana

frmPrincipal = LabelFrame(app,text="Alumnos")
frmPrincipal.grid(row=0,column=0,columnspan=3,pady=10)

lblNombre = Label(frmPrincipal,text="Nombre: ")
lblNombre.grid(row=1,column=0)
txtNombre = Entry(frmPrincipal)
txtNombre.grid(row=1,column=1)

lblEmail = Label(frmPrincipal,text="Email: ")
lblEmail.grid(row=2,column=0)
txtEmail = Entry(frmPrincipal)
txtEmail.grid(row=2,column=1)

lblCelular = Label(frmPrincipal,text="Celular: ")
lblCelular.grid(row=3,column=0)
txtCelular = Entry(frmPrincipal)
txtCelular.grid(row=3,column=1)

btnRegistrar = Button(frmPrincipal,text="Registrar",command=registrar)
btnRegistrar.grid(row=4,column=2)

app.mainloop() #Muestra la ventana