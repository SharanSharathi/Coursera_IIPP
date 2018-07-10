# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1


# Timer handler
def inc():
    global radius
    radius += 1
    
# Draw handler
def drawC(canvas):
    global radius, WIDTH, HEIGHT
    canvas.draw_circle([WIDTH/2, HEIGHT/2],radius,1,'black',"green")
        
# Create frame and timer
f = simplegui.create_frame('Expanding circle',WIDTH,HEIGHT)
f.set_canvas_background('white')
f.set_draw_handler(drawC)
t = simplegui.create_timer(100,inc)

# Start timer
f.start()
t.start()

