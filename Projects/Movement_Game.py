# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
s1 = create_sprite("harry", -150,150)
s2 = create_sprite("bad (1)", -150,-150)
s3 = create_sprite("golden-snitch", 150,0)

set_background("pitch (1)")

speed = 5

# Section 3: Controls
def move_up():
	s1.setheading(90)
	s1.forward(speed)

def move_left():
	s1.setheading(180)
	s1.forward(speed)

def move_down():
	s1.setheading(270)
	s1.forward(speed)

def move_right():
	s1.setheading(0)
	s1.forward(speed)

def reset():
	s1.goto(-150,150)
	s1.goto(-150,-150)

def turbo():
	speed +=2
	s1.write("Turbo",font = ("Arial", 40, "norma;"))

def slow():
	speed -=2

window.onkeypress(move_up, "w")
window.onkeypress(move_left, "a")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(reset, "r")
window.onkeypress(turbo, "1")
window.onkeypress(slow, "2")

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  

	#s2.setheading(s2.towards(s1))
	#s2.forward(3)

	if timer % 10 == 0:
		s3.setheading(random.randint(0, 360))

	s3.forward(10)


	x, y = s3.xcor(), s3.ycor()
	if abs(x) > 300 or abs(y) > 225:
		s3.setheading(s3.towards(0, 0))

	




	window.update()

	if get_distance(s1,s3) < 20:
		s1.write("You Win!", font = ("Arial", 40, "normal"))
		s2.hideturtle()
		break

	elif get_distance(s2,s3) < 20:
		s2.write("You Lose!", font = ("Arial", 40, "normal"))
		s1.hideturtle()
		break
	
	elif timer == 60:
		s3.write("You Lose!", font = ("Arial", 40, "normal"))

print("Game Over")