# encoding=utf8
from State import *
introState0 = State()
introState1 = State()
introState2 = State()
introState3 = State()
introState4 = State()

introState3.setDeadState(True)
introState4.setFinalState(True)

introState0.setScene("After spending countless hours at work, you decide that "
                     "you deserve a vacation. You book a last minute flight to "
                     "the fabulous Caribbean Island of the Bahamas. Unfortunately"
                     ",  a horrendous storm comes in your plane’s path. The airline"
                     "needs one more volunteer passenger to sit in the emergency exit"
                     "and to help out if needed.")
introState1.setScene("You volunteer to sit in the emergency exit and listen to "
                     "all instructions from the flight crew. You now know what "
                     "to do in case of an emergency.")
introState2.setScene("You sit in your normal seat and relax for the flight. You "
                     "fall asleep before the plane takes off and do not get to listen"
                     "to instructions from the flight crew.")
introState3.setScene("The darkness of the sky and thunder frighten you and your"
                     " fellow passengers. A way of extreme turbulence takes "
                     "place and makes everyone aboard wonder how serious the "
                     "storm is. Suddenly, the plane begins to fall out of the "
                     "sky and you hear  the pilot say “we’re all going down”. "
                     "From the massive drop in altitude and pure terror you "
                     "blackout")
introState4.setScene("The darkness of the sky and thunder frighten you and your"
                     "fellow passengers. A way of extreme turbulence takes "
                     "place and makes everyone aboard wonder how serious the "
                     "storm is. Suddenly, the plane begins to fall out of the "
                     "sky and you hear  the pilot say “we’re all going down”. "
                     "You are trained and prepared to handle the situation, but "
                     "the turbulence is just too strong! You manage to save "
                     "yourself from injury.")

introState0.makeTransition("Volunteer to sit in the emergency exit", introState1)
introState0.makeTransition("Let someone else do the job", introState2)
introState1.makeTransition('E', introState4)
introState2.makeTransition('E', introState3)









                     
                     
                     
                     
