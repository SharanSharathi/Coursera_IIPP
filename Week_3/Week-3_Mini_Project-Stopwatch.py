# Testing template for format function in "Stopwatch - The game"

###################################################
# Student should add code for the format function here
import simplegui

num = 0
count = 0
won = 0
color = "Olive"
text = 'Lets Go yeah!'
running = False
    
def tick():
    global num
    num += 1
    
def format(cal):
    msec = cal % 10
    sec1 = (cal //10) % 10
    sec2 = (cal //100) % 6
    min1 = (cal // 600) % 10
    min2 = (cal //6000)
    return (str(min2) + str(min1) + ':' + str(sec2) + str(sec1) + "." + str(msec))
    

def start():
    global running, text, color
    frame.set_canvas_background("silver")
    timer.start()
    running = True
    text = "Now stop the timer"
    color = "Yellow"
    
def stop():
    global running, won, count, text, color
    timer.stop()
    if running:
        if (num% 10 == 0):
            won += 1
            count += 1
            frame.set_canvas_background("Yellow")
            text = "Awesome!!!"
            color = "Green"
            
        else:
            count += 1
            frame.set_canvas_background("Red")
            text = "Try again!"
            color = "lime"
            
    running = False
    
def reset():
    global num, count, won, text, color
    timer.stop()
    num = 0
    count = 0
    won = 0
    text = 'Lets Go Again!'
    color = "Olive"
    frame.set_canvas_background("Aqua")
    
    
def draw(canvas):
    global num
    canvas.draw_text(format(num), [25,90], 50, 'black') 
    canvas.draw_text((str(won) +"/" + str(count)),[130,25],30,'black')
    canvas.draw_text(text,[10,140],24,color)
    
    
    
    
frame = simplegui.create_frame("Stopwatch",200,150)
frame.set_canvas_background('white')
frame.set_draw_handler(draw)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
timer = simplegui.create_timer(100, tick)



frame.start()
###################################################
# Test code for the format function
# Note that function should always return a string with 
# six characters


print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9

