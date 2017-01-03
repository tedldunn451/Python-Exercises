# Python 2.7.12
# 
# Author: Kristen Findley
# 
# Purpose: Python course drill 35 of 68 Nice/Mean Game

'''
def startNum():
    print(get_number())

def get_number():
    number = 12
    return number

def startName():
    print("Hello {}!".format(get_name()))

def get_name():
    name = raw_input("Enter your name: ") # Python 2 uses 'raw_input', Python 3 uses 'input'
    return name

def startInfo():
    f_name = "Kristen"
    l_name = "Findley"
    age = 26
    gender = "Female"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} year old {}.".format(f_name,l_name,age,gender))
'''

# initialize variables and call game setup
def start_game(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

# provide instructions for game and call game function
def describe_game(name):
    '''
        check if this is a new game or not,
        if it is, get the user's name.
        If it is not, thank the player for playing
        and continue playing the game.
    '''
    if name != "":
        print("\nThank you for playing {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize() # normalize user input
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.")
                    print("At the end of the game, your fate will be influenced by your actions.")
                    stop = False
    return name

# player chooses to be nice or mean and accumulates points
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m: ").lower()
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = nice + 1
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and abruptly storms off...")
            mean = mean + 1
            stop = False
        score(nice,mean,name) # pass the three variables to score

# score display
def show_score(nice,mean,name):
    print ("\n{}, you currently have {} nice and {} mean points.".format(name,nice,mean))

# tracking of score and consequences for winning or losing
def score(nice,mean,name):
    if nice > 5:
        win(nice,mean,name)
    if mean > 5:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

# consequences for winning
def win(nice,mean,name):
    print ("\nNice job {}, you win! \nEveryone loves you and you live in a palace!".format(name))
    again(nice,mean,name)

# consquences for losing
def lose(nice,mean,name):
    print ("\nToo bad {}. You weren't nice enough and now you live alone in a broken down van by the dump.".format(name))
    again(nice,mean,name)

# generate user input determining if they will play again or not
def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            stop = False
            exit()
        else:
            print ("\nPlease enter 'y' for YES and 'n' for NO...")

# reset the score for a new game with the same user
def reset(nice,mean,name):
    nice = 0
    mean = 0
    start_game(nice,mean,name)

if __name__ == "__main__":
    start_game()
