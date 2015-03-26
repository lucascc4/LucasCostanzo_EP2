# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:37:41 2015

@author: LUCAS C
"""

#LucasCostanzo

import turtle
from random import randint

window = turtle.Screen()    
window.bgcolor("red")
window.title("Jogo Da Forca")

t = turtle.Turtle()  # Cria um objeto "desenhador"
t.speed(10) 
t.penup()       # Remova e veja o que acontece
t.setpos(-250,-40)
t.pendown()
t.color("black")
t.left(90)