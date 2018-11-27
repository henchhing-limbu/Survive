# TODO: This is where we need all parts (scenarios) of the game
# TODO: Can we come up with some interesting scenarios

from State import *

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
  
state0 = State()
state1 = State()
state2= State()
state3 = State()
state0.setScene("You are in a deserted island. You are the only survivor")
state0.makeTransition("Explore right", state1)
state0.makeTransition("Explore left", state2)

state1.setScene("Found some firewood")
state1.makeTransition("Make Fire", state3)

state3.setScene("You are hungry")
state2.setScene("Found a survivor")
# making a map (making a transition) -> graph
