
# -*- coding: utf-8 -*-

"""
Módulo que gestiona las habitaciones.
"""

import conexion, sqlite3, variables

def insertarhab(fila):
    """
    Añade una habitación a la base de datos.

    :param fila: fila con los datos de una nueva habitación
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('insert into habitacion(numero,tipo,prezo,libre) values(?,?,?,?)', fila)
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listarhab():
    """
    Devuelve un listado con las habitaciones de la base de datos.

    :return: listado: contiene todas las habitaciones de la bbdd
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select * from habitacion')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def limpiarentry(fila):
    """
    Limpia los widgets de entrada de las habitaciones.

    :param fila: contiene los widgets de entrada de las habitaciones
    :return: void
    """
    for i in range(len(fila)):
        fila[i].set_text('')

def listadohab(listhab):
    """
    Inserta un listado de las habitaciones en el treeview.

    :param listhab: contiene el treeview de las habitaciones
    :return: void
    Excepciones: Error de consulta, imprime ("Error en cargar treeview de hab")
    """
    try:
        variables.listado = listarhab()
        variables.listhab.clear()
        for registro in variables.listado:
            listhab.append(registro)
    except:
        print("error en cargar treeview de hab")


def bajahab(numhab):
    """
    Elimina una habitación de la bbdd.

    :param numhab: número de la habitación que se desea eliminar
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('delete from habitacion where numero = ?', (numhab,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def modifhab(registro, numhab):
    """
    Modifica los datos de una habitación de la bbdd.

    :param registro: recibe los nuevos datos de la habitación
    :param numhab: indica la habitación a modificar
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('update habitacion set tipo = ?, prezo = ?, libre = ? where numero = ?',
                             (registro[1], registro[0], registro[2], numhab))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadonumhab():
    """
    Realiza una consulta que almacena los números de las habitaciones en una variable listcmbhab.

    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select numero from habitacion')
        listado = conexion.cur.fetchall()
        variables.listcmbhab.clear()
        for row in listado:
            variables.listcmbhab.append(row)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def listadonumhabres():
    """
    Realiza una consulta que almacena los números de las habitaciones en una variable llamada lista.

    :return: lista
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select numero from habitacion')
        lista = conexion.cur.fetchall()
        return lista
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def cambiaestadohab(libre, numhabres):
    """
    Cambia el estado de una habitación de libre a ocupada o viceversa.

    :param libre: contiene un string con "SI" o "NO" para cambiar el estado de la habitación
    :param numhabres: contiene el número de la habitación que se desea modificar
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        print(libre)
        conexion.cur.execute('update habitacion set libre = ? where numero = ?',
                             (libre[0], numhabres))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
       print(e)
       conexion.conex.rollback()