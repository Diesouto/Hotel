
# -*- coding: utf-8 -*-

"""
Módulo que gestiona las operaciones de los clientes.
"""

import conexion
import sqlite3
import variables

def limpiarentry(fila):
    '''
    Se encarga de limpiar los widgets de cliente.
    :param fila: una tupla con los widgets del cliente
    :return: void
    '''

    variables.menslabel[1].set_text('')
    for i in range(len(fila)):
        fila[i].set_text('')

def validoDNI(dni):

    """
    Se encarga de validar un dni.
    :param dni: un dni que se quiere validar
    :return: True si es válido o False si es inválido
    Excepciones:    Si el dni no es válido print("Error")
    """

    try:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"   #letras del dni, es estandar
        dig_ext = "XYZ"
        #tabla letras extranjeroreemp_
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = dni.upper()
        if len(dni) == 9: #el dni debe tener 9 caracteres
            dig_control = dni[8]
            dni = dni[:8]                                          #el número que son los 8 primeros
            if dni[0] in dig_ext:
                print(dni)
                dni = dni.replace(dni[0],reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] == dig_control
        return False
    except:
        print("Error")
        return None

#inserta un registro

def insertarcli(fila):
    """
    Inserta un cliente en la base de datos.
    :param fila:
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('insert into  clientes(dni,apel,nome, data) values(?,?,?,?)',(fila[0], fila[1], fila[2], fila[3]))
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

# select para utilizar en las operaciones de datos

def listar():
    """
    Devuelve un listado con todos los clientes.
    :return: listado con todos los clientes
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select * from clientes')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

# esta funcion da de baja un clieente
def bajacli(dni):
    """
    Elimina un cliente de la base de datos.
    :param dni: dni del cliente a borrar
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('delete from clientes where dni = ?', (dni,))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def modifcli(registro, cod):
    """
    Modifica los datos de un cliente en la base de datos.
    :param registro: recoge los nuevos datos del cliente
    :param cod: codigo del cliente a modificar
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('update clientes set dni = ?, apel= ?, nome = ?, data = ? where id = ?',
                             (registro[0], registro[1], registro[2], registro[3], cod))
        conexion.conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

#esta funcion carga el treeview con los datos de la tabla clientes

def listadocli(listclientes):
    """
    Inserta los datos del cliente en un treeview.
    :param listclientes: treeview donde se insertarán los clientes
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        variables.listado = listar()
        listclientes.clear()
        for registro in variables.listado:
            listclientes.append(registro[1:5])
    except:
        print("error en cargar treeview")


def selectcli(dni):
    """
    Devuelve los datos de un cliente de la base de datos.
    :param dni: dni del cliente que queremos seleccionar
    :return: listado con los datos del cliente
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select id from clientes where dni = ?', (dni,))
        listado = conexion.cur.fetchone()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def limpiarentry(fila):
    """
    Limpia los entry de cliente.
    :param fila:
    :return: void
    """
    for i in range(len(fila)):
        fila[i].set_text('')

def apelnomfac(dni):
    """
    Obtiene el nombre y apellido del cliente y los devuelve concatenados.
    :param dni: dni del cliente a consultar
    :return: apelnome: concatenación con el nombre y el apellido del cliente
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select apel, nome from clientes where dni = ?', (dni,))
        apelnome = conexion.cur.fetchone()
        conexion.conex.commit()
        return apelnome
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

