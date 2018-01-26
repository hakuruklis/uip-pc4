import sqlite3
import os

db = sqlite3.connect('data/Libros.db') # Base de datos en un archivo
cursor = db.cursor()
# Creacion de la base de datos
# cursor.execute('''CREATE TABLE LIBROS(id INTEGER PRIMARY KEY, Cant_paginas NUMERIC, ISBN NUMERIC, AUTOR TEXT, PUBLICACION NUMERIC)''')
# Cant_paginas = input("Cantidad de paginas: ")
# publicacion = input("Publicacion: ")
# ISBN = input("ISBN: ")
# Autor = input("Autor: ")
# db.commit()

n=0
while (n != 999):
    print("1 Agreagar Valor")
    print("2 Buscar ISBN")
    print("3 Elinimar registro")
    n = int(input("Inserte su opcion: "))
    if n== 1:
        Cant_paginas = int(input("Cantidad de paginas: "))
        publicacion = int(input("Publicacion: "))
        ISBN = int(input("ISBN: "))
        Autor = input("Autor: ")
        id=int(input("ID: "))
        cursor.execute('''INSERT INTO LIBROS VALUES (?, ?, ?, ?, ?)''', (id,Cant_paginas , ISBN, Autor, publicacion,))
        x = int(input("Desea regresar al menu pricinpal? si=1 no=0"))
        db.commit()
        if x == 0:
            n = 999
        os.system('cls')
    elif n==2:
        ISBN2 = input("Inserte ISBN")
        cursor.execute('''SELECT ISBN FROM LIBROS WHERE ISBN = ?''', (ISBN2,))
        temp = cursor.fetchall()
        temp2 =0
        for fila in temp:
            temp2 = fila[0]
        if int(ISBN2) == int(temp2):
            print("Encontrado")
        else:
            print("No Encontrado")
        x = int(input("Desea regresar al menu pricinpal? si=1 no=0"))
        if x == 0:
            n = 999
    elif n==3:
        cursor.execute('''SELECT id FROM LIBROS''')
        resultado = cursor.fetchall()
        id = input("ID de usuario a eliminar: ")
        for fila in resultado:
            if int(id) == int(fila[0]):
                cursor.execute('''DELETE FROM LIBROS WHERE id = ?''',(id,))
                db.commit()
            else:
                print("id no encontado")
        x = int(input("Desea regresar al menu pricinpal? si=1 no=0"))
        if x == 0:
            n == 999
    else:
        print("Valor incorrecto")

db.close()