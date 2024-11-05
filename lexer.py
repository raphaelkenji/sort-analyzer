import ply.lex as lex

tokens = [    
    'COMPARE',
    'BUBBLE_SORT', 'SELECTION_SORT', 'INSERTION_SORT', 'QUICK_SORT', 'MERGE_SORT', 'HEAP_SORT',
    'SEMICOLON', 'COMMA', 'NUMBER',
]

t_SEMICOLON = r';'
t_COMMA = r','

def t_COMPARE(t):
    r'[Cc][Oo][Mm][Pp][Aa][Rr][Ee]'
    return t

def t_BUBBLE_SORT(t):
    r'[Bb][Uu][Bb][Bb][Ll][Ee][_][Ss][Oo][Rr][Tt]'
    return t

def t_SELECTION_SORT(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt][Ii][Oo][Nn][_][Ss][Oo][Rr][Tt]'
    return t

def t_INSERTION_SORT(t):
    r'[Ii][Nn][Ss][Ee][Rr][Tt][Ii][Oo][Nn][_][Ss][Oo][Rr][Tt]'
    return t

def t_MERGE_SORT(t):
    r'[Mm][Ee][Rr][Gg][Ee][_][Ss][Oo][Rr][Tt]'
    return t

def t_QUICK_SORT(t):
    r'[Qq][Uu][Ii][Cc][Kk][_][Ss][Oo][Rr][Tt]'
    return t

def t_HEAP_SORT(t):
    r'[Hh][Ee][Aa][Pp][_][Ss][Oo][Rr][Tt]'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    if t.value < 0:
        print("Error: The number must be greater than zero.")
    elif t.value > 1000:
        print("Warning: The number is too big. It may take a long time to compare the algorithms.")
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()