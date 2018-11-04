import turtle
turtle.goto (0,0)
list1= [blue, red, yellow, orenge, black]
a= 0
for i in range(5):
	turtle.right(144)
	turtle.forward(200)
	turtle.color(list1[a])
	a= a+1



turtle.mainloop()

