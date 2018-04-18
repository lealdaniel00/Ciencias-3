import ply.lex as lex

pReserv =['SI','si','entonces','ENTONCES','repetir','REPETIR','para','PARA','hacer','HACER','SINO','sino','mientras','MIENTRAS','HASTA','hasta','fin','FIN','ESCRIBIR','escribir','leer','LEER']
relacional=['<','>','<=','>=','==','!=','menor','MENOR','mayor','MAYOR','diferente','DIFERENTE','menor','MENOR','mayor','MAYOR']
tokens = ['PRESERVADA','RELACIONAL','VARIABLE','NUMERO','SUMA','RESTA','MULTIPLICACION', 'DIVISION','FINAL','ASIGNACION','POTENCIACION','MODULO']+pReserv

t_ignore = ' \t'
t_ASIGNACION = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_POTENCIACION = r'\^'
t_MODULO = r'%'
t_VARIABLE = r'[[a-zA-Z_][a-zA-Z0-9_]*'
t_FINAL = r'fin'
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_PRESERVADA(t):
    r'[[a-zA-Z_][a-zA-Z0-9_]*'
    return buscar(t)
def t_RELACIONAL(t):
    r'[[a-zA-Z_][a-zA-Z0-9_]*|(==) | (<) | (>) | (<=) | (>=) | (!=)'
    return buscar(t)

def buscar(t):
    for x in relacional:
        if x==t.value:
            t.type='RELACIONAL'
            return t
    for x in pReserv:
        if x==t.value:
            t.type='PRESERVADA'
            return t
    t.type = 'VARIABLE'
    return t
# Error handling rule
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
lex.lex() # Build the lexer
archivo="archivo.txt"
listaExpresiones = [x.strip('\n') for x in open(archivo, "r").readlines()]
for expresion in listaExpresiones:
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))
