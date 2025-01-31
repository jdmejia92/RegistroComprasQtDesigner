from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import QStringListModel
from Controlador.arregloClientes import *
from Controlador.arregloEmpleados import * 
from Controlador.arregloProductos import *
from Controlador.factura import * 
from Controlador.arregloFactura import * 
from Controlador.detalleFactura import * 
from Controlador.arregloDetalleFactura import * 
from datetime import date

# Carga de Objetos
aCli = ArregloClientes()
aEmp = ArregloEmpleados()
aPro = ArregloProductos()
acFactura = ArregloFactura()
adFactura = ArregloDetalleFactura()
Detalle = []

class VentanaComprobante(QtWidgets.QMainWindow):
  Fila = -1
  def __init__ (self,parent = None) :
    super(VentanaComprobante, self).__init__(parent) 
    uic.loadUi("UI/ventanaComprobante.ui", self)
    self.show()

    aCli.actualizar()

    self.btnBuscarCli.clicked.connect(self.buscarCli)
    self.btnBuscarEmpleado.clicked.connect(self.buscarEmp)
    self.btnBuscarProd.clicked.connect(self.buscarProd)
    self.btnAgregar.clicked.connect(self.agregar)
    self.btnQuitar.clicked.connect(self.quitar)
    self.btnRegistrar.clicked.connect(self.registrar)
    self.btnLimpiar.clicked.connect(self.Limpiar_Controles_Productos)
    self.btnSalir.clicked.connect(self.salir)
    self.btnConsultar.clicked.connect(self.consultarFactura)

  def buscarCli(self):
    aCli.actualizar()  # Actualizar la lista de clientes
    if aCli.tamannoArregloClientes() == 0:
        QtWidgets.QMessageBox.information(self, "Consultar Cliente", 
                                          "No existen clientes a consultar...!!!", 
                                          QtWidgets.QMessageBox.Ok)
    else:
        dni = self.txtDniCli.text()
        pos = aCli.buscarCliente(dni)
        if pos == -1:
            QtWidgets.QMessageBox.information(self,
                                              "Consultar Cliente",
                                              "El DNI ingresado no existe...!!! ",
                                              QtWidgets.QMessageBox.Ok)
        else:
            self.txtApeNomCli.setText(aCli.devolverClientes(pos).getApellidoPaternoCliente() + " " + 
                                      aCli.devolverClientes(pos).getApellidoMaternoCliente() + ", " + 
                                      aCli.devolverClientes(pos).getNombreCliente())
            self.txtDireccionCli.setText(aCli.devolverClientes(pos).getDireccionCliente())

  def buscarEmp(self):
    if aEmp.tamañoArregloEmpleados() == 0:
        QtWidgets.QMessageBox.information(self, "Consultar Cliente", 
                                        "No existen clientes a consultar...!!!", 
                                        QtWidgets.QMessageBox.Ok)
    else: 
      dni = self.txtDniEmp.text().strip()
      
      self.txtDniEmp.setText(dni)  # Mostrar el DNI ingresado en el campo

      pos = aEmp.buscarEmpleado(dni)
      if pos == -1:
          QtWidgets.QMessageBox.information(self, "Consultar Empleado", 
                                            "El DNI ingresado no existe...!!!",
                                            QtWidgets.QMessageBox.Ok)
      else:
          empleado = aEmp.devolverEmpleados(pos)
          self.txtApeNomEmp.setText(f"{empleado.getApellidoPaternoEmpleado()} "
                                    f"{empleado.getApellidoMaternoEmpleado()}, "
                                    f"{empleado.getNombresEmpleado()}")

        
  def buscarProd(self):
    if aPro.tamañoArregloProductos() == 0:
      QtWidgets.QMessageBox.information(self, "Consultar Producto", 
                                        "No existen productos a consultar...!!!", 
                                        QtWidgets.QMessageBox.Ok)
    else:
      codigo = self.txtCodProd.text()
      pos = aPro.buscarProducto(codigo)
      if pos == -1:
        QtWidgets.QMessageBox.information(self, "Consultar Producto", 
                                          "El Código ingresado no existe...!!! ",
                                          QtWidgets.QMessageBox.Ok)
      else:
        self.txtNomProd.setText(aPro.devolverProducto(pos).getNombre())
        self.txtStockMin.setText(str(aPro.devolverProducto(pos).getStockMinimo()))
        self.txtStockActual.setText(str(aPro.devolverProducto(pos).getStockActual()))
        self.txtPrecioVenta.setText(str(aPro.devolverProducto(pos).getPrecioVenta()))

  def Limpiar_Controles_Productos(self):
    self.txtCodProd.clear(); self.txtNomProd.clear(); self.txtStockMin.clear()
    self.txtStockActual.clear(); self.txtPrecioVenta.clear(); self.txtCodProd.setFocus()

  def agregar(self): # _ --> True=Aceptar False=Cancelar
    # Solicitar cantidad al usuario
    Cantidad, ok = QtWidgets.QInputDialog.getText(self, "Cantidad Solicitada:", "Ingrese Cantidad:")

    if ok == False:
        return QtWidgets.QMessageBox.warning(self, "Entrada inválida", "Debe ingresar una cantidad válida.", QtWidgets.QMessageBox.Ok)
    
    Cantidad = int(Cantidad)
    
    # Verificar que todos los campos estén completos
    if not self.txtNumComprobante.text().strip():
        return QtWidgets.QMessageBox.warning(self, "Campo vacío", "Debe ingresar un número de comprobante.", QtWidgets.QMessageBox.Ok)
    if not self.txtCodProd.text().strip():
        return QtWidgets.QMessageBox.warning(self, "Campo vacío", "Debe ingresar un código de producto.", QtWidgets.QMessageBox.Ok)
    if not self.txtNomProd.text().strip():
        return QtWidgets.QMessageBox.warning(self, "Campo vacío", "Debe ingresar un nombre de producto.", QtWidgets.QMessageBox.Ok)
    if not self.txtPrecioVenta.text().strip() or not self.txtPrecioVenta.text().replace('.', '', 1).isdigit():
        return QtWidgets.QMessageBox.warning(self, "Campo vacío o inválido", "Debe ingresar un precio de venta válido.", QtWidgets.QMessageBox.Ok)
    
    # Convertir precio a float
    PrecioVenta = float(self.txtPrecioVenta.text())
    
    # Agregar los datos
    self.Fila += 1
    Detalle.append([])
    Detalle[self.Fila].append(self.txtNumComprobante.text())  # 0
    Detalle[self.Fila].append(self.txtCodProd.text())         # 1
    Detalle[self.Fila].append(self.txtNomProd.text())         # 2
    Detalle[self.Fila].append(PrecioVenta)                   # 3
    Detalle[self.Fila].append(Cantidad)                      # 4
    Detalle[self.Fila].append(PrecioVenta * Cantidad)        # 5

    # Verificar que haya datos en Detalle
    if not Detalle:
        return QtWidgets.QMessageBox.information(self, "No ingreso datos", "Debe ingresar los datos faltantes para poder agregarlo", QtWidgets.QMessageBox.Ok)
    
    # Limpiar controles e imprimir
    self.Limpiar_Controles_Productos()
    self.Imprimir()

  def registrar(self):
    # Verificar si hay detalles de compra
    if len(Detalle) == 0:
        QtWidgets.QMessageBox.warning(self, "Registro de Venta", 
                                      "No hay productos en la compra \nDebe ingresar productos primero, haciendo click en 'Agregar'.", 
                                      QtWidgets.QMessageBox.Ok)
        return

    # Capturar datos de la cabecera
    num_comprobante = self.txtNumComprobante.text()
    dni_cliente = self.txtDniCli.text()
    dni_empleado = self.txtDniEmp.text()
    fecha = str(date.today())

    # Crear factura y agregarla al arreglo
    factura = Factura(num_comprobante, dni_cliente, dni_empleado, fecha, estado="pagado")
    acFactura.adicionaFactura(factura)
    status = acFactura.grabar()
    if status:
      QtWidgets.QMessageBox.warning(self, "Problemas con Nro Documento", 
                                      status, 
                                      QtWidgets.QMessageBox.Ok)
    else:
      # Registrar los detalles de la factura
      for item in Detalle:
          detalle = DetalleFactura(num_comprobante, item[1], int(item[4]), float(item[3]), int(item[4]), int(item[5]))
          adFactura.adicionaDetalleFactura(detalle)
          statusDetails = adFactura.grabar()
          if statusDetails:
            QtWidgets.QMessageBox.warning(self, "Problemas con Nro Documento", 
                                        statusDetails, 
                                        QtWidgets.QMessageBox.Ok)
          else:
            # Confirmación de registro
            QtWidgets.QMessageBox.information(self, "Registro de Venta", 
                                            "Factura registrada con éxito.", 
                                            QtWidgets.QMessageBox.Ok)

    # Limpiar datos después del registro
    self.Limpiar_Controles_Productos()
    self.txtComprobante.setModel(None)
    Detalle.clear()
    self.Fila = -1

  def quitar(self):
    Item, ok = QtWidgets.QInputDialog.getText(self, "Fila", "Ingrese Nro Documento a Eliminar")
    
    if not ok or not Item.strip().isdigit():
        return QtWidgets.QMessageBox.warning(self, "Entrada inválida", "Debe ingresar un número de documento válido.", QtWidgets.QMessageBox.Ok)
    
    nro_documento = Item.strip()
    
    # Buscar y eliminar la factura
    indice_factura = acFactura.buscarFactura(nro_documento)
    if indice_factura == -1:
        return QtWidgets.QMessageBox.warning(self, "Error", "El número de documento no existe en facturas.", QtWidgets.QMessageBox.Ok)
    
    # Eliminar la factura del arreglo
    acFactura.eliminarFactura(indice_factura)
    
    # Buscar y eliminar los detalles asociados a la factura
    indice_detalle = adFactura.buscarDetalleFactura(nro_documento)
    while indice_detalle != -1:
        adFactura.eliminarDetalleFactura(nro_documento)
        indice_detalle = adFactura.buscarDetalleFactura(nro_documento)
    
    # Actualizar los archivos
    acFactura.grabar()  # Actualizar facturas.txt
    adFactura.grabar()  # Actualizar detalle_facturas.txt
    
    # Actualizar la vista
    self.Fila -= 1
    self.Imprimir()
    QtWidgets.QMessageBox.information(self, "Éxito", "Factura eliminada correctamente.", QtWidgets.QMessageBox.Ok)

  def consultarFactura(self):
    # Obtener el número de comprobante ingresado
    num_comprobante = self.txtNumComprobante.text().strip()
    adFactura.cargar()
    acFactura.cargar()
    
    if num_comprobante == 0 or num_comprobante == "":
      QtWidgets.QMessageBox.information(self, "Consultar Codigo Factura", 
                                      "Debes agregar un numero de documento...!!!", 
                                      QtWidgets.QMessageBox.Ok)
    else:
      # Buscar la factura en el arreglo
      pos = acFactura.buscarFactura(num_comprobante)

      if pos == -1:
          QtWidgets.QMessageBox.information(self, "Consultar Factura",
                                            "El número de comprobante no existe.",
                                            QtWidgets.QMessageBox.Ok)
      else:
          factura_detalles = adFactura.buscarDetalleFactura(num_comprobante)
          factura = acFactura.devolverFactura(pos)
          # Mostrar los detalles de la factura en los campos correspondientes
          self.txtDniCli.setText(factura.getdniCliente())
          self.txtDniEmp.setText(factura.getdniEmpleado())
          self.txtApeNomCli.setText(aCli.devolverClientes(aCli.buscarCliente(factura.getdniCliente())).getApellidoPaternoCliente() + " " +
                                    aCli.devolverClientes(aCli.buscarCliente(factura.getdniCliente())).getApellidoMaternoCliente())
          self.txtApeNomEmp.setText(aEmp.devolverEmpleados(aEmp.buscarEmpleado(factura.getdniEmpleado())).getApellidoPaternoEmpleado() + " " +
                                    aEmp.devolverEmpleados(aEmp.buscarEmpleado(factura.getdniEmpleado())).getApellidoMaternoEmpleado())
          self.txtDireccionCli.setText(aCli.devolverClientes(aCli.buscarCliente(factura.getdniCliente())).getDireccionCliente())

          # Mostrar los detalles de la factura en el QListView
          self.mostrarDetallesFactura(num_comprobante)

  def mostrarDetallesFactura(self, num_comprobante):
    # Crear un nuevo modelo vacío
    model = QStringListModel()
    
    # Verificar si la factura ya está en los datos actuales
    if self.txtComprobante.model():
        data_actual = self.txtComprobante.model().stringList()
        if any(f"Factura: {num_comprobante}" in linea for linea in data_actual):
            return  # Evita duplicados

    data = []

    # Agregar cabecera de factura
    data.append("*******************************************************************")
    data.append(f"Factura: {num_comprobante}")
    data.append("*******************************************************************")

    # Buscar y agregar los detalles de la factura
    for detalle in adFactura.dataDetalleFactura:
        if detalle.getnroCom() == num_comprobante:
            data.append(f"Producto: {detalle.getnomProducto()}")
            data.append(f"Precio: {detalle.getprecioVenta()} | Subtotal: {detalle.getSubtotal()}")

    # Mostrar el total de la factura
    total = sum(detalle.getSubtotal() for detalle in adFactura.dataDetalleFactura if detalle.getnroCom() == int(num_comprobante))
    data.append("*******************************************************************")
    data.append(f"Total: {total}")

    # Cargar los datos en el modelo
    model.setStringList(data)
    self.txtComprobante.setModel(model)  # Se reemplaza el modelo con uno nuevo limpio


  def Imprimir(self):
    model = QStringListModel()
    data = []  # Lista para almacenar el contenido

    # Cabecera del Comprobante
    data.append("*******************************************************************")
    data.append("Comprobante de Pago")
    data.append("*************************************************************")
    data.append(f"Comprobante:\t\t{self.txtNumComprobante.text()}")
    data.append(f"Cliente\t:\t\t{self.txtApeNomCli.text()}")
    data.append(f"Dirección\t:\t\t{self.txtDireccionCli.text()}")
    data.append(f"Empleado\t:\t\t{self.txtApeNomEmp.text()}")
    data.append(f"Fecha\t:\t\t{str(date.today())}")
    data.append("*****************************************************************")
    
    # Detalle del Comprobante
    data.append("Item\tCant x Descripción\tImportes")
    data.append("***********************************************************************")
    
    Acumulador = 0
    for i in range(len(Detalle)):
        data.append(f"{i+1}\t{Detalle[i][4]} x {Detalle[i][2]}")
        data.append(f"\tPrecio: {Detalle[i][3]}\t\t{str(Detalle[i][5])}")
        Acumulador += Detalle[i][5]
    
    data.append("***************************************************************")
    data.append(f"Total\t\t: {str(Acumulador)}")
    Igv = Acumulador * 0.18
    Tg = Acumulador + Igv
    data.append(f"Igv(18%) \t\t: {str(Igv)}")
    data.append(f"Total Venta\t\t: {str(Tg)}")

    # Cargar los datos en el modelo y asignarlo al QListView
    model.setStringList(data)
    self.txtComprobante.setModel(model)

  def salir(self):
    Fila = -1
    Detalle.clear()
    self.close()