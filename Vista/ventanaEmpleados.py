from PyQt5 import QtWidgets, uic
from Controlador.arregloEmpleados import *

aEmp = ArregloEmpleados()

class VentanaEmpleados(QtWidgets.QMainWindow):
    Fila = -1

    def __init__(self, parent=None):
        super(VentanaEmpleados, self).__init__(parent)
        uic.loadUi("Ui/ventanaEmpleados.ui", self)
        self.show()
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.tableView.clicked.connect(self.Seleccionar)

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
        self.tableView.clearContents()
        self.tableView.setRowCount(6)

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del empleado...!!!"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del empleado...!!!"
        elif self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del empleado...!!!"
        elif self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del empleado...!!!"
        elif self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del empleado...!!!"
        elif self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del empleado...!!!"
        else:
            return ""

    def listar(self):
        self.tableView.setRowCount(aEmp.tamañoArregloEmpleados())
        self.tableView.setColumnCount(6)
        for i in range(0, aEmp.tamañoArregloEmpleados()):
            self.tableView.setItem(i, 0, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleados(i).getDniEmpleado()))
            self.tableView.setItem(i, 1, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleados(i).getNombresEmpleado()))
            self.tableView.setItem(i, 2, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleados(i).getApellidoPaternoEmpleado()))
            self.tableView.setItem(i, 3, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleados(i).getApellidoMaternoEmpleado()))
            self.tableView.setItem(i, 4, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleados(i).getDireccionEmpleado()))
            self.tableView.setItem(i, 5, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleados(i).getTelefonoEmpleado()))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    def registrar(self):
        if self.valida() == "":
            objEmp = Empleado(self.obtenerDni(), self.obtenerNombres(),
                              self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(),
                              self.obtenerDireccion(), self.obtenerTelefono())
            dni = self.obtenerDni()
            if aEmp.buscarEmpleado(dni) == -1:
                aEmp.adicionalEmpleado(objEmp)
                aEmp.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                  "El DNI ingresado ya existe... !!!", 
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                              "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        if aEmp.tamañoArregloEmpleados() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                              "No existen empleados a consultar...!!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Empleado", "Ingrese el DNI a consultar")
            pos = aEmp.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                  "El DNI ingresado no existe...!!! ", 
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aEmp.devolverEmpleados(pos).getDniEmpleado())
                self.txtNombres.setText(aEmp.devolverEmpleados(pos).getNombresEmpleado())
                self.txtApellidoPaterno.setText(aEmp.devolverEmpleados(pos).getApellidoPaternoEmpleado())
                self.txtApellidoMaterno.setText(aEmp.devolverEmpleados(pos).getApellidoMaternoEmpleado())
                self.txtDireccion.setText(aEmp.devolverEmpleados(pos).getDireccionEmpleado())
                self.txtTelefono.setText(aEmp.devolverEmpleados(pos).getTelefonoEmpleado())

    def eliminar(self):
        dni = self.txtDni.text()
        pos = aEmp.buscarEmpleado(dni)
        if pos != -1:
            aEmp.eliminarEmpleado(pos)
            aEmp.grabar()
            self.limpiarControles()
            self.listar()

    def Seleccionar(self):
        self.Fila = self.tableView.currentRow()

    def quitar(self):
        if aEmp.tamañoArregloEmpleados() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                              "No existen empleados a eliminar...!!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tableView.selectedItems()
            if self.Fila != -1:
                indiceFila = fila[0].row()
                dni = self.tableView.item(self.Fila, 0).text()
                pos = aEmp.buscarEmpleado(dni)
                aEmp.eliminarEmpleado(pos)
                aEmp.grabar()
                self.limpiarTabla()
                self.listar()
                self.Fila = -1
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                  "Debe seleccionar una fila...!!!",
                                                  QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aEmp.tamañoArregloEmpleados() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Empleado",
                                              "No existen empleados a modificar...!!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            dni = self.obtenerDni()
            pos = aEmp.buscarEmpleado(dni)
            if pos != -1:
                objEmp = Empleado(self.obtenerDni(), self.obtenerNombres(),
                                  self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(),
                                  self.obtenerDireccion(), self.obtenerTelefono())
                aEmp.modificarEmpleado(objEmp, pos)
                aEmp.grabar()
                self.limpiarControles()
                self.listar()