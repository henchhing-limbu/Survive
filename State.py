class State:
  def __init__(self, scene='', optns = {}, final=False, dead=False):
    self.scene = scene          # this explains the situation
    self.finalState = final   # boolean saying if the state is final
    self.deadState = dead     # boolean saying if the state is dead state
    self.transitions = optns    # map to show transitions to different states
    self.optionToAlphabet = {}

  # sets scene value
  def setScene(self, scene):
    self.scene = scene
  # returns scene value
  def getScene(self):
    return self.scene

  # sets final state boolean value
  def setFinalState(self, val):
    self.finalState = val
  
  # sets dead stste boolean value
  def setDeadState(self, val):
    self.deadState = val
  
  # checks if the state is final state
  def isFinalState(self):
    return self.finalState
  
  # checks if the state is dead state
  def isDeadState(self):
    return self.deadState

  # maps choice to a state
  def makeTransition(self, choice, state):
    self.transitions[choice] = state
  
  # get transitions 
  def getTransitions(self):
    return self.transitions

  def setOptionToAlphabet(self, alphabet, option):
    self.optionToAlphabet[alphabet] = option

  # displys the current situation to the player, and gives him opportunity to choose
  def display(self):
    print(self.getScene())
    print("Now you have the following choices to make. Choose wisely")
    optionNum = 'A'
    for key in self.getTransitions().keys():
      print("%s. %s"  %(optionNum, key))
      optionNum = str(ord('A')+1)
      self.optionToAlphabet[optionNum] = key

