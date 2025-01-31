class DetalleFactura:

    def __init__(self, nroCom, codProducto, nomProducto, precioVenta, cant, subtotal):
        self.__nroCom = nroCom
        self.__codProducto = codProducto
        self.__nomProducto = nomProducto
        self.__precioVenta = precioVenta
        self.__cant = cant
        self.__subtotal = subtotal

    def getnroCom(self):
        return self.__nroCom

    def getcodProducto(self):  # Método correcto
        return self.__codProducto

    def getnomProducto(self):
        return self.__nomProducto

    def getprecioVenta(self):
        return self.__precioVenta

    def getcant(self):
        return self.__cant

    def getSubtotal(self):
        return self.__subtotal

    def setnroCom(self, nroCom):
        self.__nroCom = nroCom

    def setcodProducto(self, codProducto):
        self.__codProducto = codProducto

    def setnomProducto(self, nomProducto):
        self.__nomProducto = nomProducto

    def setprecioVenta(self, precioVenta):
        self.__precioVenta = precioVenta

    def setcant(self, cant):  # Error tipográfico corregido
        self.__cant = cant