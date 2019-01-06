import turtle 
from turtle import Turtle
import random  

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r , color):
		Turtle.__init__(self)
		self.shape("circle")
		self.penup()
		self.x = x
		self.y = y
		self.color(color)
		self.r = r
		self.dx = dx
		self.dy = dy

	def move(self, screen_width, screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx

		current_y = self.ycor()
		new_y = current_y + self.dy
		self.goto(new_x,new_y)

class Point:
	def __init__(self, x=0, y=0,):
		self.x = x
		self.y = y




ball1=Ball( 100, 100, 50, 50, 4,(random.random(), random.random(), random.random()))
ball1.move(100,100)
turtle.mainloop()

