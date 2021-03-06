import us
import random

## pip install us

states = us.states.STATES
states_lower = [x.name.lower() for x in states]


## Which state has the capital ""
def capitalGame():
    score = 0
    tally = 0
    while True:
        rand_state = random.choice(states)
        inp = input("What is the capital of " + rand_state.name + "?\n")
        if inp == "/stop":
            break
        elif inp.lower() == rand_state.capital.lower():
            score += 1
            tally += 1
            print("Yep, that's correct!")
        else:
            tally += 1
            print("That is incorrect. The correct answer is " + rand_state.capital + ".")
    print("Your final score was " + str(score) + ".")
    if tally != 0:
        score_percent = round(100*(score/tally), 2)
        print ("You correctly answered " + str(score_percent) + r"%" +  " of the questions.")
    pass

## In what year did "" get its statehood?
def statehoodYearGame():
    score = 0
    tally = 0
    while True:
        rand_state = random.choice(states)
        inp = input("What year did " + str(rand_state) + " gain statehood?\n")
        ans = str(rand_state.statehood_year)
        if inp == "/stop":
            break
        elif inp == ans:
            score += 1
            tally += 1
            print("Correct!")
        else:
            tally += 1
            print("Sorry, the correct answer was " + ans + ".")
    print("Alright, your final score was " + str(score) + "!")
    if tally != 0:
        score_percent = round(100*(score/tally), 2)
        print ("You correctly answered " + str(score_percent) + r"%" +  " of the questions.")
    pass


## What state starts with "" and ends with ""
def spellingGame():
    score = 0
    tally = 0
    while True:
        randomState = random.choice(states_lower)
        first_l = randomState[0]
        last_l = randomState[-1]
        question = "What is a state that starts with the letter \"" + first_l
        question += "\" and ends with the letter \"" + last_l + "\"?\n" 
        stateInput = input(question)
        if stateInput == "/stop":
            break
        else:
            bool1 = (first_l == stateInput[0].lower()) and (last_l == stateInput[-1].lower())
            bool2 = stateInput.lower() in states_lower
            tally += 1
            if not bool2:
                print("That isn't a state!")
            elif not bool1:
                print("That doesn't match!")
            else:
                print("Correct!")
                score += 1
    print("Not bad! Your final score was " + str(score) + "!")
    if tally != 0:
        score_percent = round(100*(score/tally), 2)
        print ("You successfuly answered " + str(score_percent) + r"%" +  " of the questions.")
    pass


## Name the abbreviation of this state:
def abbrGame():
    score = 0
    tally = 0
    while True:
        currentState = random.choice(states)
        userInput = input("What is the abbreviation of " + currentState.name + "? \n")
        answer = currentState.abbr
        if userInput == "/stop":
            print("Alright, stopping the game now.")
            break
        elif userInput.upper() == answer:
            score += 1
            tally += 1
            print("Correct! Your score is now " + str(score) + ".")
        else:
            print("Not quite, the correct answer was " + answer + ".")
            tally += 1
    print("Not bad! Your final score was " + str(score) + "!")
    if tally != 0:
        score_percent = round(100*(score/tally), 2)
        print ("You got " + str(score_percent) + r"%" +  " of the questions correct.")
    pass

print("Welcome to States Trivia! Quiz your knowledge of the US States.")
print("Make a selection from the following options by typing the corresponding number.")
print("Use /stop to end the game.")
print("")
print("(1) Capitals Quiz")
print("(2) Year of Statehood Quiz")
print("(3) States Spelling Quiz")
print("(4) Abbreviations Quiz")
print("You can use /list to view these again.")
print("")

while True:
    selection = input("Which game would you like to play? ")
    if selection == "1":
        capitalGame()
        if input("Would you like to keep playing? (Y/N) ").lower() != "y":
            break
    elif selection == "2":
        statehoodYearGame()
        if input("Would you like to keep playing? (Y/N) ").lower() != "y":
            break
    elif selection == "3":
        spellingGame()
        if input("Would you like to keep playing? (Y/N) ").lower() != "y":
            break
    elif selection == "4":
        abbrGame()
        if input("Would you like to keep playing? (Y/N) ").lower() != "y":
            break
    elif selection == "/list":
        print("(1) Capitals Quiz")
        print("(2) Year of Statehood Quiz")
        print("(3) States Spelling Quiz")
        print("(4) Abbreviations Quiz")
    else:
        print("That's not a valid input. Type either 1, 2, 3, or 4.")
