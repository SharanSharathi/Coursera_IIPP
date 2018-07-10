# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simplegui 

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if first_letter in ('aeiou'):
        rest_of_word = str(first_letter) + str(rest_of_word)
        first_letter = word[1]
        
    return(str(rest_of_word)+ str(first_letter) +"ay")

# Handler for input field
def get_input(latin):
    print(pig_latin(latin))

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)
frame.add_input("pig_latin",get_input,50)

# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


