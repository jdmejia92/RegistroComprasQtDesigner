from Controlador.factura import *
import os

class ArregloFactura:

    def __init__(self):
        self.dataFactura = []  # Lista para almacenar objetos de tipo Factura
        self.contNumFact = 0   # Contador de facturas

    def adicionaFactura(self, factura):
        # Añade una factura a la lista y aumenta el contador
        self.dataFactura.append(factura)
        self.contNumFact += 1

    def devolverFactura(self, pos):
        # Devuelve la factura en la posición indicada
        if 0 <= pos < len(self.dataFactura):
            return self.dataFactura[pos]
        return None

    def tamañoFactura(self):
        # Devuelve el número de facturas en la lista
        return len(self.dataFactura)

    def buscarFactura(self, nroDoc):
        # Busca una factura por su número de documento
        for i in range(self.tamañoFactura()):
            if nroDoc == self.dataFactura[i].getnroDoc():
                return i
        return -1

    def eliminarFactura(self, indice):
        # Elimina una factura en la posición indicada
        if 0 <= indice < self.tamañoFactura():
            del self.dataFactura[indice]
            self.contNumFact -= 1

    def nroSerie(self):
        # Devuelve una lista con los números de documento de las facturas
        self.series = []
        for i in range(self.tamañoFactura()):
            self.series.append(self.dataFactura[i].getnroDoc())
        return len(self.series)

    def grabar(self):
        filename = "Modelo/facturas.txt"

        if not os.path.exists("Modelo"):
            os.makedirs("Modelo")  # Crea el directorio si no existe

        # Escribir los datos actualizados en el archivo
        with open(filename, "w", encoding="utf-8") as file:
            for factura in self.dataFactura:
                file.write(
                    f"{factura.getnroDoc()}, {factura.getdniCliente()}, "
                    f"{factura.getdniEmpleado()}, {factura.getfecha()}, {factura.getEstado()}\n"
                )

        print("Facturas actualizadas correctamente.")

    def cargar(self):
        archivo_path = "Modelo/facturas.txt"

        # Crear el archivo si no existe
        if not os.path.exists(archivo_path):
            with open(archivo_path, "w", encoding="utf-8"):
                pass
            print("Archivo facturas.txt creado automáticamente.")

        try:
            self.dataFactura.clear()  # Limpiar la lista antes de cargar
            self.contNumFact = 0      # Reiniciar el contador
            with open(archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo.readlines():
                    columna = linea.strip().split(", ")  # Separar los datos por comas
                    if len(columna) >= 5:
                        nroDoc = columna[0].strip()
                        dniCliente = columna[1].strip()
                        dniEmpleado = columna[2].strip()
                        fecha = columna[3].strip()
                        estado = columna[4].strip()
                        # Crear un objeto Factura con los datos cargados
                        factura = Factura(nroDoc, dniCliente, dniEmpleado, fecha, estado)
                        self.adicionaFactura(factura)
            print("Facturas cargadas correctamente.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")