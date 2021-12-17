from tkinter import *
from tkinter import messagebox

def saludar():
    messagebox.showinfo("Saludo","Hola " + txtNombre.get())

app = Tk()
app.title('Primera interface') 
app.geometry('500x500') #Tamaño de la ventana

frmPrincipal = LabelFrame(app,text="Frame")
frmPrincipal.grid(row=0,column=0,columnspan=3,pady=10)

lblNombre = Label(frmPrincipal,text="Nombre: ")
lblNombre.grid(row=1,column=0)

txtNombre = Entry(frmPrincipal)
txtNombre.grid(row=1,column=1)

btnSaludo = Button(frmPrincipal,text="Saludar",command=saludar)
btnSaludo.grid(row=1,column=2)

app.mainloop() #Muestra la ventana
