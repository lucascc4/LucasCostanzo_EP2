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
t.backward(100)
t.forward(50)
t.left(90)
t.forward(300)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
