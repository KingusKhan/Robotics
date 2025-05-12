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
s1 = create_sprite("harry",-150,150)
s2 = create_sprite("bad (1)"-150,-150)

set_background("pitch")

time = 0
	
speed = 10

# Section 3: Controls
def moveup():
	s1.setheading(90)
	s1.forward(speed)

def moveleft():
	s1.setheading(180)
	s1.forward(speed)

def movedown():
	s1.setheading(270)
	s1.forward(speed)

def moveright():
	s1.setheading(270)
	s1.forward(speed)

def reset():
	s1.goto(-150,150)
	s1.goto(-150,-150)

def turbo():
	speed +=5
	s1.write("Turbo",font = ("Arial", 40, "norma;"))

def slow():
	speed -=5

window.onkeypress(moveup, "w")
window.onkeypress(moveleft, "a")
window.onkeypress(movedown, "s")
window.onkeypress(moveright, "d")
window.onkeypress(reset, "r")
window.onkeypress(turbo, "e")
window.onkeyrelease(slow, "e")

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions






	window.update()

	# if :
	# 	break
	

print("Game Over")