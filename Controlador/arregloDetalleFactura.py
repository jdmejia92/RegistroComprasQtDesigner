from Controlador.detalleFactura import DetalleFactura
import os

class ArregloDetalleFactura:

    def __init__(self):
        self.dataDetalleFactura = []
        self.contNumFact = 0

    def adicionaDetalleFactura(self, objDetFact):
        self.dataDetalleFactura.append(objDetFact)
        self.contNumFact += 1  # Incrementar el contador

    def devolverDetalleFactura(self, pos):
        if 0 <= pos < len(self.dataDetalleFactura):
            return self.dataDetalleFactura[pos]
        return None

    def tamañoDetalleFactura(self):
        return len(self.dataDetalleFactura)

    def buscarDetalleFactura(self, nDocumentoVenta):
        for i, detalle in enumerate(self.dataDetalleFactura):
            if nDocumentoVenta == detalle.getnroCom():
                return i
        return -1

    def eliminarDetalleFactura(self, nro_documento):
        # Filtrar las facturas para eliminar la que tiene el nro_documento
        self.dataDetalleFactura = [
            detalle for detalle in self.dataDetalleFactura if detalle.getnroCom() != nro_documento
        ]
        self.contNumFact = len(self.dataDetalleFactura)  # Actualizar el contador

    def grabar(self):
        filename = "Modelo/detalle_facturas.txt"

        if not os.path.exists("Modelo"):
            os.makedirs("Modelo")  # Crea el directorio si no existe

        # Escribir los datos actualizados en el archivo
        with open(filename, "w", encoding="utf-8") as file:
            for detalle in self.dataDetalleFactura:
                file.write(
                    f"{detalle.getnroCom()}, {detalle.getcodProducto()}, {detalle.getnomProducto()}, "
                    f"{detalle.getprecioVenta()}, {detalle.getcant()}, {detalle.getSubtotal()}\n"
                )

    print("Detalles de facturas actualizados correctamente.")

    def cargar(self):
        archivo_path = "Modelo/detalle_facturas.txt"
        if not os.path.exists(archivo_path):
            with open(archivo_path, "w", encoding="utf-8"):
                pass
            print("Archivo detalle_facturas.txt creado automáticamente.")

        try:
            self.dataDetalleFactura.clear()  # Limpiar la lista antes de cargar
            self.contNumFact = 0  # Reiniciar el contador
            with open(archivo_path, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    columna = linea.strip().split(", ")  # Separación por comas
                    if len(columna) == 6:  # Verificar que la línea tenga 6 columnas
                        nroCom = columna[0].strip()
                        codPro = columna[1].strip()
                        nomProducto = columna[2].strip()
                        precioVenta = float(columna[3].strip())
                        cant = int(columna[4].strip())
                        subtotal = float(columna[5].strip())
                        objDetFact = DetalleFactura(nroCom, codPro, nomProducto, precioVenta, cant, subtotal)
                        self.adicionaDetalleFactura(objDetFact)
            print("Detalles de facturas cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")