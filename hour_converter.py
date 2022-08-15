#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ezequielpolacco

Crear una función que, a partir de un dato de entrada que sea en horas, 
nos informe cuántos minutos y cuántos segundos serán esas horas. 
Imprimir por pantalla dichos valores.

"""

hour = float(input("Input hour value in 24hs format: "))

def convert(hour):
    minute_value = hour * 60
    sec_value = minute_value * 60
    
    print("Converted hour value in minutes: ", minute_value)
    print("Converted hour value in seconds: ", sec_value)

convert(hour)