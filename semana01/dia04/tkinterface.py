from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import tkinter as tk
import sqlite3


class Alumno:
    def onInsert(self):
        sql_clause = "insert into " + self.tb_name + "(nombre,email,celular) values (?,?,?)"
        sql_params = (self.name.get(),self.email.get(),self.cellphone.get())
        sql_result = self.sqlExecute(sql_clause,sql_params)
        messagebox.showinfo("Registro","Datos registrados correctamente")
        self.listRecords()
    
    def listRecords(self):
        #Limpiando la lista de registros
        c_alumnos = self.recordsview.get_children()
        for r_alumno in c_alumnos:
            self.recordsview.delete(r_alumno)

        #Mostrando los registros consultándolos de la BD
        sql_clause = "select nombre, email, celular from " + self.tb_name + " order by nombre"
        sql_params = ()
        sql_result = self.sqlExecute(sql_clause,sql_params)
        
        for record in sql_result:
            self.recordsview.insert('',tk.END,values=record)
        
    def sqlExecute(self,clause,params):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            result = cursor.execute(clause,params)
            connection.commit()
        return result
            
    def __init__(self,window,title):
        self.db_name = "academico.s3db"
        self.tb_name = "alumnos"
        
        self.window = window #Propiedad 'window' inicializada con el objeto 'Window' donde se dibujará esta clase 
        self.window.title(title)

        #Definiendo la propiedad 'frame'
        self.frame = LabelFrame(self.window,text="Nuevo alumno")
        self.frame.grid(row=0,column=0,columnspan=4,pady=10)

        #Definiendo la propiedad 'name'
        self.lbl_name = Label(self.frame,text="Nombre: ")
        self.lbl_name.grid(row=1,column=0)
        self.name = Entry(self.frame)
        self.name.grid(row=1,column=1)
        
        #Definiendo la propiedad 'email'
        self.lbl_email = Label(self.frame,text="Email: ")
        self.lbl_email.grid(row=2,column=0)
        self.email = Entry(self.frame)
        self.email.grid(row=2,column=1)

        #Definiendo la propiedad 'cellphone'
        self.lbl_cellphone = Label(self.frame,text="Celular: ")
        self.lbl_cellphone.grid(row=3,column=0)
        self.cellphone = Entry(self.frame)
        self.cellphone.grid(row=3,column=1)

        self.btn_registrar = Button(self.frame,text="Registrar",command=self.onInsert)
        self.btn_registrar.grid(row=4,columnspan=2,sticky=W + E)
        
        #Definiendo el objeto 'recordsview'
        self.recordsview = Treeview(columns=('nombre','email','celular'), show='headings')
        self.recordsview.grid(row=6,column=0,columnspan=1)
        self.recordsview.heading('#1',text="Nombre",anchor=CENTER)
        self.recordsview.heading('#2',text="Email",anchor=CENTER)
        self.recordsview.heading('#3',text="Celular",anchor=CENTER)
        self.listRecords()

window = Tk()
window.geometry('600x400')
canvas = Alumno(window,"Alumnos")
window.mainloop() 
