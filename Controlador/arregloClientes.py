from Controlador.clientes import *
import os

class ArregloClientes:

  def __init__(self):
      self.dataClientes = []
      self.cargar()

  def adicionaCliente(self, objCli):
    self.dataClientes.append(objCli)

  def devolverClientes(self, pos):
    return self.dataClientes[pos]
  
  def tamannoArregloClientes(self):
    return len(self.dataClientes)
  
  def buscarCliente(self, dni):
    for i in range(self.tamannoArregloClientes()):
      if dni == self.dataClientes[i].getDniCliente():
        return i
    return -1
  
  def eliminarCliente(self, indice):
    del(self.dataClientes[indice])

  def modificarCliente(self, objCli, pos):
    self.dataClientes[pos] = objCli

  def retornarDatos(self):
    return self.dataClientes
  
  def cargar(self):
    archivo_path = "Modelo/clientes.txt"
    if not os.path.exists(archivo_path):
      # Si no existe, creamos el archivo vacío
      with open(archivo_path, "w", encoding="utf-8"):
          pass
      print("Archivo cliente.txt creado automáticamente.")
    archivo = open("Modelo/clientes.txt", "r", encoding="utf-8")
    for linea in archivo.readlines():
      columna = str(linea).split(",")
      dni = columna[0]
      nombres = columna[1]
      apellidoPaterno = columna[2]
      apellidoMaterno = columna[3]
      direccion = columna[4]
      telefono = columna[5].strip()
      objCli = Cliente(dni, nombres, apellidoPaterno, apellidoMaterno, 
                      direccion, telefono)
      self.adicionaCliente(objCli)
    archivo.close()

  def grabar(self):
    archivo = open("Modelo/clientes.txt", "w", encoding="utf-8")
    for i in range(self.tamannoArregloClientes()):
      archivo.write(str(self.devolverClientes(i).getDniCliente()) + "," 
                    + str(self.devolverClientes(i).getNombreCliente()) + "," 
                    + str(self.devolverClientes(i).getApellidoPaternoCliente()) + "," 
                    + str(self.devolverClientes(i).getApellidoMaternoCliente()) + "," 
                    + str(self.devolverClientes(i).getDireccionCliente()) + "," 
                    + str(self.devolverClientes(i).getTelefonoCliente()) + "\n")
    archivo.close()

  def actualizar(self):
    """Recarga los clientes desde el archivo."""
    self.dataClientes.clear()  # Limpiar la lista actual
    self.cargar()  # Volver a cargar los datos desde el archivo