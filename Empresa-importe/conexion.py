
# -*- coding: utf-8 -*-

"""
módulo encargado de abrir y cerrar el cursor y la bbdd.
"""

import os, sqlite3


class Conexion:
    def abrirbbdd(self):
        """
        Abre la conexión con la base de datos y crea un cursor que realizará las operaciones con la bbdd.
        :return: void
        Excepciones: Error de operación en SQLite, muestra el error
        """
        try:
            global bbdd, conex, cur
            bbdd = 'empresa.sqlite'         #variable que almacena la base de datos
            conex = sqlite3.connect(bbdd)   #la abrimos
            cur = conex.cursor()            #la variable cursor que hará las operaciones
            print("Conexión realizada correctamente")
        except sqlite3.OperationalError as e:
            print("Error al abrir: ", e)

    def cerrarbbdd(self):
        """
        Cierra la conexión con la base de datos y el cursor.
        :return: void
        Excepciones: Error de operación en SQLite, muestra el error
        """
        try:
            cur.close()
            conex.close()
            print("Base de datos cerrada correctamente ")
        except sqlite3.OperationalError as e:
            print("Error al cerrar: ", e)




