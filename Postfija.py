class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si est� vac�a. """
 
    def __init__(self):
        """ Crea una pila vac�a. """
        # La pila vac�a se representa con una lista vac�a
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila est� vac�a levanta una excepci�n. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila est� vac�a")

    def es_vacia(self):
        """ Devuelve True si la lista est� vac�a, False si no. """
        return self.items == []

def verificacionCar(valor):
    if(valor=="+" or valor=="-" or valor=="/" or valor=="-" or valor=="^"):
        return True
    else:
        return False
  
def verificacionInt(valor):
    try:
        valor = int(valor)
        return True
    except ValueError:
        return False

#def operacion(valor1,valor2,operacion):
#    if(operacion=="+"):
#        return valor1+valor2
#    if(operacion=="-"):
#        return valor1-valor2
#    if(operacion=="/"):
#        return valor1/valor2
#    if(operacion=="*"):
#        return valor1*valor2
#    if(operacion=="^"):
#        return valor1**valor2
    
pila = Pila()
while True:
    expresion = raw_input("Digite la expresion: ")
    try:
        for caracter in expresion:
            if(verificacionInt(caracter)==True):
                pila.apilar(caracter)
            else:
                derecha = pila.desapilar()
                izquierda = pila.desapilar()
                if(verificacionCar(caracter)==True):
                    pila.apilar("("+izquierda+caracter+derecha+")")
        operacion = pila.desapilar()
        print operacion
    except:
        print " La expresion no es valida"
        break
