from os import system
import us
import random

## pip install us

states = us.states.STATES
tz_dict = {
    "America/Chicago" : "Central Time",
    "America/Anchorage" : "Alaska Time",
    "America/Phoenix" : "Mountain TIme",
    "America/Los_Angeles" : "Pacific Time",
    "America/Denver" : "Mountain Time",
    "America/New_York" : "Eastern Time",
    "Pacific/Honolulu" : "Hawaii-Aleutian Time",
    "America/Indiana/Indianapolis" : "Eastern Time",
    "America/North_Dakota/Center" : "Central Time"
}


print("\n\nWelcome to States Hangman!\n")
print("You will be given a blank and need to guess letters that could be in the mystery state's name.")
print("You will have 3 lives, with 1 life being used for each guessed letter that is not in the state")
print("You can also use up a life to get a hint about the state your guessing by using /hint.")
print("Use /stop to end the game at any time.")
print("Alrighty, good luck!\n")


def lifv(n):
    if n == 1:
        return "life"
    else:
        return "lives"


def vowell(n):
    if n == 1:
        return "vowel"
    else:
        return "vowels"


def randHint(st, hint):
    ## 1 - time zone
    ## 2 - capital
    ## 3 - vowels
    ## 4 - statehood year
    if hint == 1:
        tz = tz_dict[st.capital_tz]
        print("This state's main time zone is " + tz + ".")
    elif hint == 2:
        letter = st.capital[0].lower()
        print("This state's capital starts with the letter " + letter + ".")
    elif hint == 3:
        vowel_count = 0
        vowels = ["a", "e", "i", "o", "u"]
        for letter in st.name.lower():
            if letter in vowels:
                vowel_count += 1
        print("This state has " + str(vowel_count) + " " + vowell(vowel_count) + " in its name.")
    else:
        st_year = str(st.statehood_year)
        print("This state gained its statehood in the year " + st_year + ".")
    pass


while True:
    lives = 3
    ## lives cannot be greater than 4 due to only 4 hints
    possible_hints = [1,2,3,4]
    already_guess = []
    rand_state = random.choice(states)
    rand_name = rand_state.name
    rand_lower = rand_name.lower()
    hangman_blanks = ""
    for letter in rand_name:
        if letter == " ":
            hangman_blanks += " "
        else:
            hangman_blanks += "-"
    while True:
        guess = input("Guess a letter, or the whole state:\n" + hangman_blanks + "\n")
        if guess.lower() == rand_lower:
            print("Nice! You got it correct, with " + str(lives) + " " + lifv(lives) + " left to spare.")
            break
        elif guess.lower() in already_guess:
            print("That letter was already guessed.")
        elif (len(guess) == 1) and (guess.lower() in rand_lower) and (guess != " "):
            already_guess.append(guess.lower())
            hangman_list = list(hangman_blanks)
            hangman_blanks = ""
            for i in range(len(rand_lower)):
                if rand_lower[i] == guess.lower():
                    hangman_blanks += rand_name[i]
                else:
                    hangman_blanks += hangman_list[i]
            if not "-" in hangman_blanks:
                print("Good job, you figured it out. The state was " + rand_name + ".")
                break
            else:
                print("Nice guess!")
        elif guess.lower() == "/hint":
            if lives == 1:
                print("You don't have enough lives to do that!")
            else:
                rand_hint = random.choice(possible_hints)
                possible_hints.remove(rand_hint)
                lives -= 1
                randHint(rand_state, rand_hint)
                print("You have " + str(lives) + " " + lifv(lives) + " remaining.")
        elif guess.lower() == "/stop":
            quit()
        else:
            lives -= 1
            print("Good guess, but that isn't a letter in the state, or the guess was not correct.")
            if lives == 0:
                print("Looks like you're all out of lives. The correct answer was " + rand_name + ".")
                break
            else:
                print("You have " + str(lives) + " " + lifv(lives) + " remaining.")
    if input("If you would like to play again, type \"yes\"\n").lower() != "yes":
        break
