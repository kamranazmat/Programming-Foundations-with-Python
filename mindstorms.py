import turtle

window = turtle.Screen()
window.bgcolor("white")

def draw_square():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(20)

	for i in range(0, 72):
		for j in range(0, 4):
			brad.forward(100)
			brad.right(90)
		brad.right(5)

	for i in range(0, 36):
		for j in range(0, 4):
			brad.forward(200)
			brad.right(90)
		brad.right(10)
	
	
def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("yellow")
	angie.speed(20)

	for i in range(0, 18):
		angie.circle(100)
		angie.right(20)
	
def draw_triangle():
	tri = turtle.Turtle()
	tri.shape("classic")
	tri.color("orange")
	tri.speed(20)
	for i in range(0, 36):
		for j in range(0, 3):
			tri.forward(150)
			tri.right(120)
		tri.left(10)

draw_square()
draw_circle()
draw_triangle()
window.exitonclick()