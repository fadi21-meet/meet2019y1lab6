#import turtle
#turtle.goto(0,0)

#def up():
   # print("you pressed the up key.")

#turtle.onkey(up, "Up")
#turtle.goto(0,0)
#turtle.listen()

import turtle
turtle.goto(0,0)

turtle.direction = None

def up():
    turtle.direction = "w"
    print("you pressed the w key.")

turtle.onkey(w, "w")
turtle.listen()

def on_move():
    #to do
