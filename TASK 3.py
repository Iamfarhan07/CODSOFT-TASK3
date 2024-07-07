import random


def play():
    
    rounds=int(input("enter no. of rounds:"))
    for i in range(0,rounds):

        uwin=0
        cwin=0
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r', 'p', 's'])
        print(computer)

        if user == computer:
            uwin=uwin+1
            cwin=cwin+1
            print("It\s a tie")

      # r > s, s > p, p > r
        
        elif is_win(user, computer):
            uwin=uwin+1
            print("You won!")
           
        else:   
            cwin=cwin+1
            print("You lost!")

            
    if uwin>cwin:
            print("###################  YOU WON ######################")
    elif cwin>uwin:
            print("################### YOU LOST ######################")
    elif cwin==uwin:

            print("################### ITS A TIE ######################")    
        
            

def is_win(player, opponent):
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            
            
            return True


    
print(play())
i=input("Do you want to play again??y/n:-")
if i=='y':
      print(play())
    

