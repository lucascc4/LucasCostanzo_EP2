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
t.right(90)	#cabeça
t.circle(30)
t.left(90)	#corpo
t.penup()
t.forward(60)
t.pendown()
t.forward(70)
t.penup()	#braço1
t.backward(60)
t.left(45)
t.pendown()
t.forward(40)
t.backward(40)
t.right(90)	#braço2
t.forward(40)
t.backward(40)
t.left(45)
t.forward(60)
t.left(45)	#perna1
t.forward(40)
t.backward(40)
t.right(90)	#perna2
t.forward(40)
t.backward(40)
t.left(45)
window.mainloop()

#importando palavras
arquivo = open("texto.txt","r", encoding="utf-8")
print(arquivo)