'''
    author: Aditha Mansilu Ranawaka
    date: 10/8/2026
    version: 
    desciption: Heads or Tails game
'''
#---------------------libraries-------------------
import random 

#---------------------functions-------------------

def name_check(first_name):
    min_name=2
    max_name=10

    while True:
        if (len(first_name) >= min_name and len(first_name) <= max_name):
            if(first_name.isalpha):
                return first_name
        else:
            print('Your name has an invalid length')
            first_name = input ('Enter your name again between 2 and 10 letters: ')
        

def check_age():
    min_age=6
    while True:
        try:
            age=int(input('Enter your age (in years):'))
            if age>=min_age:
                return age 
            else:
                age=int(input('Enter an age above 6'))
        except ValueError:
            age=int(input('Enter an age above 6 as a whole number: '))

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

        if user_score==2:
            print('{}, You won that game'.format(first_name))
        elif computer_score==2:
            print('{}, You lost that game'.format(first_name))
            

    
#---------------------main routine----------------

if __name__ == "__main__":
    first_name = str(input('What is your name:'))
    name_check(first_name)

    check_age()

    print('Hi {}! Welcome to the heads or tails game'.format(first_name))
    choice = heads_tails()
    
    # print(f'this is what i am recieving {choice}')




