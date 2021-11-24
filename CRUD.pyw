"""
APLICACION GRAFICA CRUD

"""
from sqlite3.dbapi2 import Cursor, connect
from tkinter import *
from tkinter import messagebox
import sqlite3
from typing import TextIO

root=Tk()
root.title("Sistema CRUD")
root.geometry("350x500")
root.resizable(0,0)

#--------------------Logica----------------#

def ayudaAcercaDe ():
    messagebox.showinfo("Sistema CRUD", """
    Creador: Nahuel Ramirez
    Fecha: 11/11/2021
    Email: nahuel-ramirez@hotmail.com
    """)

def ayudaLicencia():
    messagebox.showinfo("Licencia", """
    Sistema CRUD programado en Python v3.9.6
    Version: 0.1.1
    Editor de texto: Visual Studio Code
    Base de Datos: SQLite3
    Librerias: Tkinter, Messagebox y SQLite3
    """)

def manualAyuda():
    messagebox.showinfo("Manual de ayuda", """
A continuacion se le explicara como utlizar cada opcion de este sistema.

Primero debera conectarse a la base de datos, o bien crearla. 
Para eso, presione en la solapa 'BBDD' la opcion 'Conectar' y luego, podra realizar las Altas, Bajas y Modificaciones de registros.

Se actualiza, lee y borran datos a traves del campo 'Legajo'.

Por ejemplo:

Si desea borrar un registro, solo debera ingresar el Legajo de la persona y seleccionar 'Borrar'. Lo mismo con el boton de leer. Para actualizar debera ingresar el legajo, asi como tambien los demas campos en blanco.

Notara ademas que en el menu superior existe la solapa 'Borrar', esto es para borrar todos los campos
y no para borrar registros.


    """)


def salir():
    salida=messagebox.askquestion("Salir", "¿Desea salir de la aplicacion?")
    if salida == "yes":
        root.destroy()

def bbddConectar():
    con=sqlite3.connect("Usuarios")
    cursor=con.cursor()

    try:
        cursor.execute('''
            CREATE TABLE DATOS_USUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LEGAJO VARCHAR(50) UNIQUE NOT NULL,
            NOMBRE VARCHAR(50) NOT NULL,
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(100),
            CARGO VARCHAR (50) NOT NULL,
            SALARIO VARCHAR (25) NOT NULL
            )
        ''')

        messagebox.showinfo("Base de Datos", "¡Base de datos creada con exito!")
    except:
        messagebox.showwarning("¡Atencion!", "La Base de datos ya existe.")

    con.commit()
    con.close()

def insertarDatos():
    con=sqlite3.connect("Usuarios")
    cursor=con.cursor()

    cursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,'" + miLegajo.get() + 
    "','" + miNombre.get() + 
    "','" + miApellido.get() + 
    "','" + miDireccion.get() + 
    "','" + miCargo.get() + 
    "','" + miSalario.get() + "')")

    
    con.commit()
    
    messagebox.showinfo("Base de datos", "Registro insertado con exito.")

    con.close()

def borrarDatos():
    con=sqlite3.connect("Usuarios")
    cursor=con.cursor()

    cursor.execute("DELETE FROM DATOS_USUARIOS WHERE LEGAJO="+miLegajo.get())

    messagebox.showinfo("ELIMINADO", "Registro eliminado con exito.")

    con.commit()
    con.close()

def actualizarDatos():
    con=sqlite3.connect("Usuarios")
    cursor=con.cursor()

    cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE='" + miNombre.get() + 
    "', APELLIDO='" + miApellido.get() +
    "', DIRECCION='" + miDireccion.get() +
    "', CARGO='" + miCargo.get() +
    "', SALARIO='" + miSalario.get() +
    "' WHERE LEGAJO=" + miLegajo.get())

    messagebox.showinfo("ACTUALIZADO", "Registro actualizado con exito.")

    con.commit()
    con.close()


def leerDatos():
    con=sqlite3.connect("Usuarios")
    cursor=con.cursor()

    cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE LEGAJO="+miLegajo.get())
    usuario=cursor.fetchone()
    miID.set(usuario[0])
    miNombre.set(usuario[2])
    miApellido.set(usuario[3])
    miDireccion.set(usuario[4])
    miCargo.set(usuario[5])
    miSalario.set(usuario[6])    
    
    con.commit()
    con.close()



