from pila import *

caracteres = ['+','-','/','*','=']    
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
    if(valor=="+" or valor=="-" or valor=="/" or valor=="*" or valor=="^"):
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
    
def esDivision(var1,var2,operacion):
    if(operacion=="/" and var2==0):
        return True
    return False
    
def buscar(var1,var2):
    cont=0;
    for variable in var1:
        if(variable.identificador == var2 and cont == 0):
           cont+=1;
    return cont;

def cambiar(var1,var2,result):
    for variable in var1:
       if variable.identificador == var2:
           variable.valor=result
    return var1

def sintactico(listaExpresiones,errores):
    posError=0
    for y in listaExpresiones:
        posError += 1
        for x in y:
            if not validar(x):
                errores.append(Variable(posError,x))
    return errores
class Variable:
    def __init__(self, identificador, valor):
        self.identificador=identificador
        self.valor=valor
        
postfija="postfija.txt"
"Analisis lexico"
listaExpresiones = [y.split(' ') for y in [x.strip('\n') for x in open(postfija, "r").readlines()]]
pila=Pila()
variables=[]
respuestas=[]
errores=[]

def operacion_sin_variable(expresion):
    pilaOp = Pila()
    try:
        for caracter in expresion:
            if esVariable(caracter):
                for objeto in variables:
                    if(objeto.identificador==elemento):
                        caracter=objeto.valor
            if(verificacionInt(caracter)==True):
                pilaOp.apilar(caracter)
            else:
                derechaOp = pilaOp.desapilar()
                izquierdaOp = pilaOp.desapilar()
                if(verificacionCar(caracter)==True):
                    pilaOp.apilar(str(operar(int(izquierdaOp),int(derechaOp),caracter)))
        operada = pilaOp.desapilar()
        print "Res: "+str(operada)
    except:
        print "La expresion no es valida"
        

"------------------------Validación de la Expresión-----------------"
errores=sintactico(listaExpresiones,errores)
"------------------------Cálculo de la Expresión----------------------"
posError=0
if len(errores)==0:
    for expresion in listaExpresiones:
        posError +=1
        if expresion[len(expresion)-1]!="=":
            operacion_sin_variable(expresion)
        elif posError >0:
            for i, elemento in enumerate(expresion[:-1]):
                #print "Entra :"+str(posError)
                if esVariable(elemento):
                    #print "Entra :"+str(posError)
                    
                    if expresion[i+1]=="=":
                        "La variable está al final de la expresion, por lo que se agrega a la lista de variables"
                        if(pila.es_vacia()):
                            print "El sentido de la expresion es erroneo en la linea "+str(posError)
                            break
                        value=pila.desapilar()
                        if(buscar(variables,elemento)!=0):
                            variables=cambiar(variables,elemento,value)
                        else:
                            variables.append(Variable(elemento, value))
                    else:
                        "Se busca en la lista de variables la variable, se obtiene su valor, y se hace push en la pila el número..."
                        for objeto in variables:
                            if(objeto.identificador==elemento):
                                pila.apilar(int(objeto.valor))
                elif verificacionInt(elemento):
                    
                    pila.apilar(int(elemento))
                elif verificacionCar(elemento):
                    try:
                        valor1=pila.desapilar()
                        valor2=pila.desapilar()
                        if not(esDivision(valor2,valor1,elemento)):
                            pila.apilar(operar(valor2, valor1, elemento))
                        else:
                            print "Error division por cero"
                            posError=-1
                            break
                    except ValueError:
                        print "No se ha definido la variable en la linea "+str(posError) 
                        break
        else:
            break
    for var in variables:
        print var.identificador+" = "+str(var.valor)
else:
    for err in errores:
        print "Error en la operacion "+str(err.identificador)
        print "Caracter invalido " + str(err.valor)
