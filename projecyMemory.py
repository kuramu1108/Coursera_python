try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

WEIGHT = 800
HEIGHT = 100
# helper function to initialize globals
def new_game():
    global deck
    deck = range(0, 8) + range(0, 8)
    random.shuffle(deck)
    global exposed
    exposed = [False for card in deck]
    global pick_1
    global pick_2
    global state
    state = 0
    global turn
    turn = 0


# define event handlers
def mouseclick(pos):
    global state
    global turn
    global pick_1
    global pick_2
    index = pos[0] // (WEIGHT / len(deck))
    if not exposed[index]:
        exposed[index] = True
        if state == 0:
            state = 1
            pick_1 = index
        elif state == 1:
            state = 2
            pick_2 = index
        else:
            state = 1
            if deck[pick_1] != deck[pick_2]:
                exposed[pick_1] = False
                exposed[pick_2] = False
            pick_1 = index
            turn += 1
            label.set_text("Turns = " + str(turn))

# cards are logically 50x100 pixels in size
def draw(canvas):
    count = 0
    for card in deck:
        if exposed[count]:
            canvas.draw_text(str(card), [count * 50 + 22 , 65], 30, 'Red')
        else:
            canvas.draw_polygon([[count * 50, 0], [count * 50, 100], [count * 50 + 50, 100], [count * 50 + 50, 0]], 5, "Black", "Green")
        count += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WEIGHT, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
