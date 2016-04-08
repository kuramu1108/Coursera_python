# Mini-project #6 - Blackjack

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

defaultRange = [0, 100]
inPlay = False

def new_game():
    global answer, remainGuess, inPlay
    inPlay = True
    answer = random.randrange(defaultRange[0], defaultRange[1])
    remainGuess = int(math.ceil(math.log(defaultRange[1], 2)))
    print "New game, Range is from", defaultRange[0], "to", defaultRange[1]
    print "Number of remaining guesses is", remainGuess, "\n"

# define event handlers for control panel
def range100():
    global defaultRange
    defaultRange = [0, 100]
    new_game()

def range1000():
    global defaultRange
    defaultRange = [0, 1000]
    new_game()

def input_guess(inp):
    global remainGuess, inPlay
    if inPlay:
        try:
            guess = int(inp)
        except:
            print "Invalid input"
        print "Guess was", guess
        remainGuess -= 1
        print "Number of Remaining guesses is", remainGuess
        if guess == answer:
            print "Correct\n"
            inPlay = False
        elif guess > answer:
            print "Lower\n"
        elif guess < answer:
            print "Higher\n"

        if remainGuess == 0 and answer != guess:
            print "Game over, the answer is", answer
            print "Please start a new game\n"
            inPlay = False
    else:
        print "Please Start a new Game\n"


# create frame
frame = simplegui.create_frame("Guessing Number", 220, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Guess:", input_guess, 200)
frame.start()
# call new_game
new_game()


# always remember to check your completed program against the grading rubric
