
# -*- coding: utf-8 -*-

"""
módulo encargado de la conexión entre la interfaz de usuario y el programa.
"""

import gi

import funcionesservicio

gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import conexion, variables, funcionescli, funcioneshab, funcionesreser, funcionesvar, importar,facturacion, impresion
import os, shutil
from datetime import date, datetime, time


class Eventos():


# eventos generales
    def on_acercade_activate(self, widget):
        """
        Muestra la ventana acerca de cuando se presiona sobre el botón.
        :param widget: Acerca de en la barra de herramientas
        :return: void
        Excepciones: Error al abrir la ventana de diálogo
        """
        try:
            variables.venacercade.show()
        except:
            print('error abrira acerca de')

    def on_btnCerrarabout_clicked(self, widget):
        """
        Cierra la ventana de acerca de.
        :param widget: Botón cerrar de la ventana Acerca de
        :return: void
        """

        try:
            variables.venacercade.connect('delete-event', lambda w, e: w.hide() or True)
            variables.venacercade.hide()
        except:
            print('error abrir calendario')


    def on_menuBarbackup_activate(self, widget):
        """
        Realiza una backup de la bbdd cuando se presiona el botón correspondiente.
        :param widget: Backup de la barra de herramientas
        :return: void
        Excepciones: Error al abrir la ventana, imprime "error abrir file choose backup"
        """
        try:
            variables.filechooserbackup.show()
            variables.neobackup = funcionesvar.backup()
            variables.neobackup = str(os.path.abspath(variables.neobackup))
            print(variables.neobackup)

        except:
            print('error abrir file choose backup')


    def on_menuBarImportar_activate(self, widget):
        """
        Importa clientes de un fichero excel al presionar el botón correspondiente.
        :param widget: Importar en la barra de menú
        :return: void
        Excepciones: Error al abrir la ventana, muestra el error
        """
        try:
            variables.filechooserimport.show()
        except Exception as e:
            print(e)


    def on_menuBarExportar_activate(self, widget):
        """
        Exporta clientes a un fichero excel al presionar el botón correspondiente.
        :param widget: Exportar en la barra de menú
        :return: void
        Excepciones: Error de operación, muestra el error
        """
        try:
            importar.exportarBBDD()
        except Exception as e:
            print(e)


    def on_menuBarsalir_activate(self, widget):
        """
        Termina la ejecución del programa al presionar el botón correspondiente.
        :param widget: Salir en la barra de menú
        :return: void
        """
        try:
            self.salir()
        except:
            print('salir en menubar')

    def salir(self):
        """
        Termina la ejecución del programa, cierra las ventanas y la conexión con la bbdd.
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            conexion.Conexion.cerrarbbdd(self)
            funcionesvar.cerrartimer()
            Gtk.main_quit()
        except:
            print('error función salir')

    def on_venPrincipal_destroy(self, widget):
        """
        Termina el programa cuando se cierra la ventana principal.
        :param widget: Ventana principal
        :return: void
        """
        self.salir()

    def on_btnSalirtool_clicked(self, widget):
        """
        Muestra la ventana de diálogo de salir.
        :param widget: Botón salir
        :return: void
        """
        variables.vendialogsalir.show()

    def on_btnCancelarsalir_clicked(self, widget):
        """
        Cierra la ventana de diálogo de salir.
        :param widget: Botón cancelar en la ventana de diálogo Salir
        :return: void
        """
        variables.vendialogsalir.connect('delete-event', lambda w, e: w.hide() or True)
        variables.vendialogsalir.hide()

    def on_btnAceptarsalir_clicked(self, widget):
        """
        Termina la ejecución del programa.
        :param widget: botón Salir en la ventana de diálogo salir.
        :return: void
        """
        self.salir()
    """
    Eventos Clientes
    """

    def on_btnAltacli_clicked(self, widget):
        """
        Realiza el alta de un cliente.
        Obtiene la información de los widgets de entrada, valida si el
        dni es correcto e inserta al cliente en la bbdd.
        :param widget: Botón Alta en Clientes
        :return: void
        Excepciones: DNI inválido o la existencia de ese cliente en la bbdd, imprime mensaje de error
        """
        try:
            dni = variables.filacli[0].get_text()
            apel = variables.filacli[1].get_text()
            nome = variables.filacli[2].get_text()
            data = variables.filacli[3].get_text()
            registro = (dni, apel, nome, data)
            if funcionescli.validoDNI(dni):
                funcionescli.insertarcli(registro)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                variables.menslabel[0].set_text('ERROR DNI')
        except:
            print("Error alta cliente")

#botón baja cliente.

    def on_btnBajacli_clicked(self, widget):
        """
        Elimina a un cliente de la bbdd.
        Obtiene el cliente a borrar por el dni que se
        encuentre en el entry en ese momento.
        :param widget: Botón baja en clientes
        :return: void
        Excepciones: Entry vacío o ausencia de cliente en la bbdd, imprime mensaje de error
        """
        try:
            dni = variables.filacli[0].get_text()
            if dni != '' :
                funcionescli.bajacli(dni)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                print('falta dni u otro error')
        except:
            print("error en botón baja cliente")

#  modificamos cliente
    def on_btnModifcli_clicked(self, widget):
        """
        Modifica los datos de un cliente en la bbdd.
        Recoge los nuevos datos y los inserta donde coincida
        el dni de entrada con el del cliente existente en la bbdd.
        :param widget: Botón Modificar en clientes
        :return: void
        Excepciones: Cliente no existe en la bbdd o dni inválido, imprime mensaje de error
        """
        try:
            cod = variables.menslabel[1].get_text()
            dni = variables.filacli[0].get_text()
            apel = variables.filacli[1].get_text()
            nome = variables.filacli[2].get_text()
            data = variables.filacli[3].get_text()
            registro = (dni, apel, nome, data)
            if dni != '':
                funcionescli.modifcli(registro, cod)
                funcionescli.listadocli(variables.listclientes)
                funcionescli.limpiarentry(variables.filacli)
            else:
                print('falta el dni')
        except:
            print('error en botón modificar')


# controla el valor del deni
    def on_entDni_focus_out_event(self, widget, dni):
        """
        Valida el dni intoducido.
        Controla si se ha introducido un dni válido cuando el ratón abandona el entry del dni
        y muestra un aviso por pantalla en un label.
        :param widget: Entry del dni clientes
        :param dni: contiene el dni a validar
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            dni = variables.filacli[0].get_text()
            if funcionescli.validoDNI(dni):
                variables.menslabel[0].set_text('')
                pass
            else:
                variables.menslabel[0].set_text('ERROR')
        except:
            print("Error alta cliente en out focus")


    def on_treeClientes_cursor_changed(self, widget):
        """
        Controla la selección de un cliente el el treeview de clientes.
        :param widget: treeview de clientes
        :return: void
        Excepciones: Error al obtener los datos del cliente, imprime mensaje de error
        """
        try:
            model,iter = variables.treeclientes.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            variables.menslabel[0].set_text('')
            funcionescli.limpiarentry(variables.filacli)
            if iter != None:
                sdni = model.get_value(iter, 0)
                sapel = model.get_value(iter, 1)
                snome = model.get_value(iter, 2)
                sdata = model.get_value(iter, 3)
                if sdata == None:
                    sdata = ''
                cod = funcionescli.selectcli(sdni)
                variables.menslabel[1].set_text(str(cod[0]))
                variables.filacli[0].set_text(str(sdni))
                variables.filacli[1].set_text(str(sapel))
                variables.filacli[2].set_text(str(snome))
                variables.filacli[3].set_text(str(sdata))
                variables.menslabel[4].set_text(str(sdni))
                variables.menslabel[5].set_text(str(sapel))

        except:
            print ("error carga cliente")

    def on_btnCalendar_clicked(self, widget):
        """
        Abre la ventana calendario para seleccionar una fecha en clientes.
        :param widget: botón calendar de clientes
        :return: void
        Excepciones: Error al abrir calendario, imprime mensaje de error
        """
        try:
            variables.semaforo = 1
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()

        except:
            print('error abrir calendario')

    def on_btnCalendarResIn_clicked(self,widget):
        """
        Abre la ventana calendario para seleccionar una fecha en la entrada de la reserva.
        :param widget: botón calendario checkin en reservas
        :return: void
        Excepciones: Error al abrir calendario, imprime mensaje de error
        """
        try:
            variables.semaforo = 2
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()
        except:
            print('error abrir calendario')

    def on_btnCalendarResOut_clicked(self, widget):
        """
        Abre la ventana calendario para seleccionar una fecha en la salida de la reserva
        :param widget: botón calendario checkout en reservas
        :return: void
        Excepciones: Error al abrir calendario, imprime mensaje de error
        """
        try:
            variables.semaforo  = 3
            variables.vencalendar.connect('delete-event', lambda w, e: w.hide() or True)
            variables.vencalendar.show()
        except:
            print('error abrir calendario')

    def on_Calendar_day_selected_double_click(self, widget):
        """
        Guarda la fecha en el calendario al hacer doble click
        :param widget: calendario
        :return: void
        Excepciones: Error al obtener la fecha, imprime mensaje de error
        """
        try:
            agno, mes, dia = variables.calendar.get_date()
            fecha = "%02d/" % dia + "%02d/" % (mes + 1) + "%s" % agno
            if variables.semaforo == 1:
                variables.filacli[3].set_text(fecha)
            elif variables.semaforo == 2:
                variables.filareserva[2].set_text(fecha)
            elif variables.semaforo == 3:
                variables.filareserva[3].set_text(fecha)
                funcionesreser.calculardias()
            else:
                pass
            #variables.semaforo = 0
            variables.vencalendar.hide()
        except:
            print('error al coger la fecha')


