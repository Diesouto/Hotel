
# -*- coding: utf-8 -*-

'''
Almacena variables.

El módulo variables almacena variables que necesitamos
en otros módulos.
+Módulo clientes:
    *filacli: almacena los valores del entry
    *listcliente: almacena los valores a mostrar en el treeview
    *treecliente: almacena el widget que contiene los valores de listcliente
+Módulo reservas:
    *filareserva: almacena los valores del entry
    *listreservas: almacena los valores a mostrar en el treeview
    *treereservas: almacena el widget que contiene los valores de listreserva
+Módulo habitación:
    *filahab: almacena los valores del entry
    *listhab: almacena los valores a mostrar en el treeview
    *treehab: almacena el widget que contiene los valores de listhab
+Módulo factura:
    *mensfac: contiene labels para mostrar información de la factura
+Módulo variables:
    *t: es un timer
+Ventanas o labels:
    *menslabel: contiene labels de aviso o advertencia, como el label para validar el dni
    *vencalendar: contiene la ventana de diálogo del calendario
    *venacercade: contiene la ventana de acerca de
    *vendialogsalir: contiene la ventana de diálogo de salir
+Otros:
    *neobackup: contiene la fecha y ruta de una backup de la bbdd
    *semaforo: permite saber a que calendario debemos controlar
'''

filacli = ()
listclientes = ()
treeclientes = ()
treereservas = ()
listreservas =()
menslabel = ()
labels_factura = ()
mensfac = ()
listado = ()
vencalendar = None
calendar = None
filahab = ()
filarbt = ()
treehab = ()
listhab = ()
venacercade = None
panel = None
listcmbhab = ()
cmbhab = None
filareserva = ()
semaforo = None
check = ()
filechooserbackup = None
filechooserimport = None
neobackup = None
numhabres = None
reserva = None
vendialogsalir = None
t = None
cod = None
switch = None
filaservicio = ()
lblservicio = ()
listservicios = ()
treeservicios = ()
