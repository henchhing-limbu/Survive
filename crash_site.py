# encoding=utf8
"""Creates State objects (scenarios) in the game."""
from State import *

# State objects that represents different stages (scenarios) in the game.
crashState0 = State()
crashState1 = State()
crashState2 = State()
crashState3 = State()
crashState4 = State()
crashState5 = State()
crashState6 = State()
crashState7 = State()
crashState8 = State()
crashState9 = State()
crashState10 = State()
crashState11 = State()

crashState9.setDeadState(True)
crashState10.setDeadState(True)
crashState7.setFinalState(True)
crashState11.setDeadState(True)

crashState0.setScene(
        "You wake up on a deserted beach shore along with the remains of the "
        "plane crash. You quickly discover you’re the only survivor. You "
        "think to yourself, how will you survive?")

crashState1.setScene(
        "You go to explore the right side of the island and you discover that "
        "despite you are the only plane crash survivor on a deserted island, "
        "you are not alone. In the distance, you notice that there is a dingy "
        "looking man nearby what looks to be his shelter. He doesn’t see you "
        "as you cautiously move in his direction.")

crashState2.setScene(
        "You now go to the left side of the island to explore. Despite your "
        "growing hunger, you find a large supply of wood. ")

crashState3.setScene(
        "While the island man leaves his home, you enter in and look around. "
        "You see mostly junk but quickly land your eyes on what appears to be "
        "a makeshif fishing rod. You take it as you quickly escape the left "
        "side of the island before the island man comes back.\n[Fishing "
        "unlocked: You can now go fishing in suitable location.]")
# TODO: Fishing Skill needs to be added to the player skills array

crashState4.setScene(
        "The strange island man hears your steps as you move closer to him and"
        " turns around. To your surprise he rapidly turns around in a dramatic"
        " fashion and runs to you. He grabs a hold of you before you can do "
        "anything and says ”Boy, am I glad to see you”. The both of you "
        "explain how you got stuck on the island and soon become friends. The "
        "island man shares his shelter with you and now you have a new home "
        "and a friend. [Communication Skill Unlocked: You can now persaude "
        "people to benefit you]")
# TODO: Communication skill needs to be added to the player skills array

crashState8.setScene(
        "You begin your journey to find berries and lucky for you are "
        "successful in your search.While you're gathering your berries you hear"
        " the bush in front of you rattle louder and louder.Suddenly a wolf "
        "comes out of the bush.")
                     
crashState9.setScene(
        "You new friend teaches you to hunt and you become good, but…not that "
        "good. You don’t realize this and go off hunting on your own. Your "
        "naivety causes you to get killed by your lunch.")

crashState10.setScene(
        "Trying to save yourself, you run away as fast as you can from the "
        "wolf. However, you are no match for the beast. You get eaten by the "
        "beast.")

crashState11.setScene("The berries were poisonous. You die!")

crashState5.setScene(
        "You put up a brave fight against the wolf. Despite getting injured, "
        "you kill the wolf.You return to the place where you made fire. On your"
        " way back you find a fishing rod") 
                     
crashState6.setScene(
        "You take the wood you just found and build a fire. Now that you’re "
        "warm, decide to find food.")

crashState7.setScene(
        "You are on your way to go fishing on the beach. After that you decide"
        " to go to the jungle.")

# Make transitions from one state to another state based on options.
crashState0.makeTransition("Explore the left side of the island", crashState1)
crashState0.makeTransition("Explore the right side of the island", crashState2)

crashState1.makeTransition("Secretly enter his home", crashState3)
crashState1.makeTransition("Make him friend", crashState4)

crashState2.makeTransition("Build a Fire", crashState6)
crashState2.makeTransition("You find some unknown berries. Eat it", crashState10)

crashState3.makeTransition('E', crashState2)

crashState4.makeTransition("Learn to hunt", crashState9)
crashState4.makeTransition("Explore the rest of island", crashState2)

crashState6.makeTransition("Go Fishing", crashState7)
crashState6.makeTransition("Go pick some berries", crashState8)
crashState7.setSkillNeeded("Fishing")

crashState8.makeTransition("Run away", crashState10)
crashState8.makeTransition("Pick up the wood near you, and fight the wolf", crashState5)

crashState5.makeTransition('E', crashState2)
