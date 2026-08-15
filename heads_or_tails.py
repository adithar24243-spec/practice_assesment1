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

    options = ['H','T'] 

    while user_score!=2 and computer_score!=2:
        choice= random.randint(0,1)
        computer_guess = options[choice]
        user_guess = input('Enter H or T: ')

        while(True): 
            if(user_guess in options):
                break
            else:
                user_guess =str(input('Invalid input. Enter H or T in capital: '))
        
        if user_guess == computer_guess:
            print("It was {}, you guessed {}, you won that round".format(computer_guess,user_guess))
            user_score +=1
        else:
            print("It was {}, you guessed {}, you lost that round".format(computer_guess,user_guess))
            computer_score +=1

        # if user_score==2:
        #     print('You won that game')
        # elif computer_score==2:
        #     print('You lost that game')
            
    # return 

    
#---------------------main routine----------------

if __name__ == "__main__":
    choice = heads_tails()
    
    # print(f'this is what i am recieving {choice}')




