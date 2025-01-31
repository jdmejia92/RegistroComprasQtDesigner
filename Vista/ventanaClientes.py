from PyQt5 import QtWidgets, uic
from Controlador.arregloClientes import *

aCli = ArregloClientes()

class VentanaClientes(QtWidgets.QMainWindow):
    Fila = -1

    def __init__(self, parent=None):
        super(VentanaClientes, self).__init__(parent)
        uic.loadUi("Ui/ventanaClientes.ui", self)
        self.show()
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.tblClientes.clicked.connect(self.Seleccionar)

        # Cargar clientes al iniciar
        self.listar()

    def obtenerDni(self):
        return self.txtDni.text()

    def obtenerNombres(self):
        return self.txtNombres.text()

    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()

    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()

    def obtenerDireccion(self):
        return self.txtDireccion.text()

    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del cliente...!!!"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del cliente...!!!"
        elif self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del cliente...!!!"
        elif self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del cliente...!!!"
        elif self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del cliente...!!!"
        elif self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del cliente...!!!"
        else:
            return ""

    def listar(self):
        self.tblClientes.setRowCount(aCli.tamannoArregloClientes())
        self.tblClientes.setColumnCount(6)
        # Cabecera
        self.tblClientes.verticalHeader().setVisible(False)
        for i in range(aCli.tamannoArregloClientes()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getDniCliente()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getNombreCliente()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getApellidoPaternoCliente()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getApellidoMaternoCliente()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getDireccionCliente()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverClientes(i).getTelefonoCliente()))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    def registrar(self):
        if self.valida() == "":
            objCli = Cliente(
                self.obtenerDni(),
                self.obtenerNombres(),
                self.obtenerApellidoPaterno(),
                self.obtenerApellidoMaterno(),
                self.obtenerDireccion(),
                self.obtenerTelefono()
            )
            dni = self.obtenerDni()
            if aCli.buscarCliente(dni) == -1:
                aCli.adicionaCliente(objCli)
                aCli.grabar()
                self.limpiarControles()
                self.listar()
                QtWidgets.QMessageBox.information(self, "Registrar Cliente",
                                                 "Cliente registrado correctamente.",
                                                 QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente",
                                                 "El DNI ingresado ya existe...!!!",
                                                 QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente",
                                             "Error en " + self.valida(),
                                             QtWidgets.QMessageBox.Ok)

    def consultar(self):
        if aCli.tamannoArregloClientes() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Cliente",
                                             "No existen clientes a consultar...!!!",
                                             QtWidgets.QMessageBox.Ok)
        else:
            dni, ok = QtWidgets.QInputDialog.getText(self, "Consultar Cliente",
                                                    "Ingrese el DNI a consultar")
            if ok and dni:
                pos = aCli.buscarCliente(dni)
                if pos == -1:
                    QtWidgets.QMessageBox.information(self, "Consultar Cliente",
                                                     "El DNI ingresado no existe...!!!",
                                                     QtWidgets.QMessageBox.Ok)
                else:
                    self.txtDni.setText(aCli.devolverClientes(pos).getDniCliente())
                    self.txtNombres.setText(aCli.devolverClientes(pos).getNombreCliente())
                    self.txtApellidoPaterno.setText(aCli.devolverClientes(pos).getApellidoPaternoCliente())
                    self.txtApellidoMaterno.setText(aCli.devolverClientes(pos).getApellidoMaternoCliente())
                    self.txtDireccion.setText(aCli.devolverClientes(pos).getDireccionCliente())
                    self.txtTelefono.setText(aCli.devolverClientes(pos).getTelefonoCliente())

    def eliminar(self):
        dni = self.txtDni.text()
        if dni:
            pos = aCli.buscarCliente(dni)
            if pos != -1:
                aCli.eliminarCliente(pos)
                aCli.grabar()
                self.limpiarControles()
                self.listar()
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                                 "Cliente eliminado correctamente.",
                                                 QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                                 "El DNI ingresado no existe...!!!",
                                                 QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                             "Debe ingresar un DNI...!!!",
                                             QtWidgets.QMessageBox.Ok)

    def Seleccionar(self):
        self.Fila = self.tblClientes.currentRow()

    def quitar(self):
        if aCli.tamannoArregloClientes() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                             "No existen clientes a eliminar...!!!",
                                             QtWidgets.QMessageBox.Ok)
        else:
            if self.Fila != -1:
                dni = self.tblClientes.item(self.Fila, 0).text()
                pos = aCli.buscarCliente(dni)
                if pos != -1:
                    aCli.eliminarCliente(pos)
                    aCli.grabar()
                    self.limpiarTabla()
                    self.listar()
                    self.Fila = -1
                    QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                                     "Cliente eliminado correctamente.",
                                                     QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                                 "Debe seleccionar una fila...!!!",
                                                 QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aCli.tamannoArregloClientes() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente",
                                             "No existen clientes a modificar...!!!",
                                             QtWidgets.QMessageBox.Ok)
        else:
            dni = self.obtenerDni()
            pos = aCli.buscarCliente(dni)
            if pos != -1:
                objCli = Cliente(
                    self.obtenerDni(),
                    self.obtenerNombres(),
                    self.obtenerApellidoPaterno(),
                    self.obtenerApellidoMaterno(),
                    self.obtenerDireccion(),
                    self.obtenerTelefono()
                )
                aCli.modificarCliente(objCli, pos)
                aCli.grabar()
                self.limpiarControles()
                self.listar()
                QtWidgets.QMessageBox.information(self, "Modificar Cliente",
                                                 "Cliente modificado correctamente.",
                                                 QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, "Modificar Cliente",
                                                 "El DNI ingresado no existe...!!!",
                                                 QtWidgets.QMessageBox.Ok)