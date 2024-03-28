from turtle import *
import random as ran

title('Omagad')
color('blue')
width(3)

while True:
	if int(ran.randint(0, 2))==1:
		forward(5)
	left(int(ran.randint(-15, 15)))