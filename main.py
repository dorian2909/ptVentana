import sys
from builtins import set

from PySide6.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow
from PySide6.QtGui import Qt

from inter.principal import Ui_MainWindow
from inter.Autentificacion import Ui_Form as Autentificacion
from inter.regisCli import Ui_Form as regisCli
from inter.registroCom import Ui_Form as registroCom


class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super(ventanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self.subVentana1 = QMdiSubWindow()
        self.subVentana2 = QMdiSubWindow()
        self.subVentana3 = QMdiSubWindow()

        self.iniMenu()

    def iniMenu(self):
        self.ui.actionAutentificacion.triggered.connect(self.abrirVentana1)
        self.ui.actionregistro_de_clientes.triggered.connect(self.abrirVentana2)
        self.ui.actionregistro_de_la_Comanda.triggered.connect(self.abrirVentana3)

    def abrirVentana1(self):
        self.ventana1 = Autentificacion()

        if self.subVentana1 not in self.mdi.subWindowList():
            self.subVentana1.setWidget(self.ventana1)
            self.subVentana1.setAttribute(Qt.WA_DeleteOnClose, False)
            self.mdi.addSubWindow(self.subVentana1)
            self.ventana1.ButtonCanc.clicked.connect(self.cerrarVentana1)
            self.ventana1.ButtonAcep.clicked.connect(self.validaUSCon)
            self.subVentana1.setFixedSize(self.ventana1.size())
            self.subVentana1.show()

    def abrirVentana2(self):
        self.ventana2 = regisCli()

        if self.subVentana2 not in self.mdi.subWindowList():
            self.subVentana2.setWidget(self.ventana2)
            self.subVentana2.setAttribute(Qt.WA_DeleteOnClose, False)
            self.mdi.addSubWindow(self.subVentana2)
            self.ventana2.btnCan.clicked.connect(self.cerrarVentana2)
            self.subVentana2.setFixedSize(self.ventana2.size())
            self.subVentana2.show()

    def abrirVentana3(self):
        self.ventana3 = registroCom()


        if self.subVentana3 not in self.mdi.subWindowList():
            self.subVentana3.setWidget(self.ventana3)
            self.subVentana3.setAttribute(Qt.WA_DeleteOnClose, False)
            self.mdi.addSubWindow(self.subVentana3)
            self.ventana3.btnSalir.clicked.connect(self.cerrarVentana3)
            self.subVentana3.setFixedSize(self.ventana3.size())
            self.subVentana3.show()

    def cerrarVentana1(self):
        self.ventana1.close()
        self.subVentana1.hide()

    def cerrarVentana2(self):
        self.ventana2.close()
        self.subVentana2.hide()

    def cerrarVentana3(self):
        self.ventana3.close()
        self.subVentana3.hide()

    def validaUSCon(self):
        user= "admin"
        contra= "secreta"
        us = self.ventana1.txtUs.text()
        con = self.ventana1.txtCon.text()
        if con == contra and us == user:
            print("Pasa")
        else:
            print("invalido")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana = ventanaPrincipal()
    ventana.show()

    sys.exit(app.exec())
