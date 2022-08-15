#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crear una función que devuelva True si los parámetros ingresados son todos números, 
False si hay al menos uno de los parámetros ingresados que no es un número, y 
None si ninguno de los parámetros ingresados es un número. 
Imprimir resultado por pantalla
"""

char = input("Enter character: ")

def number_true(char):
    if char.isdigit() == True:
        
        return char.isdigit()
    
    else: 
        return None
    
    
number_true(char)