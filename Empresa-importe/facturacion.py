
# -*- coding: utf-8 -*-

"""
módulo encargado de las operaciones con la factura de un cliente.
"""


import funcionesreser
import variables
import datetime

def limpiar_labels_factura(labels_factura):
    """
    Limpia los labels de la factura.

    :param labels_factura: contiene los labels de la factura
    :return: void
    """
    for i in range(len(labels_factura)):
        labels_factura[i].set_text('')


def obtener_factura(dni, apellidos, nombre, cod, numero_habitacion, noches):
    """
    Genera la factura para un cliente del hotel.

    :param dni: dni del cliente
    :param apellidos: apellidos del cliente
    :param nombre: nombre del cliente
    :param cod: código de la habitación
    :param numero_habitacion: número de la habitación del cliente
    :param noches: número de noches que se queda el cliente
    :return: void
    Excepciones: Error de obtención de datos, muestra el error e imprime el mensaje("Error en obtener factura")
    """
    try:
        variables.mensfac[0].set_text(str(dni))
        variables.mensfac[1].set_text(str(apellidos))
        variables.mensfac[2].set_text(str(nombre))
        variables.mensfac[3].set_text(str(cod))
        variables.mensfac[4].set_text(str(numero_habitacion))
        variables.mensfac[5].set_text(str(datetime.date.today()))
        variables.mensfac[6].set_text("Noches")
        variables.mensfac[7].set_text(str(noches))
        precio_habitacion = funcionesreser.obtener_precio(numero_habitacion)
        variables.mensfac[8].set_text(str(precio_habitacion[0]))
        total = float(str(noches)) * float(precio_habitacion[0])
        variables.mensfac[9].set_text(str(total))
    except Exception as e:
        print(e)
        print('Error en obtener_factura')
