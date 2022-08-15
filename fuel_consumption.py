#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crear una función que calcule cuántos litros de nafta gasta un auto que 
consume 2 litros x 100km, en un viaje ida y vuelta MdP-Bue si la distancia es de 400km.
Luego crear una función que, a partir de esos datos, devuelva cuánto significa eso en pesos 
si el litro de nafta está 60$.
"""

# consumption = 2 / 100 == 0.02 liters per kilometer

distance = float(input("Indicate the total distance to travel, in kilometers: "))

def consumption(distance):
    consumption_km = distance * 0.02
    
    print(f"The car consumes {consumption_km} liters per {distance} kilometers")
    return consumption_km

def fuel_value(x):
    # value = 60 pesos per liter. 
    #So the function receives a value and then multiplies that by 60
    value = x * 60
    
    print(f"These liters have a total value of ${value}")
    return value
    
fuel_value(consumption(distance))