# Blackjack Capstone
#print statements
from art import logo
import random

print (logo)
ch1=input("Would you like to play a round of BlackJack Capstone? Press 'y' for your first 2 cards and 'n' to quit.")

while(ch1=='y'):
    cards_list=[11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    user_cards=[]
    computer_cards=[]

    u1,u2= random.choices(cards_list, k=2)
    sum_u=u1+u2
    user_cards.append(u1)
    user_cards.append(u2)
    print(f"Your cards are {u1} and {u2}")

    c1,c2= random.choices(cards_list, k=2)
    sum_c=c1+c2
    computer_cards.append(c1)
    computer_cards.append(c2)
    print(f"Computer's cards are {c1} and {c2}")


    def add_cards_user(sum_u):
        new_card=random.choices(cards_list, k=1)[0]
        sum_u=sum_u+new_card
        print(f"Your next card: {new_card}")
        return sum_u

    def add_cards_computer(sum_c):
        if (sum_c<18):
            new_card_computer=random.choices(cards_list, k=1)[0]
            sum_c=sum_c+new_card_computer
            print(f"Computer's next card: {new_card_computer}")
        return sum_c

    def check(s1,s2):
        if(s1>21):
            print('You LOSE!!')
            return True
        elif(s2>21 and s1>21):
            print('DRAW!!')
            return True
        elif(s2>21):
            print('You WIN!!')
        elif(s1==s2):
            print('DRAW!!')
            return True
        if (s1==21 and s2!=21):
            print('Blackjack!! You WIN!!')
            return True
        elif(s2==21 and s1!=21):
            print('Blackjack!! You LOSE!')
            return True
        elif(s1>s2 and s1<21):
            print('You WIN!!')
            return True
        elif(s2>s1 and s2<21):
            print('You LOSE!!')  
            return True
  
    
    ch2=input('Do you want to add another card?')
    while(ch2=='y'):
        s1=add_cards_user(sum_u)
        s2=add_cards_computer(sum_c)
        y=check(s1,s2)
        if(y==True):
            break
        else:
            ch2=input('Do you want to add another card?')
    else:
        s2=add_cards_computer(sum_c)
        check(sum_u,s2)
    ch1=input("Would you like to play another round? Press 'y' to continue.")
else:
    print('END GAME!!')
   
   
          







