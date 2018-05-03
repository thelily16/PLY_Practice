# -*- coding: UTF-8 -*-
'''
Created on 2018年4月21日

@author: Fanny
'''
import ply.yacc as yacc
from lex_easy_example import tokens
from pip._vendor.packaging.requirements import EXTRA     

def p_order(p):
    'order : DRINK option'
    print(p[1] + p[2])

def p_option(p):
    '''option : NUMBER Toption SIZE 
    | NUMBER SIZE Toption 
    | Toption NUMBER SIZE
    | Toption SIZE NUMBER
    | SIZE NUMBER Toption
    | SIZE Toption NUMBER'''
    
    num = ''
    size = ''
    opt = ''
    for i in range(1, 4):
        if p[i].isdigit():
            num = ' * ' + p[i]
        elif p[i] == 'Large' or p[i] == 'Medium' or p[i] == 'Small':
            size = p[i][0:1]
        else:
            opt = p[i]
    p[0] = num + '\t ' + size + '\t ' + opt

def p_Toption(p):
    '''Toption : Setlevel SUGAR Setlevel ICE
                | Setlevel ICE Setlevel SUGAR'''
    
    if p[2] == 'Sugar':
        p[0] = p[1] + ' ' + p[2] + '\t' + p[3] + ' ' + p[4]
    else:
        p[0] = p[3] + ' ' + p[4] + ' \t' + p[1] + ' ' + p[2]

def p_Setlevel(p):
    '''Setlevel : level
                | PERCENT'''
    
    p[0] = p[1]

def p_level(p):
    '''level : LEVEL'''
    if p[1] == 'Extra':
        p[0] = '120%'
    elif p[1] == 'Regular':
        p[0] = '100%'
    elif p[1] == 'Less':
        p[0] = '70%'
    elif p[1] == 'Half':
        p[0] = '50%'
    elif p[1] == 'Little':
        p[0] = '30%'
    elif p[1] == 'No':
        p[0] = '0%'

def p_error(p):
    print('Please make sure your order is correct, '
          'it must contain Drink, Quantity, Size, Sugar level and Ice level!')
    
def make_parser():
    parser = yacc.yacc()
    return parser