from turtle import *

# Головне обчислення повороту
def test_heading(rots):
	if heading()+90==rots:
		res=90
	else:
		if heading()-90==rots:
			res=-90
		else:
			if heading()-270==rots:
				right(-90)
			if heading()+270==rots:
				right(90)
	return res

# Функції при натисканні клавіш
def move0():
	rot=test_heading(90)
	left(rot)
def move1():
	rot=test_heading(180)
	left(rot)
def move2():
	rot=test_heading(270)
	left(rot)
def move3():
	rot=test_heading(0)
	left(rot)

title('Omagad')# Назва вікна
color('blue')# Колір turtle
width(3)# Ширина лінії після turtle

# Прив'язування клавіш до відповідних функцій
onkey(move0, "w")
onkey(move1, "a")
onkey(move2, "s")
onkey(move3, "d")
listen()# Хз для чого це

# Цикл для руху змії у перед
while True:
	forward(1)

# Щоб не крашився
mainloop()
