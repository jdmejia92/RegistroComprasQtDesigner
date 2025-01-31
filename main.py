import sys
from PyQt5 import QtWidgets
from Vista.login import Login

if __name__ == '__main__':
    # Crear la aplicación
    app = QtWidgets.QApplication(sys.argv)

    # Crear y mostrar la ventana de login
    window = Login()
    window.show()

    # Ejecutar la aplicación
    sys.exit(app.exec_())