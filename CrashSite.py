from State import *

state0 = State()
state1 = State()
state2 = State()
state3 = State()
state4 = State()


state0.setScene("After spending countless hours at work, you decide that you deserve a vacation. You book a last minute flight to the fabulous Caribbean Island of the Bahamas. "
                "Unfortunately,  a horrendous storm comes in your plane’s path. The darkness of the sky and thunder frighten you and your fellow passengers. A way of extreme "
                "turbulence takes place and makes everyone aboard wonder how serious the storm is. Suddenly, the plane begins to fall out of the sky and you hear  the pilot "
                "say “we’re all going down”. From the massive drop in altitude and pure terror you blackout. You lose!\n"
                "You wake up on a deserted beach shore along with the remains of the plane crash. You quickly discover you’re the only survivor. You think to yourself, how "
                "will you survive?")
state1.setScene("You go to explore the right side of the island and you discover that despite you are the only plane crash survivor on a deserted island, you are not alone. "
                "In the distance, you notice that there is a dingy looking man nearby what looks to be his shelter. He doesn’t see you as you cautiously move in his direction.")
state2.setScene("You now go to the left side of the island to explore. Despite your growing hunger, you find a large supply of wood. ")
state3.setScene("While the island man leaves his home, you enter in and look around. You see mostly junk but quickly land your eyes on what appears to be a makeshif fishing rod. "
                "You take it as you quickly escape the left side of the island before the island man comes back.\n[Fishing unlocked: You can now go fishing in suitable location.]")
# TODO: Fishing Skill needs to be added to the player skills array
state4.setScene("The strange island man hears your steps as you move closer to him and turns around. To your surprise he rapidly turns around in a dramatic fashion and runs to you. "
                "He grabs a hold of you before you can do anything and says ”Boy, am I glad to see you”. The both of you explain how you got stuck on the island and soon become "
                "friends. The island man shares his shelter with you and now you have a new home and a friend. [Communication Skill Unlocked: You can now persaude people to benefit you]")
# TODO: Communication skill needs to be added to the player skills array

state0.makeTransition("Explore the left side of the island", state1)
state0.makeTransition("Explore the right side of the island", state2)

state1.makeTransition("Secretly enter his home", state3)
state1.makeTransition("Make him friend", state4)

print("Runs this file")


                      
