class State:
  # constructor
  def __init__(self, scene=None, optns = None, final=False, dead=False):
    if scene:
      self.scene = scene          # this explains the situation
    else:
      self.scene = ''
    self.finalState = final       # boolean saying if the state is final
    self.deadState = dead         # boolean saying if the state is dead state
    if optns:
      self.transitions = optns    # map to show transitions to different states
    else:
      self.transitions = {}
    self.optionToAlphabet = {}    # maps options to alphabets

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
  
  def getAlphabetToOption(self):
    return self.optionToAlphabet

  # displys the current situation to the player, and gives him opportunity to choose
  def display(self):
    print("%s" %self.getScene())
    print("Now you have the following choices to make. Choose wisely")
    if self.isDeadState() or self.isFinalState() or 'E' in self.getTransitions():
      return
    optionNum = 'A'
    for key in self.getTransitions().keys():
      print("%s. %s"  %(optionNum, key))
      self.setOptionToAlphabet(optionNum, key)
      optionNum = chr(ord('A')+1)

