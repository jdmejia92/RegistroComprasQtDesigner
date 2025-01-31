from PyQt5 import QtWidgets, uic, QtGui
from Vista.ventanaPrincipal import VentanaPrincipal

class Login(QtWidgets.QMainWindow):
  def __init__(self, parent = None):
    super(Login, self).__init__(parent)
    uic.loadUi("Ui/login.ui", self)
    self.show()
    self.setWindowTitle("Ventana Principal")
    self.setWindowIcon(QtGui.QIcon("static/img/icono.png"))

    # Eventos
    self.btnIniciar.clicked.connect(self.iniciarSesion)

  # Nuevas funciones
  def iniciarSesion(self):
      usuario = self.txtUsuario.text().lower()
      contraseña = self.txtPassword.text()
      """ if usuario == "scott" and contraseña == "123456": """
      self.close()
      vprincipal = VentanaPrincipal(self)
      vprincipal.show()
      """ else:
          mensaje = QtWidgets.QMessageBox()
          mensaje.setWindowTitle("Punto de Venta")
          mensaje.setText("Los datos ingresados son incorrectos....!!!")
          mensaje.setIcon(QtWidgets.QMessageBox.Information)
          mensaje.exec_()  """