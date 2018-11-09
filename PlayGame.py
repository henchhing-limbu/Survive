# This method simply introduces the user with game intro
def intro():
  print("*****Welcome to Survive!*****\n\nThis is a choice based survival game where you need to make right choices to survive in this unknown island\n")
  userInput = int(input("To start game, press 1\nTo Exit game, press 0\n"))
  if (userInput):
    print("Starting the game\n")
    startGame()
  else:
    print("Exiting the game\n")
    quit()


# TODO: Expecting graph of states in here
def startGame(startState):
  state = startState
  # This is where the flow of game will occur
  while (state):
    state.display()
    # checking if the state is final state or dead state
    # if it is, it's game over
    if state.isFinalState() or state.isDeadState():
      return
    transition = state.getTransitions()

    alphabets = state.getAlphabetToOption()
    if 'E' in transition:
      state = transitions['E']
    else:
      # expecting right input from the user
      while True:
        userChoice = str(input("Enter option A, B, C or D\n"))
        if userChoice in 'ABCD':
          break
        else:
          print("Please enter a valid input\n")
      state = transition[alphabets[userChoice]]