# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Insert your solution for RPSLS here
def name_to_number(name):
    """
    this converts the name chose by player to number for calculation
    """
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Invalid!Enter any one of the following: rock,Spock,paper,lizard,scissors"
    

def number_to_name(number):
    """
    this converts the randomly generated number by the computer to names
    """

    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        "Invalid ! Enter a number from 0 to 4"

def rpsls(player_choice):
    """
    this is the main step that calculates and find the winner and loser
    """
    
    print "Player chooses "+ player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)

    print "Computer chooses "+ comp_choice

    result = (comp_number - player_number) % 5

    if result==1 or result==2:
        print "Computer wins!"
    elif result==3 or result==4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
    print ''

     
    
# handler for input field
def get_guess(guess):
    
    # validate input
    if not (guess == "rock" or guess == "Spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
