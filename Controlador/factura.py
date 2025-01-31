class Factura():

  __nroDoc = ""
  __dniCliente = ""
  __dniEmpleado = ""
  __fecha = ""
  __estado = ""

  def __init__(self, nroDoc, dniCliente, dniEmpleado, fecha, estado):
    self.__nroDoc = nroDoc
    self.__dniCliente = dniCliente
    self.__dniEmpleado = dniEmpleado
    self.__fecha = fecha
    self.__estado = estado

  def getnroDoc(self):
    return self.__nroDoc
  
  def getdniCliente(self):
    return self.__dniCliente
  
  def getdniEmpleado(self):
    return self.__dniEmpleado
  
  def getfecha(self):
    return self.__fecha

  def getEstado(self):
    return self.__estado
  
  def setnroDoc(self, nroDoc):
    self.__nroDoc = nroDoc

  def setdniCliente(self, dniCliente):
    self.__dniCliente = dniCliente

  def setdniEmpleado(self, dniEmpleado):
    self.__dniEmpleado = dniEmpleado

  def setfecha(self, fecha):
    self.__fecha = fecha

  def setEstado(self, estado):
    self.__estado = estado