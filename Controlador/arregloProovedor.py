from Controlador.proveedor import *
import os

class ArregloProveedor:

  def __init__(self):
    self.dataProveedor = []
    self.cargar()

  def listarProveedores(self):
      lista_proveedores = []
      for proveedor in self.dataProveedor:
          lista_proveedores.append(proveedor.getRazSoc())
      return lista_proveedores

  def adicionaProveedor(self, objPro):
    self.dataProveedor.append(objPro)

  def devolverProveedor(self, pos):
    return self.dataProveedor[pos]
  
  def tamañoArregloProveedor(self):
    return len(self.dataProveedor)
  
  def buscarProveedor(self, ruc):
    for i in range(self.tamañoArregloProveedor()):
      if ruc == self.dataProveedor[i].getDNIProveedor():
        return i
    return -1
  
  def eliminarProveedor(self, indice):
    del(self.dataProveedor[indice])

  def modificarProveedor(self, objPro, pos):
    self.dataProveedor[pos] = objPro

  def retornarDatos(self):
    return self.dataProveedor
  
  def cargar(self):
    archivo_path = "Modelo/proveedor.txt"
    if not os.path.exists(archivo_path):
      # Si no existe, creamos el archivo vacío
      with open(archivo_path, "w", encoding="utf-8"):
          pass
      print("Archivo proveedor.txt creado automáticamente.")
    archivo = open("Modelo/proveedor.txt", "r", encoding="utf-8")
    for linea in archivo.readlines():
      columna = str(linea).split(",")
      dni = columna[0]
      raz = columna[1]
      tel = columna[2]
      dir = columna[3]
      cat = columna[4].strip()
      objPro = Proveedores(dni, raz, tel, dir, cat)
      self.adicionaProveedor(objPro)
    archivo.close()

  def grabar(self):
    archivo = open("Modelo/proveedor.txt", "w", encoding="utf-8")
    for i in range(self.tamañoArregloProveedor()):
      archivo.write(str(self.devolverProveedor(i).getDNIProveedor()) + "," 
      + str(self.devolverProveedor(i).getRazSoc()) + "," 
      + str(self.devolverProveedor(i).getTelefono()) + "," 
      + str(self.devolverProveedor(i).getDireccion()) + "," 
      + str(self.devolverProveedor(i).getCategoria()) + "\n")
    archivo.close()