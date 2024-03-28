from turtle import *

def move0():
	if not heading()==180+90:
		if heading()+90==90:
			left(90)
		else:
			if heading()-90==90:
				right(90)
		forward(10)
	else:
		left(180)
		forward(10)

def move1():
	if not heading()==0:
		if heading()+90==180:
			left(90)
		else:
			if heading()-90==180:
				right(90)
		forward(10)
	else:
		left(180)
		forward(10)

def move2():
	if not heading()==180:
		if not heading()==90:
			if heading()+90==-90:
				left(90)
			else:
				if heading()-90==-90:
					right(90)
			forward(10)
		else:
			left(180)
			forward(10)
	else:
		left(90)
		forward(10)

def move3():
	if not heading()==180:
		if not heading()==180+90:
			if heading()+90==0:
				left(90)
			else:
				if heading()-90==0:
					right(90)
			forward(10)
		else:
			left(90)
			forward(10)
	else:
		left(180)
		forward(10)

title('Omagad')
color('blue')
width(3)

onkey(move0, "w")
onkey(move1, "a")
onkey(move2, "s")
onkey(move3, "d")
listen()

mainloop()