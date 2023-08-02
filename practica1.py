from interfaz.practica1Intefaz import InterfazGrafica
from PyQt5 import QtWidgets

#creamos aplicacion QtWidegets
aplicacion=QtWidgets.QApplication([]) 
interfaz1=InterfazGrafica()

interfaz1.mostrarFormulario()

aplicacion.exec()