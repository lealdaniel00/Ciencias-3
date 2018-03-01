from pila import *
caracteres = ['+','-','/','*']    
def caracter (valor):
    for y in caracteres:
        if y == valor :
            return True
    return False
def validar(operando):
    try:
        operando = int(operando)
        return True
    except ValueError:
        if caracter(operando):
            return True
        elif operando.isupper():
            return True
        return False
   
postfija="postfija.txt"
listaExpresiones = [y.split(' ') for y in [x.strip('\n') for x in open(postfija, "r").readlines()]]

"""------------------------Validación de la Expresión-----------------"""
for y in listaExpresiones:
    for x in y:
        print x
        if validar(x):
            print "Expresion valida"

"""------------------------Cálculo de la Expresión----------------------"""

def esVariable(elemento):
    if elemento.isupper():
        return True
    return False

def verificacionInt(valor):
    try:
        valor = int(valor)
        return True
    except ValueError:
        return False

def verificacionCar(valor):
    if(valor=="+" or valor=="-" or valor=="/" or valor=="-" or valor=="*" or valor=="^"):
        return True
    else:
        return False

def operar(valor1,valor2,operacion):
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

class Variable:
    def __init__(self, identificador, valor):
        self.identificador=identificador
        self.valor=valor

pila=Pila()
variables=[]

for expresion in listaExpresiones:
    for elemento in expresion:
        if esVariable(elemento):
            if expresion.index(elemento)==len(expresion)-2:
                """La variable está al final de la expresion, por lo que se agrega a la lista de variables"""
                variables.append(Variable(elemento, pila.desapilar()))
            else:
                """Se busca en la lista de variables la variable, se obtiene su valor, y se hace push en la pila el número..."""
                for objeto in variables:
                    if(objeto.identificador==elemento):
                         pila.apilar(int(objeto.valor))
        elif verificacionInt(elemento):
            pila.apilar(int(elemento))
        elif verificacionCar(elemento):
            valor1=pila.desapilar()
            valor2=pila.desapilar()
            pila.apilar(operar(valor2, valor1, elemento))
for var in variables:
    print var.identificador+" = "+str(var.valor)
    
