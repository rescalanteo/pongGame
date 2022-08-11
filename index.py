# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_pos = 200
paddle2_pos = 200
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2] # Returns the ball to the center of the field.
    
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = -random.randrange(2, 4)
        
    if direction == LEFT:
        ball_vel[0] = - random.randrange(2, 4)
        ball_vel[1] = - random.randrange(2, 4)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(1)
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # update ball
    ball_pos[0] += ball_vel [0]
    ball_pos[1] += ball_vel [1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2,"Red", "White")
    
    # collide and reflect off of upper hand side of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # collide and reflect off of lower hand side of canvas
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # determine whether GUTTER and ball collide 
            
    #Right GUTTER
    #if  ball_pos[0] >= WIDTH -(BALL_RADIUS + PAD_WIDTH):
        #ball_vel[0] = - ball_vel[0]
        #spawn_ball(LEFT)
        
    # Left GUTTER
    #if  ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        #ball_vel[0] = - ball_vel[0]
        #spawn_ball(RIGHT)
        
        
    # determine whether PADDLE and ball collide    
    
    # Right PADDLE
    if  ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):    
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += 0.1 * ball_vel[0]
            ball_vel[1] += 0.1 * ball_vel[1]
        else:
            spawn_ball(LEFT)
            score2 += 1
                       
    # Left PADDLE    
    if  ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):    
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += 0.1 * ball_vel[0]
            ball_vel[1] += 0.1 * ball_vel[1]
        else:
            spawn_ball(RIGHT)
            score1 += 1
    
    # update paddle's vertical position, keep paddle on the screen
    
    if ((paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT) and
        (paddle1_pos + paddle1_vel <= HEIGHT - 1 - HALF_PAD_HEIGHT)):
         paddle1_pos += paddle1_vel
            
    if ((paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT) and
        (paddle2_pos + paddle2_vel <= HEIGHT - 1 - HALF_PAD_HEIGHT)):
         paddle2_pos += paddle2_vel 
   
    # draw paddles
    
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Red")
    
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "Red")
        
    
    # draw scores
    canvas.draw_text(str(score1), (450, 40), 30, 'white', 'sans-serif')
    canvas.draw_text(str(score2), (150, 40), 30, 'white', 'sans-serif')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
        
        
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += 5
        
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= 5
        
        
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += 5
        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= 5

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("New Game", new_game, 100)


# start frame
new_game()
frame.start()
