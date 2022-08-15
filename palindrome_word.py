#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crear una función que verifique si una palabra es un palíndromo o no. 
En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", 
en caso contrario, devolver "La palabra no es un palíndromo"
"""
word = str(input("Please insert a word: "))
def palindrome(word):
    if word == word[::-1]:
        print("The word is a palindrome")
    else: print ("The word isn't a palindrome")


palindrome(word)