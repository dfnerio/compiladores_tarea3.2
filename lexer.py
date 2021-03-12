# LEXER CODE
# Diego Frías Nerio A01193624

import ply.lex as lex
import re

reserved = {  # list of reserved words
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT'
}


tokens = [  # list of tokens
    'DIGITS',
    'LETTER',
    'ID',
    'WS',
    'DOTS',
    'DOTCOMMA',
    'COMMA',
    'LBRACK',
    'RBRACK',
    'LPAREN',
    'RPAREN',
    'RELOP',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUAL',
    'CTEI',
    'CTEF'
] + list(reserved.values()) # add reserved words tokens to the list

# regex for tokens

t_DIGITS = r'[0-9]+'
t_LETTER = r'[A-Za-z]'
t_WS = r'\s|\t|\n'
t_DOTS = r'\:'
t_DOTCOMMA = r'\;'
t_COMMA = r'\,'
t_LBRACK = r'\{'
t_RBRACK = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RELOP = r'>|<|(<>)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'\='


def t_CTEF(t):  # check if number is an int
    r'[-+]?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_CTEI(t):  # check if a number is a float
    r'[-+]?\d+'
    t.value = int(t.value)
    return t


def t_ID(t):  # check if a word is reserved, otherwise defaults to ID
    r'[A-Za-z](([A-Za-z])|([0-9]))*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_newline(t):  # rule for tracking line numbers
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_error(t):  # handle errors
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# build the lexer
lexer = lex.lex()
