from CreateGame import *
from State import *
from crash_site import *
from intro import *
from Jungle import *
from collections import deque

startStates = [introState0, crashState0]
# This method simply introduces the user with game intro
def introduction():
  print("*****Welcome to Survive!*****\n\nThis is a choice based survival game where you need to make right choices to survive in this unknown island\n")
  userInput = int(input("To start game, press 1\nTo Exit game, press 0\n"))
  if (userInput == 1):
    print("Starting the game\n")
    return
  elif (userInput == 0):
    print("Exiting the game\n")
    quit()
  else:
    print("Please enter 1 or 0")
    introudction()


# TODO: Expecting graph of states in here
def playStage(startState, playerSkills, otherSkills, decisionQueue):
  state = startState
  # This is where the flow of game will occur
  while (state):
    print("\n%s" %state.display())
    # checking if the state is final state or dead state
    # if it is, it's game over
    if state.isFinalState():
      return True
    elif state.isDeadState():
      return False
    
    # updating communication skills
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
    if 'E' in transition:
      state = transition['E']
    else:
      while True:
        # expecting right input from the user
        while True:
          userChoice = str(input("\nEnter option A or B\n"))
          if userChoice in 'AB':
            break
          else:
            print("Please enter a valid input\n")
        nextState = transition[alphabets[userChoice]]
        decisionQueue.append(alphabets[userChoice])
        if (nextState.getSkillNeeded() == '') or (nextState.getSkillNeeded() in otherSkills):
          print(state.getSkillNeeded())
          state = transition[alphabets[userChoice]]
          break
        else:
          print("\nSorry you don't have %s skill yet!\n\nChoose some other option" %state.getSkillNeeded())
  
# plays each stages
# @param1 list of start states of each stage
def playStages(startStates, decisionQueue):
  playerSkills = Skills()
  otherSkills = set()
  stage = 1
  for startState in startStates:
    print("\n***** Stage %d *****" %stage)
    if playStage(startState, playerSkills, otherSkills, decisionQueue):
      print("\nCongratulations! You passed stage %d" %stage)
    else:
      if lostStage():
        playStages(startStates)
      else:
        return False
    stage += 1
  JungeScene(playerSkills)
  

  return True

# displays message saying the user lost
# returns True if the user wants to restart game else False
def lostStage():
  print("\n*****  You lost the game.   *****\n"
        "***** Bettur Luck Next Time *****\n")
  while (True):
    userInput = int(input("Do you want to restart the game?\nPress 1 to restart the game\nPress 0 to return to main menu"))
    if userInput == 1:
      return True
    elif userInput == 0:
      return False
    else:
      print("\nPlease enter a valid input")
  
  
def startGame():
  introduction()
  decisionQueue = deque()
  returnVal = playStages(startStates, decisionQueue)
  if returnVal:
    print("\nCongratulations! You survived. Do you want to play the game again?\nPress 1 to play again\n0 to exit")
    while (True):
      userInput = int(input("Press 1 to play again or 0 to exit"))
      if userInput == 1:
        startGame()
      elif userInput == 0:
        quit()
      else:
        print("Please enter a valid input!")
  else:
    userInput = int(input("\nGame over.\nDo you want to play the game again?\nPress 1 to play again\n0 to exit"))
    print(len(returnVal))


startGame()
