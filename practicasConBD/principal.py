#de la libreria PyQt5 importamos estos dos elem
from PyQt5 import uic,QtWidgets
from PyQt5.QtCore import QDate
from clases.cliente import Cliente

#from clases.cliente import Cliente




#clase que maneja la interfaz grafica
class InterfazGrafica: 
    #funcion constructora.
    def __init__(self):
        #atributo es el formulario generado en qt designer
        self.formulario=uic.loadUi('practicasConBD/interfaz/clientes.ui') 
        self.sentencia=0
        
        
    def habilitarCajas(self):
        self.formulario.nombre.setReadOnly(False)
        self.formulario.contrena.setReadOnly(False)
        self.formulario.email.setReadOnly(False)
        self.formulario.telefono.setReadOnly(False)
        self.formulario.calle.setReadOnly(False)
        self.formulario.numero.setReadOnly(False)
        self.formulario.localidad.setReadOnly(False)
        self.formulario.provincia.setReadOnly(False)
        self.formulario.pais.setReadOnly(False)
        self.formulario.dni.setReadOnly(False)

        self.formulario.aceptar.show()
        self.formulario.cancelar.show()
        self.formulario.nuevo.hide()
        self.formulario.editar.hide()
        self.formulario.eliminar.hide()
        self.formulario.primero.hide()
        self.formulario.anterior.hide()
        self.formulario.posterior.hide()
        self.formulario.ultimo.hide()
    
    def nuevoCliente(self):
        self.formulario.nombre.setText("")
        self.formulario.contrena.setText("")
        self.formulario.email.setText("")
        self.formulario.telefono.setText("")
        self.formulario.calle.setText("")
        self.formulario.numero.setText("")
        self.formulario.localidad.setText("")
        self.formulario.provincia.setText("")
        self.formulario.pais.setText("")
        self.formulario.dni.setText("")
        cliente1=Cliente()
        registro=cliente1.consultarUltimoCliente()
        if registro:
            del cliente1
            self.formulario.id.setText(str(int(registro[0])+1))
            
        else:
            self.formulario.id.setText("1")
        self.accion=0
        self.habilitarCajas()
            
        
    def ultimoCliente(self):
        cliente1=Cliente()
        registro=cliente1.consultarUltimoCliente()
        del cliente1
        if registro:
            self.rellenarClientes(registro)
        
    def primerCliente(self):
        cliente1=Cliente()
        registro=cliente1.consultarPrimerCliente()
        del cliente1
        if registro:
            self.rellenarClientes(registro)
        
    def anterior(self):
        cliente1=Cliente()
        cliente1.id=int(self.formulario.id.text())-1
        registro=cliente1.consultarUnCliente()
        del cliente1
        if registro:
            self.rellenarClientes(registro)
    
    def posterior(self):
        cliente1=Cliente()
        cliente1.id=int(self.formulario.id.text())+1
        registro=cliente1.consultarUnCliente()
        del cliente1
        if registro:
            self.rellenarClientes(registro)
        
        
        
        
    def rellenarClientes(self,registro):
        self.formulario.id.setText(str(registro[0]))
        self.formulario.nombre.setText(registro[1])
        self.formulario.contrena.setText(registro[2])
        self.formulario.email.setText(registro[3])
        self.formulario.telefono.setText(registro[4])
        self.formulario.calle.setText(registro[5])
        self.formulario.numero.setText(str(registro[6]))
        self.formulario.localidad.setText(registro[7])
        self.formulario.provincia.setText(registro[8])
        self.formulario.pais.setText(registro[9])
        self.formulario.dni.setText(str(registro[10]))
      
         
        
    def aceptar(self):
        cliente1=Cliente()# genero mi objeto cliente
        cliente1.id=self.formulario.id.text() 
        cliente1.nombre=self.formulario.nombre.text() 
        cliente1.contrasena=self.formulario.contrena.text() 
        cliente1.email=self.formulario.email.text() 
        cliente1.telefono=self.formulario.telefono.text() 
        cliente1.calle=self.formulario.calle.text() 
        cliente1.numero=int(self.formulario.numero.text())
        cliente1.localidad=self.formulario.localidad.text() 
        cliente1.provincia=self.formulario.provincia.text() 
        cliente1.pais=self.formulario.pais.text() 
        cliente1.dni=int(self.formulario.dni.text())
       
        if self.accion==0:
            cliente1.nuevoCliente()
            self.cancelar()
            cliente1.nuevoCliente()
        if self.accion==1:
            cliente1.eliminarCliente()
        else:
            cliente1.actualizarCliente()
        
    
    def cancelar(self):
        self.formulario.nombre.setReadOnly(True)
        self.formulario.contrena.setReadOnly(True)
        self.formulario.email.setReadOnly(True)
        self.formulario.telefono.setReadOnly(True)
        self.formulario.calle.setReadOnly(True)
        self.formulario.numero.setReadOnly(True)
        self.formulario.localidad.setReadOnly(True)
        self.formulario.provincia.setReadOnly(True)
        self.formulario.pais.setReadOnly(True)
        self.formulario.dni.setReadOnly(True)

        self.formulario.aceptar.hide()
        self.formulario.cancelar.hide()
        self.formulario.nuevo.show()
        self.formulario.editar.show()
        self.formulario.eliminar.show()
        self.formulario.primero.show()
        self.formulario.anterior.show()
        self.formulario.posterior.show()
        self.formulario.ultimo.show()
        self.ultimoCliente()
            
        
        
        
    
    #funcion para conectar los botones, y mostrar el formulario    
    def mostrarFormulario(self):
        cliente1=Cliente()
        cliente1.crearClientes()
        del cliente1
        self.ultimoCliente()
        self.formulario.ultimo.clicked.connect(self.ultimoCliente)
        self.formulario.primero.clicked.connect(self.primerCliente)
        self.formulario.anterior.clicked.connect(self.anterior)
        self.formulario.posterior.clicked.connect(self.posterior)
        self.formulario.nuevo.clicked.connect(self.nuevoCliente)
        self.formulario.aceptar.clicked.connect(self.aceptar)
        self.formulario.cancelar.clicked.connect(self.cancelar)
        self.formulario.aceptar.hide()
        self.formulario.cancelar.hide()
        #motrar formulario
        self.formulario.show()
        
        
        







#creamos aplicacion QtWidegets
aplicacion=QtWidgets.QApplication([]) 
interfaz1=InterfazGrafica()
interfaz1.mostrarFormulario()
aplicacion.exec()