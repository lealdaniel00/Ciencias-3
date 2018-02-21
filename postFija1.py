class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

def verificacionCar(valor):
    if(valor=="+" or valor=="-" or valor=="/" or valor=="-" or valor=="^" or "*"):
        return True
    else:
        return False
  
def verificacionInt(valor):
    try:
        valor = int(valor)
        return True
    except ValueError:
        return False
    
def op(valor1,valor2,operacion):
    if(operacion=="+"):
        return valor1+valor2
    if(operacion=="-"):
        return valor1-valor2
    if(operacion=="/"):
        return valor1/valor2
    if(operacion=="*"):
        return valor1*valor2
    if(operacion=="^"):
        return valor1**valor2
    

while True:
    pila = Pila()
    pilaOp = Pila()
    expresion1 = raw_input("Digite la expresion: ")
    expresion = expresion1.split(" ")
    try:
        for caracter in expresion:
            if(verificacionInt(caracter)==True):
                pila.apilar(caracter)
                pilaOp.apilar(caracter)
            else:
                derecha=pila.desapilar()
                izquierda=pila.desapilar()
                derechaOp = pilaOp.desapilar()
                izquierdaOp = pilaOp.desapilar()
                result=derechaOp+izquierdaOp
                if(verificacionCar(caracter)==True):
                    pila.apilar("("+izquierda+caracter+derecha+")")
                    pilaOp.apilar(str(op(int(izquierdaOp),int(derechaOp),caracter)))
        operacion = pila.desapilar()
        print "Infija "+operacion
        operada = pilaOp.desapilar()
        print "Resultado: "
        print operada
    except:
        print " La expresion no es valida"
        break
