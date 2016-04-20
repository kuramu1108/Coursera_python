# Mini-project #6 - Blackjack

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# load card sprite - 950x392 - source: jfitz.com
CARD_SIZE = (73, 98)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

# initialize global variables
in_play = False
outcome = ""
game_notice = ""
score = 0

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", self.suit, self.rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(self.rank)), CARD_SIZE[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_SIZE[0] / 2, pos[1] + CARD_SIZE[1] / 2], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        s = ""
        for card in self.cards:
            s += str(card) + " "
        return s

    def add_card(self, card):
        self.cards.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if don't bust
    def get_value(self):
        value = 0
        has_A = False
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_A = True
        if not has_A:
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                return value

    def busted(self):
        if self.get_value() > 21:
            return True
        else:
            return False

    def return_card(self):
        back =  self.cards
        self.cards = []
        return back

    def draw(self, canvas, p):
        for card in self.cards:
            card.draw(canvas, p)
            p[0] += CARD_SIZE[0]


# define deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    # add cards back to deck and shuffle
    def shuffle(self, pHand, dHand):
        self.cards.extend(pHand.return_card())
        self.cards.extend(dHand.return_card())
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


#define callbacks for buttons
def deal():
    global outcome, in_play, score
    if in_play:
        score -= 1
    deck.shuffle(player, dealer)
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = ""
    in_play = True

def hit():
    global game_notice, outcome, in_play, score
    if in_play:
        player.add_card(deck.deal_card())
        if player.busted():
            outcome = "Player busted, you lose"
            game_notice = "New Deal?"
            in_play = False
            score -= 1
        else:
            game_notice = "Hit or Stand?"

def stand():
    global game_notice, outcome, in_play, score
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.busted():
            outcome = "Dealer busted, you win"
            score += 1
        elif dealer.get_value() >= player.get_value():
            outcome = "you lose"
            score -= 1
        else:
            outcome = "you win"
            game_notice = "New Deal?"
            score += 1
        in_play = False

def draw(canvas):
    global in_play
    dealer.draw(canvas, [100, 200])
    if in_play:
        CARD_BACK_CENTER = [CARD_BACK_SIZE[0] / 2, CARD_BACK_SIZE[1] / 2]
        FIRSTCARD_POS = [100 + CARD_SIZE[0] / 2, 200 + CARD_SIZE[1] / 2]
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, FIRSTCARD_POS, CARD_BACK_SIZE)
    player.draw(canvas, [100, 400])
    canvas.draw_text("Blackjack", [100, 100], 35, "Black")
    canvas.draw_text("Dealer", [100, 150], 25, "Black")
    canvas.draw_text("Player", [100, 350], 25, "Black")
    canvas.draw_text(outcome, [300, 150], 25, "Black")
    canvas.draw_text(game_notice, [300, 350], 25, "Black")
    canvas.draw_text("Score: " + str(score), [500, 50], 25, "Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
dealer = Hand()
player = Hand()
deck = Deck()
deal()
# get things rolling
frame.start()
