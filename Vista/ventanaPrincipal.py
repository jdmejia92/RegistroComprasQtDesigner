from PyQt5 import QtWidgets, uic
from Vista.ventanaClientes import *
from Vista.ventanaComprobante import *
from Vista.ventanaEmpleados import *
from Vista.ventanaProducto import *
from Vista.ventanaProveedores import *


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
      super(VentanaPrincipal, self).__init__(parent)
      uic.loadUi('Ui/ventanaPrincipal.ui', self)
      
      #Eventos: Llamada de opciones de menu
      self.actionClientes.triggered.connect(self.abrir_Ventana_Cliente)
      self.actionEmpleados.triggered.connect(self.abrir_Ventana_Empleados)
      self.actionProductos.triggered.connect(self.abrir_Ventana_Productos)
      self.actionProveedor.triggered.connect(self.abrir_Ventana_Proveedor)
      self.actionVista_Previa.triggered.connect(self.abrir_Ventana_Comprobante)

    def abrir_Ventana_Cliente(self):
      vclientes = VentanaClientes(self)
      vclientes.show()

    def abrir_Ventana_Empleados(self):
      vclientes = VentanaEmpleados(self)
      vclientes.show()

    def abrir_Ventana_Productos(self):
      vclientes = VentanaProductos(self)
      vclientes.show()

    def abrir_Ventana_Proveedor(self):
      vclientes = VentanaProovedor(self)
      vclientes.show()

    def abrir_Ventana_Comprobante(self):
      vclientes = VentanaComprobante(self)
      vclientes.show()

    def cerrar(self):
      self.close()