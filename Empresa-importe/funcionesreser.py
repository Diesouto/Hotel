
# -*- coding: utf-8 -*-

"""
Módulo que gestiona las operaciones de reserva.
"""

import conexion
import sqlite3
import variables
from datetime import datetime


def limpiarentry(fila):
    """
    Limpia los widgets de entrada de reserva.

    :param fila: contiene los widgets de reserva
    :return: void
    """
    for i in range(len(fila)):
        fila[i].set_text('')
    for i in range(len(variables.menslabel)):
        variables.menslabel[i].set_text('')
    variables.cmbhab.set_active(-1)

def calculardias():
    """
    Calcula los días de estancia de un cliente.

    :return: void
    """
    diain = variables.filareserva[2].get_text()
    date_in = datetime.strptime(diain, '%d/%m/%Y').date()
    diaout = variables.filareserva[3].get_text()
    date_out = datetime.strptime(diaout, '%d/%m/%Y').date()
    noches = (date_out-date_in).days
    if noches <= 0:
        variables.menslabel[2].set_text('Check-Out debe ser posterior')
        variables.reserva = 0
    else:
        variables.reserva = 1
        variables.menslabel[2].set_text(str(noches))

def insertares(fila):
    """
    Inserta una reserva en la bbdd.

    :param fila: contiene los widgets de entrada de reserva con su información
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('insert into  reservas(dni, numhab, checkin, checkout, noches) values(?,?,?,?,?)', fila)
        conexion.conex.commit()

    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listadores():
    """
    Obtiene un listado de las reservas y lo muestra en el treeview.

    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        variables.listado = listares()
        variables.listreservas.clear()
        for registro in variables.listado:
            variables.listreservas.append(registro)
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def listares():
    """
    Realiza una consulta de todas las reservas de la bbdd y las almacena en la variable listado.

    :return: listado
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select codreser, dni, numhab, checkin, checkout, noches from reservas')
        listado = conexion.cur.fetchall()
        conexion.conex.commit()
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarapelcli(dni):
    """
    Busca el apellido de un cliente en concreto.

    :param dni: Contiene el dni del cliente del que queremos saber el apellido
    :return: apel: contiene el apellido de cliente
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select apel from clientes where dni = ?', (dni,))
        apel = conexion.cur.fetchone()
        conexion.conex.commit()
        return apel
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def buscarnome(dni):
    """
    Busca el nombre de un cliente en concreto.

    :param dni: Contiene el dni del cliente del que queremos saber el nombre
    :return: nome: contiene el nombre de cliente
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select nome from clientes where dni = ?', (dni,))
        nome = conexion.cur.fetchone()
        conexion.conex.commit()
        return nome
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def bajareserva(cod):
    """
    Elimina una reserva de la bbdd.

    :param cod: contiene el código de la reserva a eliminar
    :return: void
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        print(cod)
        conexion.cur.execute('delete from reservas where codreser = ?', (cod,))
        conexion.conex.commit()
        if variables.switch.get_active():
            libre = 'SI'
        else:
            libre = 'NO'
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()

def versilibre(numhab):
    """
    Comprueba si una habitación concreta está libre u ocupada.

    :param numhab: contiene el número de la habitación que deseamos consultar
    :return: True: si está libre
             False: si está ocupada
    Excepciones: Error de operación en SQLite, muestra el error y hace rollback
    """
    try:
        conexion.cur.execute('select libre from habitacion where numero = ?', (numhab,))
        lista= conexion.cur.fetchone()
        conexion.conex.commit()
        if lista[0] == 'SI':
            return True
        else:
            return False
    except sqlite3.OperationalError as e:
        print(e)
        conexion.conex.rollback()


def obtener_precio(numero):
    """
    Obtiene el precio de una habitación concreta.

    :param numero: contiene el número de la habitación a consultar
    :return: precio: contiene el precio de la habitación consultada
    """
    conexion.cur.execute('select prezo from habitacion where numero = ?', (numero,))
    precio = conexion.cur.fetchone()
    return precio