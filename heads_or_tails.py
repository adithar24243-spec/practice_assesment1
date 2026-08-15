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
    choice= random.randint(0,1)
    options = ['H','T']
    return options[choice] 
#---------------------main routine----------------

if __name__ == "__main__":
    choice = heads_tails()
    
    print(f'this is what i am recieving {choice}')




