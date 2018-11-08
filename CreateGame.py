# TODO: This is where we need all parts (scenarios) of the game
# TODO: Can we come up with some interesting scenarios

from State.py import State

def createGame():
  print("Welcome!\nThis is where you will write the story of your surviva game");
  gameName = input("What is the name of your game?")
  numStates = int(input("How many scenarios do you want in your game?"))
  stateNum = 1

  gameGraph = {}
  while numStates != 0:
    if stateNum == 1:
      print("This is going to be your initial state.")
    break
  
createGame()


