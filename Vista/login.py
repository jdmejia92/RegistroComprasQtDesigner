from PyQt5 import QtWidgets, uic, QtGui
from Vista.ventanaPrincipal import VentanaPrincipal
import os

# Ruta del archivo de usuarios
ARCHIVO_USUARIOS = "Modelo/usuarios.txt"

def crear_archivo_usuarios():
    """Crea el archivo de usuarios con el usuario admin por defecto si no existe."""
    if not os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
            archivo.write("admin,admin\n")
        print(f"Archivo {ARCHIVO_USUARIOS} creado con el usuario 'admin' y contraseña 'admin'.")

def cargar_usuarios():
    """Carga los usuarios y contraseñas desde el archivo."""
    usuarios = {}
    with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            usuario, clave = linea.strip().split(",")
            usuarios[usuario] = clave
    return usuarios

def autenticar_usuario(usuario, clave):
    """Autentica al usuario."""
    usuarios = cargar_usuarios()
    if usuario in usuarios and usuarios[usuario] == clave:
        return True
    return False

class Login(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        uic.loadUi("Ui/login.ui", self)
        self.show()
        self.setWindowTitle("Ventana Principal")
        self.setWindowIcon(QtGui.QIcon("static/img/icono.png"))

        # Crear el archivo de usuarios si no existe
        crear_archivo_usuarios()

        # Eventos
        self.btnIniciar.clicked.connect(self.iniciarSesion)

    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtPassword.text()

        if autenticar_usuario(usuario, contraseña):
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("Los datos ingresados son incorrectos....!!!")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)
            mensaje.exec_()