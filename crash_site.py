from State import *

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

crashState9.setDeadState(True)
crashState10.setDeadState(True)
crashState7.setFinalState(True)



crashState0.setScene("\n\nYou wake up on a deserted beach shore along with the remains of the plane crash. You quickly discover that you’re the only survivor. \nYou think to yourself, how will you survive?")

crashState1.setScene("\n\nYou go to explore the right side of the island and you discover that despite being the only plane crash survivor on a deserted island, \nyou are not alone. "
                "In the distance, you notice that there is a dingy looking man nearby what looks to be his shelter. \nHe doesn’t see you as you cautiously move in his direction.")

crashState2.setScene("\n\nYou now go to the left side of the island to explore. Despite your growing hunger, you find a large supply of wood. ")

crashState3.setScene("\n\nWhile the island man leaves his home, you enter in and look around. You see mostly junk but quickly land your eyes on what appears to be a \n"
                     "makeshift fishing rod. You take it and quickly escape the left side of the island before the island man comes back.\n[Fishing unlocked: You "
                     "can now go fishing in a suitable location.]")
# TODO: Fishing Skill needs to be added to the player skills array

crashState4.setScene("\n\nThe strange island man hears your steps as you move closer to him and turns around. To your surprise, he rapidly turns around in a dramatic fashion and runs to you. \n"
                "He grabs a hold of you before you can do anything and says ”Boy, am I glad to see you”. The both of you explain how you got stuck on the island and soon become \n"
                "friends. The island man shares his shelter with you and now you have a new home and a friend. \n[Communication Skill Unlocked: You can now persuade people to benefit you]\n")
# TODO: Communication skill needs to be added to the player skills array

crashState8.setScene("\n\nYou begin your journey to find berries and lucky for you are successful in your search. While you're gathering your berries you hear the bush in front of you rattle \n"
                    "louder and louder. Suddenly a wolf comes out of the bush.\n")
                     
crashState9.setScene("\n\nYou new friend teaches you to hunt and you become good, but…not that good. You don’t realize this and go off hunting on your own. \nYour naivety causes you to get "
                     "killed by your lunch.\n")

crashState10.setScene("\nTrying to save yourself, you run away from the wolf as fast as you can. However, you are no match for the beast. You get eaten by the beast.\n")
# TODO: hunting skills gained

crashState5.setScene("\nYou put up a brave fight against the wolf. Despite getting injured, you kill the wolf. You return to the place where you made fire\n")
                     
crashState6.setScene("\nYou take the wood you just found and build a fire. Now that you’re warm, you decide to find food.\n")

crashState7.setScene("\nYou are on your way to go fishing on the beach.\n")

crashState0.makeTransition("Explore the left side of the island", crashState1)
crashState0.makeTransition("Explore the right side of the island", crashState2)

crashState1.makeTransition("Secretly enter his home", crashState3)
crashState1.makeTransition("Make him friend", crashState4)

crashState2.makeTransition("Build a Fire", crashState6)

crashState3.makeTransition('E', crashState2)

crashState4.makeTransition("Learn to hunt", crashState9)
crashState4.makeTransition("Explore the rest of island", crashState2)

crashState6.makeTransition("Go Fishing", crashState7)
crashState6.makeTransition("Go pick some berries", crashState8)

crashState8.makeTransition("Run away", crashState10)
crashState8.makeTransition("Pick up the wood near you, and fight the wolf", crashState5)

                    








                      