# Eventos de las habitaciones

    def on_btnAltahab_clicked(self, widget):
        """
        Realiza el alta de una habitación en la bbdd.
        Recoge y almacena los valores de los entrys de habitaciones
        :param widget: botón alta en habitaciones
        :return: void
        Excepciones: Campos vacíos o habitación existente, imprime mensaje de error
        """
        try:
            numhab = variables.filahab[0].get_text()
            prezohab = variables.filahab[1].get_text()
            prezohab = prezohab.replace(',','.')
            prezohab = float(prezohab)
            prezohab = round(prezohab,2)
            if variables.filarbt[0].get_active():
                tipo = 'simple'
            elif variables.filarbt[1].get_active():
                tipo = 'doble'
            elif variables.filarbt[2].get_active():
                tipo = 'family'
            else:
                pass

            if variables.switch.get_active():
                libre = 'SI'
            else:
                libre = 'NO'
            registro = (numhab, tipo, prezohab, libre)
            if numhab != None:
               funcioneshab.insertarhab(registro)
               funcioneshab.listadohab(variables.listhab)
               funcioneshab.listadonumhab()
               funcioneshab.limpiarentry(variables.filahab)
            else:
                pass
        except:
            print("Error alta habitacion")

    def on_treeHab_cursor_changed(self, widget):
        """
        Permite seleccionar una habitación en el treeview de habitaciones.
        :param widget: treeview habitaciones
        :return: void
        Excepciones: Error de selección, imprime mensaje de error
        """
        try:
            model, iter = variables.treehab.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            funcioneshab.limpiarentry(variables.filahab)
            if iter != None:
                snumhab = model.get_value(iter, 0)
                stipo = model.get_value(iter, 1)
                sprezo = model.get_value(iter, 2)
                sprezo = round(sprezo,2)
                variables.filahab[0].set_text(str(snumhab))
                variables.filahab[1].set_text(str(sprezo))
                if stipo == str('simple'):
                    variables.filarbt[0].set_active(True)
                elif stipo == str('doble'):
                    variables.filarbt[1].set_active(True)
                elif stipo == str('family'):
                    variables.filarbt[2].set_active(True)
                slibre = model.get_value(iter,3)
                if slibre == str('SI'):
                    variables.switch.set_active(True)
                else:
                    variables.switch.set_active(False)
        except:
            print("error carga habitacion")


    def on_btnBajahab_clicked(self,widget):
        """
        Elimina una habitación seleccionada de la bbdd.
        :param widget: botón baja en habitaciones
        :return: void
        Excepciones: Número de habitación inexistente en la bbdd o mal introducido, imprime mensaje de error
        """
        try:
            numhab = variables.filahab[0].get_text()
            if numhab != '':
                funcioneshab.bajahab(numhab)
                funcioneshab.limpiarentry(variables.filahab)
                funcioneshab.listadohab(variables.listhab)
            else:
                pass
        except:
            print('borrar baja hab')


    def on_btnModifhab_clicked(self, widget):
        """
        Modifica los datos de una habitación concreta.
        Obtiene los nuevos datos de los entrys de habitación y
        modifica la habitación de la bbdd con el mismo número que la del entry.
        :param widget: botón modificar en habitaciones
        :return: void
        Excepciones: Número de habitación incorrecto o inexistente, imprime mensaje de error
        """
        try:
            numhab = variables.filahab[0].get_text()
            prezo = variables.filahab[1].get_text()
            if variables.switch.get_active():
                libre = 'SI'
            else:
                libre = 'NO'

            if variables.filarbt[0].get_active():
                tipo = 'simple'
            elif variables.filarbt[1].get_active():
                tipo = 'doble'
            elif variables.filarbt[2].get_active():
                tipo = 'family'
            else:
                pass
            registro = (prezo, tipo, libre)
            if numhab != '':
                funcioneshab.modifhab(registro, numhab)
                funcioneshab.listadohab(variables.listhab)
                funcioneshab.limpiarentry(variables.filahab)
            else:
                print('falta el numhab')
        except:
            print('error modif hab')


    # eventos de los botones del toolbar

    def on_Panel_select_page(self, widget):
        """
        Cambia la ventana que se muestra al usuario cuando este
        selecciona un panel distinto.
        :param widget:
        :return: void
        """
        try:
            funcioneshab.listadonumhab()
        except:
            print("error botón cliente barra herramientas")

    def on_btnClitool_clicked (self, widget):
        """
        Cambia la ventana del panel a la de Clientes.
        :param widget: panel clientes
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 0:
                variables.panel.set_current_page(0)
            else:
                pass
        except:
            print("error botón cliente barra herramientas")

    def on_btnReservatool_clicked(self, widget):
        """
        Cambia la ventana del panel a la de Reservas
        :param widget: panel reserva
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 1:
                variables.panel.set_current_page(1)
                funcioneshab.listadonumhab(self)
            else:
                pass
        except:
            print("error botón cliente barra herramientas")

    def on_btnHabita_clicked(self,widget):
        """
        Cambia la ventana del panel a la de Habitaciones
        :param widget: panel habitaciones
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            panelactual = variables.panel.get_current_page()
            if panelactual != 2:
                variables.panel.set_current_page(2)
            else:
                pass
        except:
            print("error botón habitacion barra herramientas")

    def on_btnCalc_clicked(self, widget):
        """
        Abre una calculadora
        :param widget: botón calculadora de la barra de herramientas
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            os.system('/snap/bin/gnome-calculator')
        except:
            print('error lanzar calculadora')

    def on_btnRefresh_clicked(self, widget):
        """
        Limpia todos los entry del programa
        :param widget: botón refresh de la barra de herramientas
        :return: void
        Excepciones: Error al obtener los entry, imprime mensaje de error
        """
        try:
            funcioneshab.limpiarentry(variables.filahab)
            funcionescli.limpiarentry(variables.filacli)
            funcionesreser.limpiarentry(variables.filareserva)
        except:
            print('error referes')

    def on_btnBackup_clicked(self, widget):
        """
        Abre la ventana de backup.
        Abre una ventana de diálogo que permite seleccionar donde se
        realizará la copia de la bbdd.
        :param widget: botón Backup de la barra de herramientas
        :return: void
        Excepciones: Error al abrir la ventana, imprime mensaje de error
        """
        try:
            variables.filechooserbackup.show()
            variables.neobackup = funcionesvar.backup()
            variables.neobackup = str(os.path.abspath(variables.neobackup))
            print(variables.neobackup)

        except:
            print('error abrir file choorse backup')

    def on_btnGrabarbackup_clicked(self, widget):
        """
        Hace una backup de la bbdd.
        Realiza una copia de la bbdd actual y la comprime en zip
        en el destino solicitado.
        :param widget: botón grabar en la ventana de Backup
        :return: void
        Excepciones: Error de selección de fichero, imprime mensaje de error
        """
        try:
            destino = variables.filechooserbackup.get_filename()
            destino = destino + '/'
            variables.menslabel[3].set_text(str(destino))
            if shutil.move(str(variables.neobackup), str(destino)):
                variables.menslabel[3].set_text('Copia de Seguridad Creada')
        except:
            print('error dselect fichero')


    def on_btnCancelfilechooserbackup_clicked(self, widget):
        """
        Cierra la ventana de diálogo de selección de ficheros.
        :param widget: botón cerrar en la ventana de backup
        :return: void
        Excepciones: Error al cerrar la ventana, imprime mensaje de error
        """
        try:
            variables.filechooserbackup.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserbackup.hide()
        except:
            print('error cerrar file chooser')

    def on_btnImporta_clicked(self, widget):
        """
        Importa clientes a la bbdd desde un fichero excel.
        :param widget: botón importar en la ventana de Importar
        :return: void
        Excepciones: Error de selección de fichero, imprime mensaje de error
        """
        try:
            destino = variables.filechooserimport.get_filename()
            importar.leerFichero(destino)
        except:
            print('error dselect fichero')


    def on_btnCancelarImportar_clicked(self, widget):
        """
        Cierra la ventana de diálogo de selección de fichero.
        :param widget: botón cancelar en la ventana de Importar
        :return: void
        Excepciones: Error al cerrar la ventana, imprime mensaje de error
        """
        try:
            variables.filechooserimport.connect('delete-event', lambda w, e: w.hide() or True)
            variables.filechooserimport.hide()
        except:
            print('error cerrar file chooser')

