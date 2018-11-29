class State2:
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

  def isOptions(self):
    return len(self.optionToAlphabet)

  def getOptions(self):
    return self.optionToAlphabet

  # displys the current situation to the player, and gives him opportunity to choose
  def display(self):
    print(self.getScene())
    print("Now you have the following choices to make. Choose wisely")
    optionNum = 'A'
    for key in self.getTransitions().keys():
      print("%s. %s"  %(optionNum, key))
      optionNum = str(ord('A')+1)
      self.optionToAlphabet[optionNum] = key

class Skills():
    def __init__(self,com = False, fish = False, nav= False):
        self.communication = com
        self.fishing = fish
        self.navigation = nav
    def set_communication(self):
        self.communication = True

    def set_fishing(self):
        self.fishing = True

    def set_navigation(self):
        self.navigation = True

    def get_communication(self):
        return self.communication

    def get_fishing(self):
        return self.fishing

    def get_navigation(self):
        return self.navigation

def makeaChoice(option, transit, curr_state):
    for options in curr_state.getOptions().values():
        print(options)    
    choice = input('Enter A or B: ')
    choice = choice.upper()
    choice = str(choice)
    # transit = curr_state.getTransitions()

    for options,states in transit.items():
        if str(choice) == options:
            curr_state = states
            return curr_state
# from State.py import State

def JungeScene(player):
    JungleS4 = State2(' You avoid this man and continue to explore the temple area on your own. You find some materials that look like they can be used to build a boat.',{},True,False)
    JungleS6 = State2('The man leads you through the temple to the explorers’ campsite. Luck for you, you catch them before they leave the island and they agreed to take you with them. You win!',{},True,False)
    JungleS2 = State2(' A predator in the distance causes all the animals to flee in fear. A stampede is now coming your way and you cannot out run it. You die.',{},False,True)
    JungleS1= State2('You see a herd of animals by a river. ', {'E': JungleS2}, False,False)
    JungleS7 = State2('You begin to get angry and the man can tell. Your anger scares the old man and he now believes you are a threat. He calls his friends and they take you captive and you are never seen again. You lose!', {},False,True)
    JungleS5 = State2('You speak to the man and he believes he has seen you before. The man mistakes you for  one of the explorers he guided around the temple a few days ago. Despite your efforts, the man still believes that you are one of the explorers.',{'A': JungleS6, 'B': JungleS7},False,False)
    JungleS3 = State2(' You think following the tracks of a mysterious animal is a bad idea so you continue on in the opposite direction of the tracks. You find yourself stumbling upon the ruins of an ancient temple. As you approach the entrance of the temple, far off in the distance you see an old man who hasn’t noticed your presence yet.',{'A': JungleS4,'B': JungleS5},False,False)

    JungleS0 = State2('You go off to explore more of the island. After wandering miles in the island heat you see a jungle in the distance. You enter into the shade of the jungle to escape the smoldering heat and you happen to look down towards your feet. You notice that there are some type of animal tracks on the ground.',{'A': JungleS1,'B': JungleS3},False,False)



    #Set option A or B to optionToAlphabet for each state that has one
    JungleS0.setOptionToAlphabet('A','A - You follow the tracks')
    JungleS0.setOptionToAlphabet('B','B - You go in the opposite direction of the tracks')

    JungleS3.setOptionToAlphabet('A','A - You avoid the man and explore the temple')
    JungleS3.setOptionToAlphabet('B','B - You go meet the man in the temple')

    JungleS5.setOptionToAlphabet('A','A - I see you have a communication skill would like to use it?')
    JungleS5.setOptionToAlphabet('B', 'B - Would not like to use it ')
   
    curr_state = JungleS0

    JungleS7.setDeadState(True)
    # while not curr_state.isFinalState():
    while True:
        option = curr_state.getOptions()
        transit = curr_state.getTransitions()
        if curr_state.finalState:
            print("This is final state")
            print(curr_state.getScene())
            userchoice = input('Would you like to start over at the Island? A - Yes , B - No ')
            print()
            userchoice = str(userchoice.upper())
            if userchoice == 'A':
                curr_state = JungleS0
            else: 
                print('Game Over')
                quit()

        if curr_state.deadState:
            print("This is dead state")
            print(curr_state.getScene())
            print()
            userchoice = input('Would you like to start over at the Island? A - Yes , B - No ')
            print()
            userchoice = str(userchoice.upper())
            if userchoice == 'A':
                curr_state = JungleS0
            else: 
                print('Game Over')
                quit()

        if curr_state == JungleS5:
            print("The last statge entered here JungleS5")
            if player.get_communication():
                curr_state =  makeaChoice(option,transit,curr_state)
            else:
                curr_state = JungleS7

        if transit:
            print("has transitions")
            print(curr_state.getScene())
            print()

            if len(option) > 1:
                print("Dead state value ", curr_state.deadState)
                print("Entered this useless place")
                curr_state = makeaChoice(option,transit,curr_state)
            
            else:
                print(curr_state.getScene())
                print()
                for options, states in transit.items():
                    if options == 'E':
                        print("This is epsilon transition")
                        curr_state = states
                
        else:
            print("There is no transition")
            for options, states in transit.items():
                 if options == 'E':
                    curr_state = states
    print(curr_state.getScene())
