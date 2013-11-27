from sys import exit

def win():
    print "You won"
    print "Congrats"
    exit(0)
    
    
def castle():
    print "At last you reach the castle."
    print "When you try to enter, the evil dragon appears."
    print "What do you do? Fight or run?"

    grab_axe = True

    while True:
        next = raw_input("> ")

        if next == "run":
            dead("The dragon kills you")
        elif next == "fight" and not grab_axe:
            dead("The dragon kills you. You didn't have an axe")
            grab_axe = True
        elif next == "fight" and grab_axe:
            win()
        else:
            print "What did you mean?"


def river():
    print "The river gets wider"
    print "It is obvious that you need to turn around"
    print "Behind a tree you see an abondoned axe"
    print "You grab the axe and then turn around (turn around)"
    grab_axe = True

    while True:
        next = raw_input("> ")

        if next == "turn around" and grab_axe:
            cross()
        else:
            dead("You fell into the river")


def cross():
    print "The river gets narrower and narrower"
    print "Make your horse jump across the river (jump)"


    next = raw_input("> ")

    if "jump" in next:
        castle()
    else:
	    dead("You drown because you didn't jump over")


def dead(why):
    print why, "Horrible!! You died!"
    exit(0)

def start():
    print "You are the Prince of Sibiria."
    print "You are going to save a captured princess who is held hostage by the evil dragon"
    print "in his big fortress in the deep forest of Cappucia."
    print "You have a long way ahead of you, and you choose to bring your horse Golden eye."
    print "When you reach a river, to wide for Golden eye to jump across you must make a choice."
    print "Do you follow the river left or right in your search for a better place to cross? (left or right)"

    next = raw_input("> ")

    if next == "left":
        river()
    elif next == "right":
        cross()
    else:
        dead("You didn't make up your mind and starved to death")


start()