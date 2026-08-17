'''
    author: Aditha Mansilu Ranawaka
    date: 10/8/2026
    version: 
    desciption: Heads or Tails game
'''
#---------------------libraries-------------------
import random 

#---------------------functions-------------------
"""
* validates user's name input
* checks length boundary and ensures only letters are entered
* loops until a valid input is entered
"""
def name_check(name):
    min_name=2 # minimum name length
    max_name=10 # maximum name length

    while True:
        if (len(name) >= min_name and len(name) <= max_name):# check if the name has a valid length
            if(name.isalpha): # check if the name only consists letters
                return name
        else:
            print('Your name has an invalid length')
            name = input ('Enter your name again between 2 and 10 letters: ')
        
"""
* validates the user's age
* checks that the age is a whole number and meets the minimum age boundary of 6
* use try and except to handle invalid datatypes without crashing
"""
def check_age():
    min_age=6 # minimum age requirement
    max_age=60 # maximum age requirement

    while(True):
        try:
            age = int(input('Enter your age in years:')) # check for numbers
            if( min_age <= age and age <=max_age): # boundary check for age requirements
                return age 
            else:
                age=int(input('Enter an age between 6 and 60:'))
        except:
            age = int(input('Enter an age between 6 and 60 as a whole number: '))

"""
* runs the best of 3 heads and tails loop
* generate a random choice for the computer and prompts the user for 'H' or 'T'
* validate user guesses, tracks until someone reaches the score of 2, 
  and announce the winner
"""
def heads_tails():

    # Ensure that the player and the computer starts at 0
    user_score = 0
    computer_score = 0

    options = ['H','T'] # possible options(H->heads or T->tails)

    # start the loop when both scores aren't 2 as 2 is the winning score
    while user_score!=2 and computer_score!=2:
        choice= random.randint(0,1) # the chioce is always random and unbiased
        computer_guess = options[choice]
        user_guess = input('Enter H or T: ') # taking user's input

        while(True): 
            if(user_guess in options): 
                break # end the loop if the input is valid
            else:
                user_guess = str(input('Invalid input. Enter H or T in capital: '))
        
        if user_guess == computer_guess:
            print("It was {}, you guessed {}, you won that round".format(computer_guess,user_guess))
            user_score +=1 # add one to the user's score if win
        else:
            print("It was {}, you guessed {}, you lost that round".format(computer_guess,user_guess))
            computer_score +=1 # add one to the computer's score if win

        # the game has 3 round. first one to win 2 wins the game overall
        if user_score == 2:
            print('{}, You won that game'.format(first_name))
        elif computer_score == 2:
            print('{}, You lost that game'.format(first_name))
    
#---------------------main routine----------------

if __name__ == "__main__":
    name = str(input('What is your name:')) 
    first_name = name_check(name)

    check_age()
    heads_tails()

    print('Hi {}! Welcome to the heads or tails game'.format(first_name)) 