## reservas

    def on_cmbNumres_changed(self, widget):
        try:
            index = variables.cmbhab.get_active()
            model = variables.cmbhab.get_model()
            item = model[index]
            variables.numhabres = item[0]
        except:
            print('error mostrar habitacion combo')

    def on_btnAltares_clicked(self, widget):
        """
        Inserta una reserva en la bbdd.
        Controla que la habitación a reservar no esté ocupada y obtiene los
        datos necesarios de la habitación y del cliente.
        :param widget: botón Alta en reservas
        :return: void
        Excepciones: Error al obtener los datos, imprime mensaje de error
        """
        try:
            if variables.reserva == 1:
                dnir = variables.menslabel[4].get_text()
                chki = variables.filareserva[2].get_text()
                chko = variables.filareserva[3].get_text()
                noches = int(variables.menslabel[2].get_text())
                registro = (dnir, variables.numhabres, chki, chko, noches)
                if funcionesreser.versilibre(variables.numhabres):
                    funcionesreser.insertares(registro)
                    funcionesreser.listadores()
                    #actualizar a NO
                    libre = ['NO']
                    funcioneshab.cambiaestadohab(libre, variables.numhabres)
                    funcioneshab.listadohab(variables.listhab)
                    funcioneshab.limpiarentry(variables.filahab)
                    funcionesreser.limpiarentry(variables.filareserva)
                else:
                    print ('habitación ocupada')
        except:
            print ('error en alta res')

    def on_btnRefreshcmbhab_clicked(self, widget):
        """
        Limpia los entry del combo hotel.
        :param widget: botón refresh
        :return: void
        Excepciones: Error al obtener los entry, imprime mensaje de error
        """
        try:
            variables.cmbhab.set_active(-1)
            funcioneshab.listadonumhab(self)
        except:
            print ('error limpiar combo hotel')

    def on_treeReservas_cursor_changed(self, widget):
        """
        Selecciona una reserva.
        Permite seleccionar una reserva en el treeview de Reservas y obtener sus datos.
        Los datos obtenidos nos permiten crear una factura.
        :param widget: treeview reservas
        :return: void
        Excepciones: Error al obtener los datos, imprime mensaje de error
        """
        try:
            model, iter = variables.treereservas.get_selection().get_selected()
            # model es el modelo de la tabla de datos
            # iter es el número que identifica a la fila que marcamos
            funcionesreser.limpiarentry(variables.filareserva)
            if iter != None:
                variables.codr = model.get_value(iter,0)
                sdni = model.get_value(iter, 1)
                sapel = funcionesreser.buscarapelcli(str(sdni))
                snome = funcionesreser.buscarnome(str(sdni))
                snumhab =  model.get_value(iter, 2)
                lista = funcioneshab.listadonumhabres()
                m = -1
                for i, x in enumerate(lista):
                    if str(x[0]) == str(snumhab):
                        m = i
                variables.cmbhab.set_active(m)
                schki = model.get_value(iter, 3)
                schko = model.get_value(iter,4)
                snoches = model.get_value(iter, 5)
                variables.menslabel[4].set_text(str(sdni))
                variables.menslabel[5].set_text(str(sapel[0]))
                variables.menslabel[2].set_text(str(snoches))
                variables.filareserva[2].set_text(str(schki))
                variables.filareserva[3].set_text(str(schko))

                facturacion.obtener_factura(str(sdni), str(sapel[0]), snome[0], variables.codr, snumhab, snoches)

                global datosfactura
                datosfactura = (variables.codr, snoches, sdni, snumhab, snoches)

                #servicios
                variables.lblservicio[0].set_text(str(variables.codr))
                variables.lblservicio[1].set_text(str(snumhab))

        except:
            print ('error cargar valores de reservas')


    def on_btnBajares_clicked(self, widget):
        """
        Borra una reserva de la bbdd.
        :param widget: botón Borrar en reservas
        :return: void
        Excepciones: Error al obtener los datos, imprime mensaje de error
        """
        try:
            libre = ['SI']
            numhabres = variables.numhabres
            funcionesreser.bajareserva(variables.codr)
            funcioneshab.cambiaestadohab(libre, numhabres)
            funcionesreser.limpiarentry(variables.filareserva)
            funcionesreser.listadores()
            funcioneshab.listadohab(variables.listhab)

        except:
            print('error baja reserva')

    def on_btnModifres_clicked(self, widget):
        """
        Modifica los datos de una reserva en la bbdd.
        :param widget: botón modificar en reserva
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            dnir = variables.menslabel[4].get_text()
            chki = variables.filareserva[2].get_text()
            chko = variables.filareserva[3].get_text()
            noches = int(variables.menslabel[2].get_text())
            registro = (dnir, variables.numhabres, chki, chko, noches)
            funcionesreser.modifreserva(registro, variables.codr)
            funcionesreser.limpiarentry(variables.filareserva)
            funcionesreser.listadores()

        except:
            print('error modificar reserva')

    def on_btChkout_clicked(self, widget):
        """
        Realiza el check out de un cliente.
        Cambia el estado de la habitación ocupada a libre.
        :param widget: botón checkout en reserva
        :return: void
        Excepciones: Error al obtener los datos, imprime mensaje de error
        """
        try:
            chko = variables.filareserva[3].get_text()
            today = date.today()
            print(chko)

            hoy = datetime.strftime(today,'%d/%m/%Y')
            print(hoy)
            registro = (variables.numhabres)
            if str(hoy) == str(chko):
                funcioneshab.modifhabres(registro)
                funcioneshab.listadohab(variables.listhab)
            else:
                print('puede facturar')
                #cambiar el estado de la habitación de ocupada a libre

        except:
            print('error en checkout')

    def on_btnPrintfac_clicked(self, widget):
        """
        Crea la factura de la reserva deseada.
        :param widget: botón imprimir de la ventana de aplicación
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            impresion.factura(datosfactura)
        except Exception as e:
            print(e)


    def on_btImprestool_clicked(self, widget):
        """
        Crea la factura de la reserva deseada.
        :param widget: botón imprimir de la barra de herramientas
        :return: void
        Excepciones: Error de operación, imprime mensaje de error
        """
        try:
            impresion.factura(datosfactura)
        except Exception as e:
            print(e)


    def btnCrearServicio_clicked(self, widget):
        try:
            reserva = variables.lblservicio[0].get_text()
            nombre = variables.filaservicio[0].get_text()
            precio = variables.filaservicio[1].get_text()
            funcionesservicio.insertares()
