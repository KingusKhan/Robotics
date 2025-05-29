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
s1 = create_sprite("harry", -250, 0)
s2 = create_sprite("bad (1)", 250, 0)

set_background("pitch (1)")

lives = 3
score = 0

# Section 3: Controls
def move_up():
	s1.setheading(90)
	s1.forward(7)

def move_down():
	s1.setheading(270)
	s1.forward(7)

def move_right():
	s1.setheading(0)
	s1.forward(7)

def move_left():
	s1.setheading(180)
	s1.forward(7)

def cheat():
	s1.goto(-250,0)

def dash():
	s1.hideturtle()
	s1.forward(60)
	s1.showturtle

# Key Binds
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(cheat, "r")
window.onkeypress(dash, "e")

# Section 4: Game Loop
window.listen()
timer = 0
obstacles = []
while True:
	time.sleep(0.1)
	timer += 1  

	if get_distance(s1,s2) < 1:
		s1.goto(-250, 0)
		s2.goto(250, 0)
		lives -= 1

	if timer % 100 == 0:
		y_position = random.randint(-250, 250)
		s3 = create_sprite("golden-snitch", 300, y_position)
		s3.setheading(180)
		obstacles.append(s3)

	for s3 in obstacles:
		s3.forward(10)
		if get_distance(s1,s3) < 50:
			score += 2
			s3.hideturtle()
			obstacles.remove(s3)

	s2.setheading(180 / 3.14 * math.atan2(s1.ycor() - s2.ycor(), s1.xcor() - s2.xcor()))
	s2.forward(5)

	window.update()

	# Ending
	if lives == 0:
		print("You Lost!")
		break

	if score == 5:
		print("You Won!")
		break

	if timer == 700:
		print("Do Something!")
		break
	
print("Game Over")