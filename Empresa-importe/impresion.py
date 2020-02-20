import datetime

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os, funcionescli

# -*- coding: utf-8 -*-

"""
Módulo encargado de generar la factura de un cliente
"""

def basico():
    """
    Imprime la información básica de la factura.
    :return: void
    Excepciones: Error de creación de PDF, imprime "Error en básico"
    """
    try:
        global bill
        bill = canvas.Canvas('prueba.pdf', pagesize=A4)
        text1 = 'Esperamos que vuelva pronto'
        text2 = 'CIF:00000000A '
        bill.drawImage('./img/logohotel.png', 475, 670 , width=64, height=64)
        bill.setFont('Helvetica-Bold', size=16)
        bill.drawString(250, 780, 'HOTEL LITE')
        bill.setFont('Times-Italic', size=10)
        bill.drawString(240,765, text1)
        bill.drawString(260, 755, text2)
        bill.line(50,660,540,660)
        textpie = ('Hotel Lite, CIF = 00000000A Tlfo = 986000000 mail = info@hotellite.com')
        bill.setFont('Times-Italic', size=8)
        bill.drawString(170,20,textpie)
        bill.line(50, 30, 540, 30)
    except:
        print('error en básico')


def factura(datosfactura):
    """
    Muestra la información del cliente en la factura.
    :param datosfactura: contiene todos los datos del cliente y su reserva necesarios para realizar la factura
    :return: void
    Excepciones: Error al obtener una variable, imprime "Error en módulo factura"
    """
    try:
        basico()
        bill.setTitle('FACTURA')
        bill.setFont('Helvetica-Bold', size= 8)
        text3 = 'Número de Factura:'
        bill.drawString(50,735, text3)
        bill.setFont('Helvetica', size=8)
        bill.drawString(140, 735, str(datosfactura[0]))
        bill.setFont('Helvetica-Bold', size=8)
        text4 = 'Fecha Factura:'
        bill.drawString(300, 735, text4)
        bill.setFont('Helvetica', size=8)
        bill.drawString(380, 735, (str(datetime.date.today())))
        bill.setFont('Helvetica-Bold', size = 8)
        text5 = 'DNI CLIENTE:'
        bill.drawString(50, 710, text5)
        bill.setFont('Helvetica', size=8)
        bill.drawString(120, 710, str(datosfactura[2]))
        bill.setFont('Helvetica-Bold', size=8)
        text6 = 'Nº de Habitación:'
        bill.drawString(300, 710, text6)
        bill.setFont('Helvetica', size=8)
        bill.drawString(380, 710, str(datosfactura[3]))
        apelnome = funcionescli.apelnomfac(str(datosfactura[2]))
        print(apelnome)
        bill.setFont('Helvetica-Bold', size=8)
        text7 = 'APELLIDOS:'
        bill.drawString(50, 680, text7)
        bill.setFont('Helvetica', size=9)
        bill.drawString(110, 680, str(apelnome[0]))
        bill.setFont('Helvetica-Bold', size=8)
        text8 = 'NOMBRE:'
        bill.drawString(300, 680, text8)
        bill.setFont('Helvetica', size=9)
        bill.drawString(350, 680, str(apelnome[1]))
        bill.showPage()
        bill.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/prueba.pdf')

    except:
        print('Error en módulo factura')

