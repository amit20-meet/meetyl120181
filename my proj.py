import turtle 
from turtle import Turtle
import random  
import time 



turtle.bgpic("AGARIOBG.gif")
turtle.hideturtle()
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
TIME_STEP = 10
LEFT = 2
RIGHT = 3
turtle.setheading(90)
RUNNING = True
sleep = 0.0099
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT =turtle.getcanvas().winfo_height()/2
turtle.tracer(0,0)
score = 0

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r , color):
		Turtle.__init__(self)
		self.shape("circle")
		self.penup()
		self.goto(x,y) 
		self.color(color)
		self.radius = r
		self.shapesize(r/10)
		self.dx = dx
		self.dy = dy

	def move(self, screen_width, screen_height):
			current_x = self.xcor()
			current_y = self.ycor()
			new_x = current_x + self.dx
			new_y = current_y + self.dy
			right_side_ball = new_x + self.radius
			left_side_ball = new_x - self.radius
			top_side_ball = new_y + self.radius
			bottom_side_ball = new_y - self.radius
			self.goto (new_x , new_y)

			if right_side_ball >= screen_width:
				self.dx = -self.dx
			
			if left_side_ball <= -screen_width:
				self.dx = -self.dx
			
			if top_side_ball >= screen_height:
				self.dy = -self.dy

			if bottom_side_ball <= -screen_height:
				self.dy = -self.dy

	def moveball(self, screen_width, screen_height):
		self.forward(5)
		current_x = self.xcor()
		current_y = self.ycor()
		new_x = current_x + self.dx
		new_y = current_y + self.dy
		right_side_ball = new_x + self.radius
		left_side_ball = new_x - self.radius
		top_side_ball = new_y + self.radius
		bottom_side_ball = new_y - self.radius

		if right_side_ball >= screen_width:
			self.backward(10)
			self.right(180)
		if left_side_ball <= -screen_width:
			self.backward(10)
			self.right(180)
		if top_side_ball >= screen_height:
			self.backward(10)
			self.right(180)
		if bottom_side_ball <= -screen_height:
			self.backward(10)
			self.right(180)
	
		def left():
			global setheading 
			#direction=self.heading()
			#self.setheading(-30+direction)
			self.left(10)

		def right():
			#direction=self.heading()
			#self.setheading(30+direction)
			self.right(10)
		turtle.onkey(left, LEFT_ARROW)
		turtle.onkey(right, RIGHT_ARROW)
		turtle.listen()





me=Ball( 100, 100, 50, 50, 40, "red")


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 5
MAXIMUM_BALL_RADIUS = 60
MINIMUM_BALL_DX = -3
MAXIMUM_BALL_DX = 3
MINIMUM_BALL_DY = -3
MAXIMUM_BALL_DY = 3

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	if dx == 0:
		dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	if dy == 0:
		dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())
	balli= Ball(x, y, dx, dy, radius, color)

	BALLS.append (balli)


def move_balls():
	for z in BALLS:
		z.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball2, ball1):
	ball2_pos = ball2.pos()
	ball1_pos = ball1.pos()	
	if ball2 == ball1 :
		return False
		sys.exit()
		
	ball2.xcor()
	ball2.ycor()
	ball1.xcor()
	ball1.ycor()

	DISTANCE_BETWEEN_CENTERS = ((ball2.xcor()-ball1.xcor())**2 + (ball2.ycor()-ball1.ycor())**2)**0.5

	if DISTANCE_BETWEEN_CENTERS+10 <= ball2.radius + ball1.radius:
		return True
	else:
		return False
		sys.exit()

def check_collision():
	for ball2 in BALLS:
		for ball1 in BALLS:
			if collide(ball2,ball1) == True:
				radius2 = ball2.radius
				radius1 = ball1.radius
				X_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
				X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while X_axis_speed == 0:
					 X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color = (random.random(), random.random(), random.random())

				if ball2 < ball1:
					ball2.goto(X_coordinate, Y_coordinate) 
					ball2.dx = X_axis_speed 
					ball2.dy = Y_axis_speed
					ball2.color(color)
					ball1.radius += 1
					ball2.radius = radius
					ball2.shapesize(ball2.radius/10)
					ball1.shapesize(ball1.radius/10)

				
				else:
					ball1.goto(X_coordinate, Y_coordinate)
					ball1.dx = X_axis_speed 
					ball1.dy = Y_axis_speed
					ball1.shapesize(radius/10)
					ball1.radius = radius
					ball1.color (color)
					ball2.radius += 1
					ball2.shapesize(ball2.radius/10)

	return True



def check_me_collision():
	for ball1 in BALLS:
		if collide(ball1,me) == True:
			radius_i = ball1.radius
			radius_me= me.radius
			global score
			if me.radius <= ball1.radius:
				turtle.write("LOSERRR!!", move = False, font=("arial",70,"normal"))
				return False

			else:
				X_coordinate = random.randint(int(-SCREEN_WIDTH) + int(MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH) - int(MAXIMUM_BALL_RADIUS))
				Y_coordinate = random.randint(int(-SCREEN_HEIGHT) + int(MAXIMUM_BALL_RADIUS),int(SCREEN_HEIGHT) - int(MAXIMUM_BALL_RADIUS))
				X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while X_axis_speed == 0:
					X_axis_speed = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while Y_axis_speed  == 0:
					Y_axis_speed  = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)

				me.radius +=10
				me.shapesize(me.radius/10)
				score += 1
				ball1.goto(X_coordinate, Y_coordinate)
				ball1.dx = X_axis_speed 
				ball1.dy = Y_axis_speed
				ball1.shapesize(radius/10)
				ball1.radius = radius
				ball1.color((random.random(), random.random(), random.random()))
				
				

	return True
	

while RUNNING == True:
	if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2 :
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2 
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
	
	move_balls()
	check_collision()
	turtle.clear()
	turtle.color("black")
	turtle.goto(-450,300)
	turtle.write("score: "+ str(score), font=("arial",20,"normal"))




	me.moveball( SCREEN_WIDTH, SCREEN_HEIGHT )
	RUNNING = check_me_collision()
	time.sleep(sleep)
	turtle.update()
	if score>55:
		turtle.write("you won", move = False, font=("arial",70,"normal"))
		RUNNING = False



turtle.mainloop()
