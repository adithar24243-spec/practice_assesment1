'''
    author: Aditha Mansilu Ranawaka
    date: 10/8/2026
    version: 
    desciption: Heads or Tails game
'''
#---------------------libraries-------------------
import random 

#---------------------functions-------------------
def heads_tails():

    # Ensure that the player and the computer starts at 0
    user_score = 0
    computer_score = 0

    choice= random.randint(0,1)
    options = ['H','T'] 

    computer_guess = options[choice]
    user_guess = input('Enter H or T: ')

    # if user_guess == 'H' or user_guess == 'T':
    #     # ensure only valid guesses pesses through
    #     print(f'You entered {user_guess}, {computer_guess}')
    
    if user_guess == computer_guess:
        print("It was {}, you guessed {}, you won that round".format(computer_guess,user_guess))
        user_score +=1
    else:
        print("It was {}, you guessed {}, you lost that round".format(computer_guess,user_guess))
        computer_score +=1
    print(f'computer score is {computer_score}, and your score is {user_score}')
        
    # return 

    
#---------------------main routine----------------

if __name__ == "__main__":
    choice = heads_tails()
    
    print(f'this is what i am recieving {choice}')




