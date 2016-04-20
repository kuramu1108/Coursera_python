import random

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    else:
        return 4

def rpsls(player_choice):
    p_num = name_to_number(player_choice)
    print "Player chooses", player_choice
    c_num = random.randrange(0, 5)
    print "Computer chooses", number_to_name(c_num)
    winner = None
    if p_num == c_num:
        winner = None
    elif p_num == 0 and (c_num == 3 or c_num == 4):
        winner = "Player"
    elif p_num == 1 and (c_num == 0 or c_num == 4):
        winner = "Player"
    elif p_num == 2 and (c_num == 1 or c_num == 0):
        winner = "Player"
    elif p_num == 3 and (c_num == 1 or c_num == 2):
        winner = "Player"
    elif p_num == 4 and (c_num == 3 or c_num == 2):
        winner = "Player"
    else:
        winner = "Computer"
    if winner is None:
        print "Player and Computer tie!"
    else:
        print winner, "wins!"
    print ""

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
