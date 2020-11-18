import ply.yacc as yacc
from MiniCLexer import tokens

def p_wae_1(p):
    'wae : ID ASSIGN wae SEMI'
    p[0] = [['id', p[1]], '=', p[3]]

def p_wae_2(p):
    'wae : LBRACE aList RBRACE'
    p[0] = p[2]

def p_wae_3(p):
    'wae : IF LPAREN wae RPAREN wae'
    p[0] = ['if', p[3], p[5]]

def p_wae_4(p):
    'wae : WHILE LPAREN wae RPAREN wae'
    p[0] = ['while', p[3], p[5]]

def p_wae_5(p):
    'wae : ID'
    p[0] = ['id', p[1]]

def p_wae_6(p):
    'wae : NUM'
    p[0] = ['num', p[1]]

def p_wae_7(p):
    'wae : wae OPTR wae'
    p[0] = [p[1], ['optr', p[2]], p[3]]

def p_aList_1(p):
    'aList : wae'
    p[0] = p[1]

def p_aList_2(p):
    'aList : aList wae'
    p[0] = p[1] + p[2]

def p_error(p):
    print('Syntax error in input!')

parser = yacc.yacc()