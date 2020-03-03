
# -*- coding: utf-8 -*-

'''
el main contiene los elementos necesarios para lanzar la aplicación
así como la declaración de los widgets que se usarán. También los módulos
que tenemos que importar de las librerías gráficas

'''

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk

import eventos, conexion, variables
import funcionescli, funcioneshab, funcionesreser,funcionesvar



class Empresa:
    def __init__(self):
        #iniciamos la libreria Gtk
        self.b = Gtk.Builder()
        self.b.add_from_file('ventana.glade')

        #cargamos los widgets con algún evente asociado o que son referenciados
        vprincipal = self.b.get_object('venPrincipal')
        self.vendialog = self.b.get_object('venDialog')
        variables.venacercade = self.b.get_object('venAcercade')
        variables.panel = self.b.get_object('Panel')
        variables.filechooserbackup = self.b.get_object('fileChooserbackup')
        variables.filechooserimport = self.b.get_object('fileChooserImport')
        menubar = self.b.get_object('menuBar').get_style_context()

        #declaracion de wigdets
        entdni = self.b.get_object('entDni')
        entapel = self.b.get_object('entApel')
        entnome = self.b.get_object('entNome')
        entdatacli = self.b.get_object('entDatacli')
        lblerrdni = self.b.get_object('lblErrdni')
        lblcodcli = self.b.get_object('lblCodcli')
        lblnumnoches = self.b.get_object('lblNumnoches')
        lbldirbackup = self.b.get_object('lblFolderbackup')
        lbldnires = self.b.get_object('lblDnires')
        lblapelres = self.b.get_object('lblApelres')
        lblfactdni = self.b.get_object('lblfactdni')
        lblfactapel = self.b.get_object('lblfactapel')
        lblfactnom = self.b.get_object('lblfactnom')
        lblfactcod = self.b.get_object('lblfactcod')
        lblfacthab = self.b.get_object('lblfacthab')
        lblfechafact = self.b.get_object('lblFechaFactura')
        lblconceptofac = self.b.get_object('lblConceptoFact')
        lblunidadesuact = self.b.get_object('lblUnidadesFact')
        lblpreciofact = self.b.get_object('lblPrecioFact')
        lbltotalfact = self.b.get_object('lblTotalFact')
        variables.vencalendar = self.b.get_object('venCalendar')
        variables.vendialogsalir = self.b.get_object('vendialogSalir')
        variables.calendar = self.b.get_object('Calendar')
        variables.filacli = (entdni, entapel, entnome, entdatacli)
        variables.listclientes = self.b.get_object('listClientes')
        variables.treereservas = self.b.get_object('treeReservas')
        variables.listreservas = self.b.get_object('listReservas')
        variables.treeclientes = self.b.get_object('treeClientes')
        variables.menslabel = (lblerrdni, lblcodcli, lblnumnoches, lbldirbackup, lbldnires, lblapelres)
        variables.mensfac = (lblfactdni, lblfactapel, lblfactnom, lblfactcod, lblfacthab, lblfechafact, lblconceptofac, lblunidadesuact, lblpreciofact, lbltotalfact)

        #widgets habitaciones
        entnumhab = self.b.get_object('entNumhab')
        entprezohab = self.b.get_object('entPrezohab')
        rbtsimple = self.b.get_object('rbtSimple')
        rbtdoble = self.b.get_object('rbtDoble')
        rbtfamily = self.b.get_object('rbtFamily')
        variables.treehab = self.b.get_object('treeHab')
        variables.listhab = self.b.get_object('listHab')
        variables.filahab = (entnumhab, entprezohab)
        variables.filarbt = (rbtsimple, rbtdoble, rbtfamily)
        variables.listcmbhab = self.b.get_object('listcmbHab')
        variables.cmbhab = self.b.get_object('cmbNumres')
        variables.switch = self.b.get_object('switch')

        #widgtes reservas

        entdatain = self.b.get_object('entDatain')
        entdataout = self.b.get_object('entDataout')

        variables.filareserva = (entdni, entapel, entdatain, entdataout)

        #widgets servicios
        lblcodres = self.b.get_object('lblServicioReserva')
        lblcodhab = self.b.get_object('lblServicioHabitacion')
        entryservicio = self.b.get_object('entryServicio')
        entryprecio = self.b.get_object('entryPrecioServicio')

        variables.filaservicio = (entryservicio, entryprecio)
        variables.lblservicio = (lblcodres, lblcodhab)
        variables.treeservicios = self.b.get_object('treeServicios')
        variables.listservicios = self.b.get_object('listServicios')

        #conectamos
        self.b.connect_signals(eventos.Eventos())

        #conexion estilos

        self.set_style()
        menubar.add_class('menuBar')
        '''
        for i in range(len(variables.menserror)):
            variables.menserror[i].add_class('label')
        '''
        vprincipal.show_all()
        vprincipal.maximize()
        conexion.Conexion().abrirbbdd()
        funcionesreser.listadores()
        funcioneshab.listadonumhab()
        funcionescli.listadocli(variables.listclientes)
        funcioneshab.listadohab(variables.listhab)
        funcionesvar.controlhab()


    def set_style(self):
        """
        Permite añadir estilos a ciertos elementos del programa.

        :return: void
        """
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('estilos.css')
        Gtk.StyleContext().add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )


if __name__=='__main__':
    main = Empresa()
    Gtk.main()

