class Cliente:

  __dniCliente = ""
  __nombreCliente = ""
  __apellidoPaternoCliente = ""
  __apellidoMaternoCliente = ""
  __direccionCliente = ""
  __telefonoCliente = ""

  def __init__(self, dniCliente, nombreCliente, apellidoPaternoCliente, 
              apellidoMaternoCliente, direccionCliente, telefonoCliente):
    self.__dniCliente = dniCliente
    self.__nombreCliente = nombreCliente
    self.__apellidoPaternoCliente = apellidoPaternoCliente
    self.__apellidoMaternoCliente = apellidoMaternoCliente
    self.__direccionCliente = direccionCliente
    self.__telefonoCliente = telefonoCliente

  def getDniCliente(self):
    return self.__dniCliente
  
  def getNombreCliente(self):
    return self.__nombreCliente
  
  def getApellidoPaternoCliente(self):
    return self.__apellidoPaternoCliente
  
  def getApellidoMaternoCliente(self):
    return self.__apellidoMaternoCliente
  
  def getDireccionCliente(self):
    return self.__direccionCliente
  
  def getTelefonoCliente(self):
    return self.__telefonoCliente
  
  def setDniCliente(self, dniCliente):
    self.__dniCliente = dniCliente

  def setNombreCliente(self, nombreCliente):
    self.__nombreCliente = nombreCliente  

  def setApellidoPaternoCliente(self, apellidoPaternoCliente):
    self.__apellidoPaternoCliente = apellidoPaternoCliente

  def setApellidoMaternoCliente(self, apellidoMaternoCliente):
    self.__apellidoMaternoCliente = apellidoMaternoCliente

  def setDireccionCliente(self, direccionCliente):
    self.__direccionCliente = direccionCliente
  
  def setTelefonoCliente(self, telefonoCliente):
    self.__telefonoCliente = telefonoCliente