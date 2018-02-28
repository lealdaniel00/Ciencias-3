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
            print "here 2"
            return True
        elif operando.isupper():
            return True
        print "here 3"
        return False
    
postfija="postfija.txt"
exprecion = [y.split(' ') for y in [x.strip('\n') for x in open(postfija, "r").readlines()]]
for y in exprecion:
    for x in y:
        print x
        if validar(x):
            print "Expresion valida"