def borrarCampos():
    miID.set("")
    miLegajo.set("")
    miNombre.set("")
    miApellido.set("")
    miDireccion.set("")
    miCargo.set("")
    miSalario.set("")


    



#----------- MENU -----------#
barraMenu = Menu(root)
root.config(menu=barraMenu)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=bbddConectar)
bbddMenu.add_command(label="Salir", command=salir)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar todos los campos", command=borrarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=insertarDatos)
crudMenu.add_command(label="Leer", command=leerDatos)
crudMenu.add_command(label="Actualizar", command=actualizarDatos)
crudMenu.add_command(label="Borrar", command=borrarDatos)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Manual de ayuda", command=manualAyuda)
ayudaMenu.add_command(label="Licencia", command=ayudaLicencia)
ayudaMenu.add_command(label="Acerca de...", command=ayudaAcercaDe)


barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


#------------------ CAMPOS ---------------------------#
campoFrame = Frame(root)
campoFrame.pack()

miID=StringVar()
miLegajo=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miDireccion=StringVar()
miCargo=StringVar()
miSalario=StringVar()

#-------- Entrys ---------- #
entryID=Entry(campoFrame, textvariable=miID, state="disabled", border=3)
entryID.grid(row=0, column=1, padx=10, pady=10)

entryLegajo=Entry(campoFrame, textvariable=miLegajo, border=3)
entryLegajo.grid(row=1, column=1, padx=10, pady=10)

entryNombre=Entry(campoFrame, textvariable=miNombre, border=3)
entryNombre.grid(row=2, column=1, padx=10, pady=10)

entryApellido=Entry(campoFrame, textvariable=miApellido, border=3)
entryApellido.grid(row=3, column=1, padx=10, pady=10)

entryDireccion=Entry(campoFrame, textvariable=miDireccion, border=3)
entryDireccion.grid(row=4, column=1, padx=10, pady=10)

entryCargo=Entry(campoFrame, textvariable=miCargo, border=3)
entryCargo.grid(row=5, column=1, padx=10, pady=10)

entrySalario=Entry(campoFrame, textvariable=miSalario, border=3)
entrySalario.grid(row=6, column=1, padx=10, pady=10)



#--------- Labels ---------#
labelID =Label(campoFrame, text="ID:")
labelID.grid(row=0, column=0, padx=10, pady=10)

labelLegajo =Label(campoFrame, text="Legajo:")
labelLegajo.grid(row=1, column=0, padx=10, pady=10)

labelNombre =Label(campoFrame, text="Nombre:")
labelNombre.grid(row=2, column=0, padx=10, pady=10)

labelApellido =Label(campoFrame, text="Apellido:")
labelApellido.grid(row=3, column=0, padx=10, pady=10)

labelDireccion =Label(campoFrame, text="Direccion:")
labelDireccion.grid(row=4, column=0, padx=10, pady=10)

labelCargo =Label(campoFrame, text="Cargo:")
labelCargo.grid(row=5, column=0, padx=10, pady=10)

labelSalario =Label(campoFrame, text="Salario:")
labelSalario.grid(row=6, column=0, padx=10, pady=10)

#----------------------- BOTONES -----------------------#
botonFrame=Frame(root)
botonFrame.pack()

botonGenerar = Button(botonFrame, text="Generar", bd=3, command=insertarDatos)
botonGenerar.grid(row=8, column=0, pady=20, padx=10)

botonLeer = Button(botonFrame, text="Leer", bd=3, command=leerDatos)
botonLeer.grid(row=8, column=1, pady=20, padx=10)

botonActualizar = Button(botonFrame, text="Actualizar", bd=3, command=actualizarDatos)
botonActualizar.grid(row=8, column=2, pady=20, padx=10)

botonBorrar = Button(botonFrame, text="Borrar", bd=3, command=borrarDatos)
botonBorrar.grid(row=8, column=3, pady=20, padx=10)


#--------------------------- Saludo Bienvenida --------------- #
saludoFrame = Frame(root)
saludoFrame.pack()

saludo=Text(saludoFrame, fg="blue", cursor="heart")
saludo.insert(1.0, """
¡Bienvenidos/as a mi primer sistema CRUD!

Antes de empezar, le recomiendo leer el \n'Manual de ayuda' cliqueando en la solapa\n'Ayuda' -> 'Manual de ayuda'
""")
saludo.config(state="disabled")
saludo.pack()


root.mainloop()
