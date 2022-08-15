#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ezequielpolacco

Crear una función que devuelva una lista con todos los números pares del 0 al 100 inclusive.
Imprimir esa lista por pantalla.

"""

def even_list():
    even = []
    for i in range(0,101):
        if i % 2 == 0:
            even.append(i)
    return even
        
            


even_list()