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