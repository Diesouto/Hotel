
# -*- coding: utf-8 -*-

"""
Módulo encargado de la gestión de ficheros excel para importar y exportar datos.
"""

from datetime import datetime
import xlrd
import xlwt
import funcionescli
import variables



def leerFichero(filename):
    """
    Importa clientes.

    Lee un fichero excel de clientes y los introduce en la bbdd.
    :param filename: Obtiene el nombre y la ruta del fichero
    :return: void
    """
    print(filename)
    document = xlrd.open_workbook(filename) #Abrimos el fichero excel "listadoclientes.xls"
    clientes = document.sheet_by_index(0) #Guarda cada una de las hojas y el número indica la hoja

    #Leemos el número de filas y columnas de la hoja de clientes
    filas_clientes = clientes.nrows
    fila = [0, 0, 0, 0]
    columnas_clientes = clientes.ncols
    print("Clientes tiene " + str(filas_clientes) + " filas y " + str(columnas_clientes) + " columnas")

    # Mostramos la informacion de todos los clientes
    for i in range(clientes.nrows+1): #Ignoramos la primera fila, que indica los campos
            for j in range(clientes.ncols):
                fila[j] = clientes.cell_value(i,j)
                    #fila[j] = datetime(*xlrd.xldate_as_tuple(clientes.cell_value(i,j), document.datemode))
            try:
                funcionescli.insertarcli(fila)
            except:
                print("Hay un dni repetido")
                fila = [0,0,0,0]

    print("Se ha terminado de importar")
    funcionescli.listadocli(variables.listclientes)
# Ejemplo de creación de hoja Excel

#definimos los estilos

def exportarBBDD():

    """
    Exporta clientes.

    Exporta los clientes de la bbdd a un fichero excel que crea el sistema.
    :return: void
    """

    style0 = xlwt.easyxf('font: name Times New Roman, colour red, bold on')
    style1 = xlwt.easyxf('', num_format_str='DD-MM-YYYY')

    #Creamos un fichero excel
    wb = xlwt.Workbook()

    #le añadimos una hoja llamada NuevoClientes que permite sobreescribir celdas
    ws = wb.add_sheet('NuevoClientes', cell_overwrite_ok=True)
    ws.write(0, 0, 'DNI', style0)
    ws.write(0, 1, 'APELIDOS', style0)
    ws.write(0, 2, 'NOMBRE', style0)
    ws.write(0, 3, 'FECHA ALTA', style0)

    #AQUÍ CONSULTAMOS UN LISTADO DE CLIENTES DE LA BASE DE DATOS
    listado = funcionescli.listar()
    #AQUÍ LO VAMOS RECORRIENDO E INSERTANDO EN LA CELDA CORRESPONDIENTE
    i = 1
    for registro in listado:
        j = 0
        for dato in registro[1:5]:
            ws.write(i, j, dato, style1)
            j += 1
        i += 1

    #GUARDAMOS LA HOJA DE CÁLCULO
    wb.save('example.xls')
















