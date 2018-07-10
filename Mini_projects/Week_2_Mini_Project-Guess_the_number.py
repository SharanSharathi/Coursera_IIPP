# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


secret_number = random.randrange(0,100)
guess_remain = 7
rang = 100
# helper function to start and restart the game
def new_game():
    global secret_number, guess_remain, rang
    print('New game. Range is from 0 to '+str(rang))
    
    if(rang == 100):
        guess_remain = 7
    elif(rang == 1000):
        guess_remain =10
    
    
    print('The number of remaining guesses is '+str(guess_remain))
    secret_number = random.randrange(0,rang)
    print('')

# define event handlers for control panel
def range100():
    global secret_number, guess_remain, rang
    secret_number = random.randrange(0,100)
    rang = 100
    new_game()
 

def range1000():
    global secret_number, guess_remain, rang
    secret_number = random.randrange(0,1000)
    rang = 1000
    new_game()
    
 
    
def input_guess(guess):
    global secret_number, guess_remain, rang
    
    
    if(int(guess) > rang or int(guess)< 0):
        print("Number out of range 0 to " + str(rang))
        new_game()
        
    print('Guess was ' + str(guess))
    guess_remain -= 1
    
    print('Number of guess remaining guesses is ' + str(guess_remain))
   
    if(guess_remain == 0):
        print('You ran out of guesses.   The number was '+ str(secret_number) +'\n')
        new_game()
    
    elif(secret_number == int(guess)):
        print('Correct!\n')
        new_game()
    elif(secret_number > int(guess)):
        print('Higher!\n')
    elif(secret_number < int(guess)):
        print('Lower!\n')
       
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)
frame.set_canvas_background('blue')
frame.add_button('Range is [0,100)', range100,200)
frame.add_button('Range is [0,1000)', range1000,200)
frame.add_input('Enter a guess', input_guess,200)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
