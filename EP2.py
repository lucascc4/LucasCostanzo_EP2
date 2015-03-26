# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:37:41 2015

@author: LUCAS C
"""

#LucasCostanzo

import turtle
from random import *

window = turtle.Screen()    
window.bgcolor("red")
window.title("Jogo Da Forca")

t = turtle.Turtle()  # Cria um objeto "desenhador"
t.speed(30) 
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



def cabeça():
	t.right(90)	#cabeça
	t.circle(30)
def corpo():
	t.left(90)	#corpo
	t.penup()
	t.forward(60)
	t.pendown()
	t.forward(70)
def braco1():
	t.penup()	#braço1
	t.backward(60)
	t.left(45)
	t.pendown()
	t.forward(40)
	t.backward(40)
def braco2():
	t.right(90)	#braço2
	t.forward(40)
	t.backward(40)
	t.left(45)
	t.forward(60)
def perna1():
	t.left(45)	#perna1
	t.forward(40)
	t.backward(40)
def perna2():
	t.right(90)	#perna2
	t.forward(40)
	t.backward(40)
	t.left(45)

#variavel_texto = window.textinput("Letra", "Escolha uma letra")	#caixa de texto

t1 = turtle.Turtle()
t1.speed(30) 
t1.penup()      
t1.setpos(-170,-70)

p = open("texto.txt", encoding="utf-8")
palavra = p.readlines()

limpa = []
for pa in palavra:
	x = pa.strip()
	if x != "":
		limpa.append(x)

def traço(palavra):
	for c in palavra:
		if c ==" ":
			t1.penup()
			t1.forward(20)
			t1.pendown()
			
		if c !=" ":
			t1.pendown()
			t1.forward(15)
			t1.penup()
			t1.forward(5)
	
			
pc = choice(limpa)
traço(pc)	#chama a funao de desenho da palavra
erro = 0
while erro < 6:
	v = window.textinput("Letra", "Escolha uma letra")
	if v in pc:
		i = pc.index(v)
		t1.penup()
		t1.setpos(-170+20*i, -65)
		t1.pendown()
		t1.write(v)
	else:
		erro +=1
		if erro == 1:
			cabeça()
		if erro == 2:
			corpo()
		if erro == 3:
			braco1()
		if erro == 4:
			braco2()
		if erro == 5:
			perna1()
		if erro == 6:
			perna2()
		


window.mainloop()



			
		

	