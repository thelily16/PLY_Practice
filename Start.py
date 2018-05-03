# -*- coding: UTF-8 -*-
'''
Created on 2018年4月24日

@author: Fanny
'''
import yacc_easy_example
import lex_easy_example

Lexer = lex_easy_example.make_lexer()
Parser = yacc_easy_example.make_parser()

while True:
    print('Hello, please enter your order!')
    print('1. If you want to see the menu, please enter "Menu"')
    print('2. If you finish your order, please enter "Done"')
    print('3. If you want to exit, please enter "Exit"')
    print('P.S: You have to enter Drink first and then enter Option, which contains Quantity, '
          'Size, "xxx Sugar" and "xxx Ice".')
    print('***********************************************************************************'
          '***********************************')
    order = input()
    result = Parser.parse(order, lexer = Lexer)
    
#===============================================================================
#     order = ''
#     All_order = []
#     while(order != 'Done'):
#         # If you want to order some drinks, the input should look like "DRINK SIZE QUANTITY SUGARLEVEL ICELEVEL"
#         # If you finish to order and want to parse your order, please enter "Done"
#         order = input()
#         if order != 'Done':
#             # If you want to see menu, please enter "Menu" and the menu will be showed.
#             if order == 'Menu':
#                 f = open('./Menu.txt', 'r')
#                 print(f.read())
#                 print ('\nPlease enter your order!')
#             # If you want to end the program, please enter "Exit", then the program will be end
#             elif order == 'Exit':
#                 exit()
#             else:
#                 All_order.append(order)
# 
#     '''
#     After enter "Done", the parser will be parse your oder in the order that you enter
#     and return the order in formal format
#     '''
#     for s in All_order:
#         result = Parser.parse(s, lexer = Lexer)
#     print('\n')
#===============================================================================