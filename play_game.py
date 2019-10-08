# encoding=utf8
"""Functions that plays the game."""
from CreateGame import *
from State import *
from crash_site import *
from intro import *
from Jungle import *

startStates = [introState0, crashState0]
def introduction():
    """
    Displays introductory message and prompts the user to either start or end 
    the game.
    """
    print(
            "*****Welcome to Survive!*****\n\nThis is a choice based survival "
            "game where you need to make right choices to survive in this "
            "unknown island\n")
    userInput = input("To start game, press 1\nTo Exit game, press 0\n")
    if (userInput == '1'):
        print("Starting the game\n")
        return
    elif (userInput == '0'):
        quit()
    else:
        print("Please provide valid input")
        introudction()

def quit():
    """Exits the program."""
    print("Exiting the game\n")
    exit()

def playStage(startState, playerSkills, otherSkills):
    """Play the game until the win state or dead state is reached."""
    state = startState
    # This is where the flow of game will occur
    while (state):
        state.display()
        # Check whether the state is final or dead state.
        if state.isFinalState():
            return True
        elif state.isDeadState():
            return False

        # Updating skills if certain scenarios are reached.
        if state == crashState4:
            playerSkills.communication = True
            otherSkills.add("Communication")
        elif state == crashState3:
            playerSkills.fishing = True
            otherSkills.add("Fishing")
        elif state == crashState5:
            playerSkills.fishing = True
            otherSkills.add("Fishing")
        
        transition = state.getTransitions()

        alphabets = state.getAlphabetToOption()
        if 'E' in transition:   # Epsilon transition
            state = transition['E']
        else:
            # Make transition to another state based on user input.
            while True:
                userChoice = input("\nEnter option A or B\n")
                if userChoice not in 'AB':
                    print("Please enter a valid input\n")
                    continue
                
                nextState = transition[alphabets[userChoice]]
                if (nextState.getSkillNeeded() == '') or (
                        nextState.getSkillNeeded() in otherSkills):
                    print(state.getSkillNeeded())
                    state = transition[alphabets[userChoice]]
                    break
                else:
                    print(
                            "\nSorry you don't have %s skill yet!\n\nChoose "
                            "some other option" %state.getSkillNeeded())
  
# plays each stages
# @param1 list of start states of each stage
def playStages(startStates):
  playerSkills = Skills()
  otherSkills = set()
  stage = 1
  for startState in startStates:
    print("\n***** Stage %d *****" %stage)
    if playStage(startState, playerSkills, otherSkills):
      print("\nCongratulations! You passed stage %d" %stage)
    else:
      if lostStage():
        playStages(startStates)
      else:
        return False
    stage += 1
  JungeScene(playerSkills)
  return True

def lostStage():
    """Display loss message and prompt user input to restart or end game."""
    print("\n*****  You lost the game.   *****\n***** Bettur Luck Next Time"
            "*****\n")
    while (True):
        userInput = input(
                "Do you want to restart the game?\nPress 1 to restart the game"
                "\nPress 0 to exit the game\n")
        if userInput == '1':
            return True
        elif userInput == '0':
            return False
        else:
            print("\nPlease enter a valid input\n")
  
def startGame():
    """Starts the game."""
    introduction()
    if playStages(startStates):
        print("\nCongratulations! You survived. Do you want to play the game "
                "again?Press 1 to play again or 0 to exit")
        while (True):
            userInput = input("Press 1 to play again\nPress 0 to exit")
            if userInput == '1':
                startGame()
            elif userInput == '0':
                quit()
            else:
                print("Please enter a valid input!")
    else:
        quit()

startGame()
