import ply.lex as lex

reserved = {'if':'IF', 'while':'WHILE'}

tokens = ['NUM', 'ID', 'LBRACE', 'RBRACE', 'SEMI',
          'LPAREN', 'RPAREN', 'ASSIGN', 'OPTR'] + list(reserved.values())

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_SEMI = r';'
t_IF = r'[iI][fF]'
t_WHILE = r'[wW][hH][iI][lL][eE]'

def t_NUM(t):
    r'[+-]?[0-9]+(\.[0-9]*)?'
    t.value = float(t.value)
    t.type = 'NUM'
    return t

def t_ID(t):
    r'[a-zA-Z][_a-zA-Z0-9]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

def t_OPTR(t):
    r'(>=|<=|==|>|<|\+|\-|\*|/)'
    t.type = 'OPTR'
    return t

t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    raise Exception('LEXER ERROR')


lexer = lex.lex()