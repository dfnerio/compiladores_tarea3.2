# PARSER CODE
# Diego Frías Nerio A01193624

import ply.yacc as yacc
from lexer import tokens

precedence = ( # set order of operators to resolve some conflicts
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

start = 'parser'  # start checking at 'parser'


def p_parser(p):  # check for all types so that it can detect them individually
    ''' parser  : programa
                | bloque
                | vars
                | estatuto
                | asignacion
                | condicion
                | escritura
                | expresion
                | varcte
                | exp
                | termino
                | factor
                | tipo
                | empty'''
    p[0] = p[1]


def p_vars(p):
    ''' vars  : VAR v1
        v1        : ID v2 DOTS tipo DOTCOMMA v1
                  | empty
        v2        : COMMA ID v2
                  | empty'''
    p[0] = "VARIABLES"


def p_programa(p):
    ''' programa  : PROGRAM ID DOTS p1 bloque
        p1        : vars
                  | empty'''
    p[0] = "PROGRAMA"


def p_bloque(p):
    ''' bloque  : LBRACK b1 RBRACK
        b1      : estatuto b1
                | empty'''
    p[0] = "BLOQUE"


def p_estatuto(p):
    ''' estatuto  : asignacion
                  | condicion
                  | escritura'''
    p[0] = "ESTATUTO"


def p_asignacion(p):
    'asignacion  : ID EQUAL expresion'
    p[0] = "ASIGNACIÓN"


def p_condicion(p):
    ''' condicion : IF LPAREN expresion RPAREN bloque c1 DOTCOMMA
        c1        : ELSE bloque
                  | empty'''
    p[0] = "CONDICIÓN"


def p_escritura(p):
    ''' escritura : PRINT LPAREN es1 RPAREN DOTCOMMA
        es1       : expresion es2
                  | ID es2
        es2       : COMMA es1
                  | empty'''
    p[0] = "ESCRITURA"


def p_expresion(p):
    ''' expresion : exp e1
        e1        : e2 exp
                  | empty
        e2        : RELOP
    '''
    p[0] = "EXPRESIÓN"


def p_exp(p):
    ''' exp : termino ex1
        ex1 : ex2 exp
            | empty
        ex2 : PLUS
            | MINUS
    '''
    p[0] = "EXP"


def p_termino(p):
    ''' termino : factor t1
        t1      : t2 termino
                | empty
        t2      : TIMES
                | DIVIDE
                | empty
    '''
    p[0] = "TÉRMINO"


def p_factor(p):
    ''' factor  : f1
                | f2
        f1      : LPAREN expresion RPAREN
        f2      : f3 varcte
        f3      : PLUS
                | MINUS
                | empty
    '''
    p[0] = "FACTOR"


def p_varcte(p):
    ''' varcte  : ID
                | CTEI
                | CTEF'''
    p[0] = "VARCTE"


def p_tipo(p):
    '''tipo : INT
            | FLOAT'''
    p[0] = "TIPO"


def p_empty(p):
    'empty :'
    pass


# error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)


parser = yacc.yacc()  # build the parser
file = open('script.txt', 'r')  # read file
code = ' '.join(file.readlines())  # concat lines to create a single string

result = parser.parse(code)  # parse
print(result)
