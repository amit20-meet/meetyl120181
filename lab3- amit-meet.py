'''

class animal(object):
	def __init__(self,sound,name,age,favorite_color,food):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
		self.food = food
	def eat(self,food):
		print("yummy!!" + self.name + " is eating " +food)
	def description(self):
		print(self.name + " is " + self.ega + " years old and loves the color " + self.favorite_color)

w = animal("scream", "wolf", 5, "white", "rabit")
'''


import turtle
turtle.register_shape("trash.gif")
turtle.shape("trash.gif")
asd = 1
turtle.speed(100000)
for i in range(720):
	asd = asd + 0.5
	turtle.pendown()
	turtle.right(asd)
	turtle.forward(340)
	turtle.right(45)
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.home()
turtle.mainoop()