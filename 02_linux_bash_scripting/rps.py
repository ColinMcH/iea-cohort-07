
user1= input("Whats your name?")
user2= input("whats your name?")

u1 = input(f'{user1}, do you want to choose rock, paper, or scissors?')
u2 = input(f'{user2}, do you want to choose rock, paper, or scissors?')

def rps(u1,u2):
    if u1 == u2:
        return("its a tie")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("rock wins")
        else:
            return("paper wins")
    elif u1 == "scissors":
        if u2 == 'paper':
            return("scissors win")
        else:
            return("rock wins")
    elif u1 == "paper":
        if u2 == "rock":
            return("paper wins")
        else:
            return("scissors win")
    else:
        return("bad input, try again")
    
compare = rps(u1,u2)
print(compare)

