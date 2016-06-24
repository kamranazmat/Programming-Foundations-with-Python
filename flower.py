import turtle

window = turtle.Screen()
window.bgcolor("white")

def draw_flower():
	flower = turtle.Turtle()
	flower.shape("turtle")
	flower.color("red")
	flower.speed(20)
	for i in range(45):
		for j in range(2):
			if j == 0:
				inner = "orange"
				outer = "red"
			else:
				inner = "red"
				outer = "orange"

			flower.color(inner)
			flower.forward(50)
			flower.right(45)
			flower.color(outer)
			flower.forward(50)
			flower.right(135)
		flower.right(8)

	flower.color("green")
	flower.right(90)
	flower.forward(200)
	window.exitonclick()


def draw_fractals():
	fractal = turtle.Turtle()
	fractal.shape("classic")
	fractal.color("green")
	fractal.speed(20)

	
draw_flower()
