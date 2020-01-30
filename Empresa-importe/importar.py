
import xlrd
import xlwt
import funcionescli
import variables

def leerFichero():
    document = xlrd.open_workbook("listadoclientes.xls") #Abrimos el fichero excel
    clientes = document.sheet_by_index(0) #Guarda cada una de las hojas y el número indica la hoja

    #Leemos el número de filas y columnas de la hoja de clientes
    filas_clientes = clientes.nrows
    fila = [0, 0, 0, 0]
    columnas_clientes = clientes.ncols
    print("Clientes tiene " + str(filas_clientes) + " filas y " + str(columnas_clientes) + " columnas")

    #Mostramos el contenido de todas las filas de la hoja de clientes
    #for i in range(clientes.nrows): # nos interesa en este caso la filas, e ignoramos la primera
    #    if(i!=0 or i!=1):
    #        fila = clientes.row(i) #libros.col(i) para mostrar las columnas
    #        funcionescli.insertarcli(fila)
    # o lo insertamos en la base de datos

    # Mostramos la informacion de todos los clientes
    for i in range(clientes.nrows-1): #Ignoramos la primera fila, que indica los campos
            for j in range(clientes.ncols):
                fila[j] = (clientes.cell_value(i,j))
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
    style0 = xlwt.easyxf('font: name Times New Roman, colour red, bold on')
    style1 = xlwt.easyxf('',num_format_str='DD-MM-YYYY')

    #Creamos un fichero excel
    wb = xlwt.Workbook()
    #le añadimos una hoja llamada NuevoClientes que permite sobreescribir celdas
    ws = wb.add_sheet('NuevoClientes', cell_overwrite_ok=True)
    ws.write(0, 0, 'DNI', style0)
    ws.write(0, 0, 'APELIDOS', style0)
    ws.write(0, 2, 'NOMBRE', style0)
    ws.write(0, 3, 'FECHA ALTA', style1)
    #AQUÍ CONSULTAMOS UN LISTADO DE CLIENTES DE LA BASE DE DATOS
    listado = funcionescli.listar()
    #AQUÍ LO VAMOS RECORRIENDO E INSERTANDO EN LA CELDA CORRESPONDIENTE
    for registro in range(len(listado)):
        for i in range(listado.nrows - 1):  # Ignoramos la primera fila, que indica los campos
            for j in range(listado.ncols):
                for dato in range(registro):
                    ws.write(i, j, dato, style1)

    #GUARDAMOS LA HOJA DE CÁLCULO
    wb.save('example.xls')
















