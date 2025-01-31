from PyQt5 import QtWidgets, uic
from Controlador.arregloProovedor import *

aProv = ArregloProveedor()

class VentanaProovedor(QtWidgets.QMainWindow):
    Fila = -1

    def __init__(self, parent=None):
        super(VentanaProovedor, self).__init__(parent)
        uic.loadUi("Ui/ventanaProveedores.ui", self)
        self.show()
        
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.tblProveedores.clicked.connect(self.seleccionar)

        self.cboCategoria.addItems(["Categoría 1", "Categoría 2", "Categoría 3"])
    
    def obtenerDni(self):
        return self.txtDni.text()
    def obtenerRazonSocial(self):
        return self.txtRazonSocial.text()
    def obtenerTelefono(self):
        return self.txtTelefono.text()
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    def obtenerCategoria(self):
        return self.cboCategoria.currentText()
    
    def limpiarTabla(self):
        self.tblProveedores.clearContents()
        self.tblProveedores.setRowCount(6)
    
    def valida(self):
        if self.txtDni.text() == "":
            return "DNI del proveedor...!!!"
        elif self.txtRazonSocial.text() == "":
            return "Razón Social del proveedor...!!!"
        elif self.txtTelefono.text() == "":
            return "Teléfono del proveedor...!!!"
        elif self.txtDireccion.text() == "":
            return "Dirección del proveedor...!!!"
        else:
            return ""
    
    def listar(self):
        self.tblProveedores.setRowCount(aProv.tamañoArregloProveedor())
        self.tblProveedores.setColumnCount(5)
        self.tblProveedores.verticalHeader().setVisible(False)
        
        for i in range(aProv.tamañoArregloProveedor()):
            proveedor = aProv.devolverProveedor(i)
            self.tblProveedores.setItem(i, 0, QtWidgets.QTableWidgetItem(proveedor.getDNIProveedor()))
            self.tblProveedores.setItem(i, 1, QtWidgets.QTableWidgetItem(proveedor.getRazSoc()))
            self.tblProveedores.setItem(i, 2, QtWidgets.QTableWidgetItem(proveedor.getTelefono()))
            self.tblProveedores.setItem(i, 3, QtWidgets.QTableWidgetItem(proveedor.getDireccion()))
            self.tblProveedores.setItem(i, 4, QtWidgets.QTableWidgetItem(proveedor.getCategoria()))
    
    def limpiarControles(self):
        self.txtDni.clear()
        self.txtRazonSocial.clear()
        self.txtTelefono.clear()
        self.txtDireccion.clear()
    
    def registrar(self):
        if self.valida() == "":
            proveedor = Proveedores(self.obtenerDni(), self.obtenerRazonSocial(), self.obtenerTelefono(), self.obtenerDireccion(), self.obtenerCategoria())
            if aProv.buscarProveedor(self.obtenerDni()) == -1:
                aProv.adicionaProveedor(proveedor)
                aProv.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Proveedor", "El DNI ingresado ya existe... !!!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Proveedor", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)
    
    def consultar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Proveedor", "No existen proveedores a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Proveedor", "Ingrese el DNI a consultar")
            pos = aProv.buscarProveedor(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Proveedor", "El DNI ingresado no existe...!!!", QtWidgets.QMessageBox.Ok)
            else:
                proveedor = aProv.devolverProveedor(pos)
                self.txtDni.setText(proveedor.getDNIProveedor())
                self.txtRazonSocial.setText(proveedor.getRazSoc())
                self.txtTelefono.setText(proveedor.getTelefono())
                self.txtDireccion.setText(proveedor.getDireccion())
                self.cboCategoria.setCurrentText(proveedor.getCategoria())
    
    def eliminar(self):
        dni = self.txtDni.text()
        pos = aProv.buscarProveedor(dni)
        if pos != -1:
            aProv.eliminarProveedor(pos)
            aProv.grabar()
            self.limpiarControles()
            self.listar()
    
    def seleccionar(self):
        self.Fila = self.tblProveedores.currentRow()
    
    def quitar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Proveedor", "No existen proveedores a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            if self.Fila != -1:
                dni = self.tblProveedores.item(self.Fila, 0).text()
                pos = aProv.buscarProveedor(dni)
                if pos != -1:
                    aProv.eliminarProveedor(pos)
                    aProv.grabar()
                    self.limpiarTabla()
                    self.listar()
                    self.Fila = -1
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Proveedor", "Debe seleccionar una fila...!!!", QtWidgets.QMessageBox.Ok)
    
    def modificar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Proveedor", "No existen proveedores a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni = self.obtenerDni()
            pos = aProv.buscarProveedor(dni)
            if pos != -1:
                proveedor = Proveedores(self.obtenerDni(), self.obtenerRazonSocial(), self.obtenerTelefono(), self.obtenerDireccion(), self.obtenerCategoria())
                aProv.modificarProveedor(proveedor, pos)
                aProv.grabar()
                self.limpiarControles()
                self.listar()