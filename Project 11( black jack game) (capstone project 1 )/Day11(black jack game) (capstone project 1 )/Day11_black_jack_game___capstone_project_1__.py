import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card=random.choice(cards)
    
    return random_card

is_game_over=False

def calculate_score(cards):
    score=sum(cards)
    if score==21 and len(cards)==2:
        print("you win")
        return 0 
    if 11 in cards and score >21:
        cards.remove(11)
        cards.append(1)
    return score
    
def compare(user_score,computer_score):
    highst_score=0
    if user_score==computer_score:
        return "it is a draw"
    elif computer_score==0:
        return "computer has blackjack , you lose"
    elif user_score==0:
        return "you has a blackjack, you win"
    elif user_score>21:
        return "you exceed 21, you lose"
    elif computer_score>21:
        return "computer exceeds 21, you win"
    elif user_score>computer_score:
        return "your score is higher , you win"
    else:
        return "computer score is higher , you lose"            
def game():               
    user_card=[]
    computer_card=[]
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    
    while not is_game_over:    
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"user cards are {user_card} and user score are {user_score}")
        print(f"computer first card is {computer_card[0]} ")    
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True    
        else:
            add_card=input("press y or n to add another card or  to end game ")
            if add_card=="y":
                user_card.append(deal_card())    
            else:
                is_game_over=True   
        
    while computer_score !=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"user cards {user_card} and the  user score is {user_score} ")   
    print(f"computer cards {computer_card} and the  computer score is {computer_score} ") 
    print(compare(user_score,computer_score))

    while input("prss y to restart the game")=="y":
        clear()
        game()
      



        
    
    
        
            
        
       
    
       



    
    
