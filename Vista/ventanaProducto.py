from PyQt5 import QtWidgets, uic
from Controlador.arregloProductos import *
from Controlador.arregloProovedor import *

aProd = ArregloProductos()
aProv = ArregloProveedor()

class VentanaProductos(QtWidgets.QMainWindow):
    Fila = -1

    def __init__(self, parent=None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("Ui/ventanaProductos.ui", self)
        self.show()
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.tblProductos.clicked.connect(self.Seleccionar)

        self.cboProveedor.addItems(aProv.listarProveedores())

    def obtenerCodigo(self):
        return self.txtCodigo.text()

    def obtenerNombre(self):
        return self.txtNombre.text()

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()

    def obtenerStockMinimo(self):
        return self.txtStockMinimo.value()

    def obtenerStockActual(self):
        return self.txtStockActual.value()

    def obtenerPrecioCosto(self):
        return self.txtPrecioCosto.value()

    def obtenerPrecioVenta(self):
        return self.txtPrecioVenta.value()

    def obtenerProveedor(self):
        return self.cboProveedor.currentText()

    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(6)

    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Código del producto...!!!"
        elif self.txtNombre.text() == "":
            self.txtNombre.setFocus()
            return "Nombre del producto...!!!"
        elif self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripción del producto...!!!"
        elif self.txtStockMinimo.value() == 0:
            self.txtStockMinimo.setFocus()
            return "Stock mínimo del producto...!!!"
        elif self.txtStockActual.value() == 0:
            self.txtStockActual.setFocus()
            return "Stock actual del producto...!!!"
        elif self.txtPrecioCosto.value() == 0:
            self.txtPrecioCosto.setFocus()
            return "Precio de costo del producto...!!!"
        elif self.txtPrecioVenta.value() == 0:
            self.txtPrecioVenta.setFocus()
            return "Precio de venta del producto...!!!"
        elif self.cboProveedor.currentText() == "Seleccionar Proveedor":
            self.cboProveedor.setFocus()
            return "Proveedor del producto...!!!"
        elif self.cboAlmacen.currentText() == "Seleccionar Almacen":
            self.cboAlmacen.setFocus()
            return "Almacén del producto...!!!"
        else:
            return ""

    def listar(self):
        self.tblProductos.setRowCount(aProd.tamañoArregloProductos())
        self.tblProductos.setColumnCount(9)
        for i in range(0, aProd.tamañoArregloProductos()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aProd.devolverProducto(i).getCodigo()))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aProd.devolverProducto(i).getNombre()))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aProd.devolverProducto(i).getDescripcion()))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(str(aProd.devolverProducto(i).getStockMinimo())))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(str(aProd.devolverProducto(i).getStockActual())))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(str(aProd.devolverProducto(i).getPrecioCosto())))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(str(aProd.devolverProducto(i).getPrecioVenta())))
            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(aProd.devolverProducto(i).getProveedor()))
            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(aProd.devolverProducto(i).getAlmacen()))

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()

    def registrar(self):
        if self.valida() == "":
            objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(),
                              self.obtenerStockMinimo(), self.obtenerStockActual(), self.obtenerPrecioCosto(),
                              self.obtenerPrecioVenta(), self.obtenerProveedor(), self.obtenerAlmacen())
            codigo = self.obtenerCodigo()
            if aProd.buscarProducto(codigo) == -1:
                aProd.adicionaProducto(objPro)
                aProd.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto", 
                                                  "El código ingresado ya existe...!!!", 
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", 
                                              "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        if aProd.tamañoArregloProductos() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                              "No existen productos a consultar...!!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto", "Ingrese el código a consultar")
            pos = aProd.buscarProducto(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                  "El código ingresado no existe...!!!", 
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtCodigo.setText(aProd.devolverProducto(pos).getCodigo())
                self.txtNombre.setText(aProd.devolverProducto(pos).getNombre())
                self.txtDescripcion.setText(aProd.devolverProducto(pos).getDescripcion())
                self.txtStockMinimo.setValue(aProd.devolverProducto(pos).getStockMinimo())
                self.txtStockActual.setValue(aProd.devolverProducto(pos).getStockActual())
                self.txtPrecioCosto.setValue(aProd.devolverProducto(pos).getPrecioCosto())
                self.txtPrecioVenta.setValue(aProd.devolverProducto(pos).getPrecioVenta())
                self.cboProveedor.setCurrentText(aProd.devolverProducto(pos).getProveedor())
                self.cboAlmacen.setCurrentText(aProd.devolverProducto(pos).getAlmacen())

    def eliminar(self):
        codigo = self.txtCodigo.text()
        pos = aProd.buscarProducto(codigo)
        if pos != -1:
            aProd.eliminarProducto(pos)
            aProd.grabar()
            self.limpiarControles()
            self.listar()

    def Seleccionar(self):
        self.Fila = self.tblProductos.currentRow()

    def quitar(self):
        if aProd.tamañoArregloProductos() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                              "No existen productos a eliminar...!!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblProductos.selectedItems()
            if self.Fila != -1:
                indiceFila = fila[0].row()
                codigo = self.tblProductos.item(self.Fila, 0).text()
                pos = aProd.buscarProducto(codigo)
                aProd.eliminarProducto(pos)
                aProd.grabar()
                self.limpiarTabla()
                self.listar()
                self.Fila = -1
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                  "Debe seleccionar una fila...!!!",
                                                  QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aProd.tamañoArregloProductos() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                              "No existen productos a modificar...!!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            codigo = self.obtenerCodigo()
            pos = aProd.buscarProducto(codigo)
            if pos != -1:
                objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(),
                                  self.obtenerStockMinimo(), self.obtenerStockActual(), self.obtenerPrecioCosto(),
                                  self.obtenerPrecioVenta(), self.obtenerProveedor(), self.obtenerAlmacen())
                aProd.modificarProducto(objPro, pos)
                aProd.grabar()
                self.limpiarControles()
                self.listar()
