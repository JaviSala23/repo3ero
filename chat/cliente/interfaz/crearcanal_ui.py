# Form implementation generated from reading ui file '/home/javi/Escritorio/escuela/practicaRepo/repo3ero/chat/cliente/interfaz/crearcanal.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CrearCanal(object):
    def setupUi(self, CrearCanal):
        CrearCanal.setObjectName("CrearCanal")
        CrearCanal.resize(542, 183)
        self.formLayoutWidget = QtWidgets.QWidget(parent=CrearCanal)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 19, 511, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.nombre = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.nombre.setObjectName("nombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nombre)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.descripcion = QtWidgets.QTextEdit(parent=self.formLayoutWidget)
        self.descripcion.setObjectName("descripcion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.descripcion)
        self.crear = QtWidgets.QPushButton(parent=CrearCanal)
        self.crear.setGeometry(QtCore.QRect(210, 150, 80, 23))
        self.crear.setObjectName("crear")
        self.cancelar = QtWidgets.QPushButton(parent=CrearCanal)
        self.cancelar.setGeometry(QtCore.QRect(310, 150, 80, 23))
        self.cancelar.setObjectName("cancelar")

        self.retranslateUi(CrearCanal)
        QtCore.QMetaObject.connectSlotsByName(CrearCanal)

    def retranslateUi(self, CrearCanal):
        _translate = QtCore.QCoreApplication.translate
        CrearCanal.setWindowTitle(_translate("CrearCanal", "Crear Canal"))
        self.label.setText(_translate("CrearCanal", "Nombre del Canal:"))
        self.label_2.setText(_translate("CrearCanal", "Descripcion del Canal:"))
        self.crear.setText(_translate("CrearCanal", "Crear"))
        self.cancelar.setText(_translate("CrearCanal", "Cancelar"))