# -*- coding: UTF-8 -*-
'''
Created on 2018年5月3日

@author: Fanny
''' 

def CountPrice(item):
    order = item.split()
    #print(order)
    drink = order[0]
    num = order[1]
    size = order[2]
    value = CheckPrice(drink, size) * int(num)
    return value
    

def CheckPrice(drink, size):
    dict = {'Greentea': {'S': 10, 'M': 15, 'L': 20},
            'Blacktea': {'S': 10, 'M': 15, 'L': 20},
            'Bubbletea': {'S': 20, 'M': 25, 'L': 30},
            'Oolongtea': {'S': 10, 'M': 15, 'L': 20},
            'Juice': {'S': 15, 'M': 20, 'L': 25},
            'Coffee': {'S': 35, 'M': 40, 'L': 45}}
    
    price = dict[drink][size]
    return price