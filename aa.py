import ply.lex as lex

reserved = {
   'IF' : 'if',
   'THEN' : 'then',
   'ELSE' : 'else',

}

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS' ]+list(reserved.values())

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    print t.value
    print reserved.values()
    print reserved.get(t.value)
    if t.value in reserved.values():
        t.type = reserved.get(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lex.lex() # Build the lexer
expresiones="expresiones.txt"
listaExpresiones = [x.strip('\n') for x in open(expresiones, "r").readlines()]

for expresion in listaExpresiones:
    print expresion
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)

