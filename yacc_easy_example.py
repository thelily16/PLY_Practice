# -*- coding: UTF-8 -*-
'''
Created on 2018年4月21日

@author: Fanny
'''
import ply.yacc as yacc
from lex_easy_example import tokens
import CheckValue as CV

total_price = 0

def p_command(p):
    '''command : order command
    | done command
    | order
    | menu
    | exit
    | done'''

def p_order(p):
    'order : DRINK option'
    
    global total_price
    item = str(p[1]).ljust(15) + p[2]
    #count the price of item
    item_price = CV.CountPrice(item)
    print(str(item).ljust(50) + str(item_price).ljust(10))
    #add the price to total price
    total_price = total_price + item_price

#the sequence of option can be random
def p_option(p):
    '''option : quantity Doption size 
    | quantity size Doption 
    | Doption quantity size
    | Doption size quantity
    | size quantity Doption
    | size Doption quantity'''
    
    num = ''
    size = ''
    opt = ''
    #format the option
    for i in range(1, 4):
        if p[i].isdigit():
            num = p[i]
        elif p[i] == 'Large' or p[i] == 'Medium' or p[i] == 'Small':
            size = p[i][0:1]
        else:
            opt = p[i]
    p[0] = num.ljust(5) + size.ljust(5) + opt.ljust(20)

def p_quantity(p):
    '''quantity : NUMBER
    | empty'''
    
    if p[1] == '':
        p[0] = '1'
    else:
        p[0] = p[1]

def p_size(p):
    '''size : SIZE
    | empty'''
    
    if p[1] == '':
        p[0] = 'Large'
    else:
        p[0] = p[1]

#the sequence of Sugar option and Ice option can be random
def p_Doption(p):
    '''Doption : Soption Ioption
    | Ioption Soption'''
    
    if "Sugar" in p[1]:
        p[0] = p[1] + '\t' + p[2]
    else:
        p[0] = p[2] + '\t' + p[1]

def p_Soption(p):
    '''Soption : Slevel
    | empty'''
    
    sugar = p[1]
    if sugar == '':
        p[0] = '100%'.ljust(5) + 'Sugar'
    else:
        p[0] = sugar  

def p_Slevel(p):
    'Slevel : Setlevel SUGAR'
    
    p[0] = str(p[1]).ljust(5)+ str(p[2])

def p_Ioption(p):
    '''Ioption : Ilevel
    | empty'''
    
    ice = p[1]
    if ice == '':
        p[0] = '100%'.ljust(5) + 'Ice'
    else:
        p[0] = p[1]

def p_Ilevel(p):
    'Ilevel : Setlevel ICE'
    
    p[0] = str(p[1]).ljust(5) + str(p[2])

def p_Setlevel(p):
    '''Setlevel : level
    | PERCENT'''
    
    p[0] = p[1]

def p_level(p):
    '''level : LEVEL'''
    #change level to percent
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

def p_menu(p):
    'menu : MENU'
    
    f = open('./Menu.txt', 'r')
    print(f.read())

def p_exit(p):
    'exit : EXIT'
    
    exit()

# Show total price of the order
def p_done(p):
    'done : DONE'
    
    global total_price
    print('Total Price: ' + str(total_price) + '\n')
    total_price = 0

def p_empty(p):
    'empty :'
    
    p[0] = ''
    
def p_error(p):
    print('Please make sure your order is correct!')
    
def make_parser():
    parser = yacc.yacc()
    return parser