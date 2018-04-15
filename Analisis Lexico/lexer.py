import ply.lex as lex

tokens = ['PRESERVADA','DESIGUALDAD','NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS']
pReserv =['SI','si','entonces','ENTONCES','para','PARA','hacer','HACER','SINO','sino']
desigualdad=['<','>','<=','>=','==','!=']
t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_DESIGUALDAD = r'== | < | > | <= | >= | !='

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_PRESERVADA(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    for x in pReserv:
        if x==t.value:
            return t
    t.type='NAME'
    return t
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lex.lex() # Build the lexer
pClave=['si','entonces']
archivo="archivo.txt"
listaExpresiones = [x.strip('\n') for x in open(archivo, "r").readlines()]
for expresion in listaExpresiones:
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))

