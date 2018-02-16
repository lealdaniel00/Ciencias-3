# -*- coding: cp1252 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self,especialidad):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]
        self.especialidad=especialidad

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    def getEspecialidad(self):
        return self.especialidad

class Objeto:
    def __init__(self,documento,nombre):
        self.documento=documento
        self.nombre=nombre
    
lista=[]
atender=0
noEncontro=True
especialidad = ''
while True:
    try:
        persona = Objeto(int(input("Digite cedula: ")),raw_input("Digite nombre: "))
        especialidad = raw_input("Digite especialidad: ")
        atender+= 1  
        for elemento in lista:
            if ((elemento.es_vacia()==False) and atender>=2):
                print ('Se Atendio:')
                print(elemento.desencolar().nombre)
                atender=0
            if especialidad == elemento.getEspecialidad():
                print ('Se agrego a la lista de espera satisfactoriamente')
                elemento.encolar(persona)
                noEncontro=False
                break 
        if noEncontro==True:
            print ('Se agrego a la lista de espera satisfactoriamente')
            cola=Cola(especialidad)
            cola.encolar(persona)
            lista.append(cola)
        noEncontro=True
                
    except:
        print ("No se admiten mas pacientes")
        break   
for elemento in lista:
    if (elemento.es_vacia()==False):
        print ('Se Atendio:')
        print(elemento.desencolar().nombre)
