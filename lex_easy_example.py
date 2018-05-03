# -*- coding: UTF-8 -*-
'''
Created on 2018年4月20日

@author: Fanny
'''
import ply.lex as lex

tokens = ['DRINK', 'SUGAR', 'ICE', 'NUMBER', 'LEVEL', 'PERCENT', 'SIZE']

t_DRINK = r'Greentea|Blacktea|Bubbletea|Oolongtea|Juice|Coffee'
t_SUGAR = r'Sugar'
t_ICE = r'Ice'
t_LEVEL = r'Extra|Regular|Less|Half|Little|No'
t_SIZE = r'Large|Medium|Small'
t_PERCENT = r'120%|100%|70%|50%|30%|0%'
t_NUMBER = r'[0-9]+'
t_ignore = ' \n\t'

def t_error(t):
    print('Sorry, there is something wrong in you order, please check it.')

def make_lexer():
    lexer = lex.lex()
    return lexer