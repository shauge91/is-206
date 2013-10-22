from sys import exit

def forest():
    print "You are in a forest"
    print "It is so dark, you can't see a thing. Suddently you hear a sound. It is a monster!"
    print "What do you do? hide or run"
    run_fast = False

    while True:
        next = raw_input("> ")
        if next == "hide":
            dead("The monster finds you and kills you")
            run_fast = True
        elif next == "run":
            print "You run back to the crossroad and choose the other road"
            harbor()
        else:
            print "I got no idea what that means."


def harbor():
    print "You are in the harbor"
    print "An old pirate lives in a boat"
    print "The pirates tries to rob you"
    print "What are you going to do? Run, push him or stand still"
    pirate_move = False

    while True:
        next = raw_input("> ")
        if next == "run":
            dead("The pirates parrot attacks you. You die.")
        elif next == "stand still" and not pirate_move:
            dead("The pirate approach you and puts a bullet through your head.")
            pirate_move = True
        elif next == "push him":
            print "The pirate falls into the water and drowns"
            win("")
        else:
            print "I got no idea what that means."


def dead(why):
    print why, "Moron!"
    exit(0)
    
def win(why):
    print why, "YOU WON! YOU ROCK"
    exit(0)

def start():
    print "You are at a cross road."
    print "Which way do you take?"
    print "Left or right?"

    next = raw_input("> ")

    if next == "left":
        forest()
    elif next == "right":
        harbor()
    else:
        dead("You get lost in the wilderness and starve to death")


start()