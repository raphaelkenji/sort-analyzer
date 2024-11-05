import ply.yacc as yacc
import random

from lexer import tokens
from algorithms import compare

def p_command(p):
    '''
    COMMAND : ENTRY SEMICOLON 
            | ENTRY SEMICOLON COMMAND
    '''
    pass

def p_entry(p):
    '''
    ENTRY : COMPARE NUMBER FORMALGO
    '''
    if len(p[3]) < 2:
        print("Error: At least two algorithms are required.")
    else:
        array = [random.randint(0, 100) for i in range(p[2])]
        compare(array, p[3])
    
def p_formalgo(p):
    '''
    FORMALGO : ALGORITHM
             | ALGORITHM COMMA FORMALGO
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
        
def algorithm(p):
    '''
    ALGORITHM : BUBBLE_SORT
              | SELECTION_SORT
              | INSERTION_SORT
              | MERGE_SORT
              | QUICK_SORT
              | HEAP_SORT
    '''
    p[0] = p[1]
    
def p_error(p):
    print("Syntax error found!")

parser = yacc.yacc()   