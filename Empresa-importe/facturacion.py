import funcionesreser
import variables
import datetime


def limpiar_labels_factura(labels_factura):
    for i in range(len(labels_factura)):
        labels_factura[i].set_text('')


def obtener_factura(dni, apellidos, nombre, cod, numero_habitacion, noches):
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
