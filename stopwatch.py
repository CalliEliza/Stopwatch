# template for "Stopwatch: The Game"
import simplegui
import time

# define global variables
counter = 0
success = 0
total_stops = 0
isRunning = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = t//600
    milli_sec = t%10
    sec = (t/10)%10
    t_sec = (t-minute*600)//100
    min = (t/600)%600
    
    stopwatch = str(min)+":"+str(t_sec)+str(sec)+"."+str(milli_sec)
    return stopwatch
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isRunning
    timer.start()
    isRunning = True

def stop():
    global total_stops
    global success
    global isRunning
    timer.stop()
    if isRunning == True:
        isRunning = False
        total_stops +=1
        if counter % 10 == 0:
            success+=1

def reset():
    global counter
    global total_stops
    global success
    if timer.is_running():
        timer.stop()
        counter = 0
        total_stops = 0
        success = 0
    else: 
        counter = 0    
        total_stops = 0
        success = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter+=1
    #print(counter)
timer = simplegui.create_timer(100,timer_handler)

# define draw handler
def draw_handler(canvas):
    global counter
    canvas.draw_text(format(counter),(50,125), 45, 'White')
    canvas.draw_text(str(success)+"/"+str(total_stops),(150,25),25,'White')
    
# create frame
frame = simplegui.create_frame('Stopwatch',200,200)

# register event handlers
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

