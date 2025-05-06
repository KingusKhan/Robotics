# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
    image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite = turtle.Turtle()
    sprite.shape(image_file)
    sprite.penup()
    sprite.goto(x,y)
    return sprite


# Section 2 - Variables
x1 = -200
y1 = 200
x2 = -200
y2 = 100
x3 = -200
y3 = 0
x4 = -200
y4 = -100


# Section 3 - Setup
set_background("track")
t1 = create_sprite("minecraft-chicken-jockey",x1,y1)
t2 = create_sprite("horse (1)",x2,y2)
t3 = create_sprite("runner (2)",x3,y3)
t4 = create_sprite("dark_horse",x4,y4)


# Section 4 - Racing
for i in range(30):
    x1 += random.randint(1 + i,2 + i)
    x2 += random.randint(5,20)
    x3 += 13
    x4 += random.randint(10,15)
    
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.01)


# Section 5 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Player 1 Wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("Player 2 Wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("Player 3 Wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print("Player 3 Wins!")
else:
    print("Tie!")
