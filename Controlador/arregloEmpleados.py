from Controlador.empleados import *
import os

class ArregloEmpleados:

  def __init__(self):
    self.dataEmpleados = []
    self.cargar()

  def adicionalEmpleado(self, objEmp):
    self.dataEmpleados.append(objEmp)

  def devolverEmpleados(self, pos):
    return self.dataEmpleados[pos]
  
  def tamañoArregloEmpleados(self):
    return len(self.dataEmpleados)
  
  def buscarEmpleado(self, dni):
    for i in range(self.tamañoArregloEmpleados()):
      if dni == self.dataEmpleados[i].getDniEmpleado():
        return i
    return -1
  
  def eliminarEmpleado(self, indice):
    del(self.dataEmpleados[indice])

  def modificarEmpleado(self, objEmp, pos):
    self.dataEmpleados[pos] = objEmp

  def retornarDatos(self):
    return self.dataEmpleados
  
  def cargar(self):
    archivo_path = "Modelo/empleados.txt"
    if not os.path.exists(archivo_path):
      # Si no existe, creamos el archivo vacío
      with open(archivo_path, "w", encoding="utf-8"):
          pass
      print("Archivo proveedor.txt creado automáticamente.")
    archivo = open("Modelo/empleados.txt", "r", encoding="utf-8")
    for linea in archivo.readlines():
      columna = str(linea).split(",")
      dni = columna[0]
      nombres = columna[1]
      apellidoPaterno = columna[2]
      apellidoMaterno = columna[3]
      direccion = columna[4]
      telefono = columna[5].strip()
      objEmp = Empleado(dni, nombres, apellidoPaterno, apellidoMaterno, 
                      direccion, telefono)
      self.adicionalEmpleado(objEmp)
    archivo.close()

  def grabar(self):
    archivo = open("Modelo/empleados.txt", "w", encoding="utf-8")
    for i in range(self.tamañoArregloEmpleados()):
      archivo.write(str(self.devolverEmpleados(i).getDniEmpleado()) + "," 
                    + str(self.devolverEmpleados(i).getNombresEmpleado()) + "," 
                    + str(self.devolverEmpleados(i).getApellidoPaternoEmpleado()) + "," 
                    + str(self.devolverEmpleados(i).getApellidoMaternoEmpleado()) + "," 
                    + str(self.devolverEmpleados(i).getDireccionEmpleado()) + "," 
                    + str(self.devolverEmpleados(i).getTelefonoEmpleado()) + "\n")
    archivo.close()