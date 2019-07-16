##Programa en python en tkinder
#Borra,actualiza y busca datos en una base de datos
#Guarda los datos en un pdf
import tkinter as tk
from tkinter import *
import pymysql
from reportlab.pdfgen import canvas
import time
    
root = tk.Tk()
root.config(bd=20)

identificador = StringVar()
nombre = StringVar()

try:
    db = pymysql.connect("localhost", "root", "", "registro")
    print("conexión  exitosa")
except:
    print("conexión erronea")
        
    
def insert():
    cursor = db.cursor()
    insert = 'INSERT INTO alumnos VALUES('+str(identificador.get())+', "'+str(nombre.get())+'");'
    cursor.execute(insert)
    db.commit()
    limpiar()
    
def delete():
    try:
        cursor = db.cursor()
        delete = 'DELETE FROM `alumnos` WHERE id = '+str(identificador.get())+' and nombre = '+str(nombre.get())
        print(delete)
        cursor.execute(delete)
        db.commit()
        limpiar()
    except:
        print("Nombre o identificador mal")
        limpiar()
    
def update():
    #Para el update en el id se pone el que quieres cambiar de nombre
    #En la casilla de nombre se coloca el nuevo nombre
    try:
        cursor = db.cursor()
        update = "UPDATE `alumnos` SET nombre = '" + nombre.get() + "' WHERE id = " + identificador.get() + ";"
        cursor.execute(update)
        db.commit()
        limpiar()
    except:
        print("identificador mal")
        limpiar()
        
def select():
    ml = 10
    t = "                          "
    j = 740

    c = canvas.Canvas('Reporte_BD.pdf')

    c.drawString(ml, 830, "Empresa: empresa X")
    c.drawString(ml, 810, "Reporte generado el: " + time.strftime("%d/%m/%y"))
    c.drawString(ml, 760, "ID" + t + "Nombre")

    
    cursor = db.cursor()
    select = "select * from alumnos"
    cursor.execute(select)
    result = cursor.fetchall()


    for row in result:
        identificador = row[0]
        nombre = row[1]
        c.drawString(ml, j, "    {0}".format(identificador,nombre) + t + "   {1}".format(identificador,nombre))
        j = j - 15

    c.save()
    
def limpiar():
    identificador.set("")
    nombre.set("")
    
def salir():
    root.destroy()

def main():
    Label(root, text="Menu principal").pack()
    Label(root, text="Reporte de empleados o alumnos").pack()
    
    Label(root, text="").pack()
    
    Label(root, text="Identificador: ").pack()
    Entry(root, justify="center", textvariable=identificador).pack()

    Label(root, text="Nombre: ").pack()
    Entry(root, justify="center", textvariable=nombre).pack()
    
    Label(root, text="").pack()
    
    Button(root, text="Insertar", command=insert).pack(side="left")
    Button(root, text="Eliminar", command=delete).pack(side="left")
    Button(root, text="Actualizar", command=update).pack(side="left")
    Button(root, text="Generar PDF", command=select).pack(side="left")
    Button(root, text="Exit", command=salir).pack(side="left")

    root.mainloop()

if __name__ == "__main__":
    main()