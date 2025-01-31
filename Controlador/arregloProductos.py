from Controlador.productos import *
import os

class ArregloProductos:

  def __init__(self):
    self.dataProductos = []
    self.cargar()

  def adicionaProducto(self, objPro):
    self.dataProductos.append(objPro)

  def devolverProducto(self, pos):
    return self.dataProductos[pos]
  
  def tamañoArregloProductos(self):
    return len(self.dataProductos)
  
  def buscarProducto(self, codigo):
    for i in range(self.tamañoArregloProductos()):
      if codigo == self.dataProductos[i].getCodigo():
        return i
    return -1
  
  def eliminarProducto(self, indice):
    del(self.dataProductos[indice])

  def modificarProducto(self, objPro, pos):
    self.dataProductos[pos] = objPro

  def retornarDatos(self):
    return self.dataProductos
  
  def cargar(self):
    archivo_path = "Modelo/productos.txt"
    if not os.path.exists(archivo_path):
      # Si no existe, creamos el archivo vacío
      with open(archivo_path, "w", encoding="utf-8"):
          pass
      print("Archivo proveedor.txt creado automáticamente.")
    archivo = open("Modelo/productos.txt", "r", encoding="utf-8")
    for linea in archivo.readlines():
      columna = str(linea).split(",")
      codigo = columna[0]
      nombre = columna[1]
      descripcion = columna[2]
      stockMinimo = int(columna[3])
      stockActual = int(columna[4])
      precioCosto = float(columna[5])
      precioVenta = float(columna[6])
      proveedor = columna[7]
      almacen = columna[8].strip()
      objPro = Producto(codigo, nombre, descripcion, stockMinimo, stockActual, 
                      precioCosto, precioVenta, proveedor, almacen)
      self.adicionaProducto(objPro)
    archivo.close()

  def grabar(self):
    archivo = open("Modelo/productos.txt", "w", encoding="utf-8")
    for i in range(self.tamañoArregloProductos()):
      archivo.write(str(self.devolverProducto(i).getCodigo()) + "," 
      + str(self.devolverProducto(i).getNombre()) + "," 
      + str(self.devolverProducto(i).getDescripcion()) + "," 
      + str(self.devolverProducto(i).getStockMinimo()) + "," 
      + str(self.devolverProducto(i).getStockActual()) + "," 
      + str(self.devolverProducto(i).getPrecioCosto()) + "," 
      + str(self.devolverProducto(i).getPrecioVenta()) + "," 
      + str(self.devolverProducto(i).getProveedor()) + "," 
      + str(self.devolverProducto(i).getAlmacen()) + "\n")
    archivo.close()