#BLACKJACK CAPSTONE
from art import logo
import random
cards_array=[2,3,4,5,6,7,8,9,10,10,10,1,11]

def pick_a_card():
    card=random.choice(cards_array)
    return card

def sumofcards(user_cards, computer_cards):
    sumuser=sum(user_cards)
    sumcomputer=sum(computer_cards)
    return sumuser, sumcomputer, user_cards, computer_cards

def add_card(f, y1, y2, user_cards, computer_cards):

    if(y1<17 and y2<17):
        computer_cards.append(pick_a_card())
        ch2=input("Your Score is <17. You must add another card. Press 'y' for your next card.").lower()
        if (ch2=='y'):
            user_cards.append(pick_a_card())
        y1,y2, user_cards, computer_cards =sumofcards(user_cards, computer_cards)
        print('Your cards are: ', user_cards)
        #print("Computer's Score: ", y2)
        print('Your Score: ', y1)
        f=0

    elif(y1<17 and y2>=17 and y2<=21):
        ch2=input("Your Score is <17. You must add another card. Press 'y' for your next card.").lower()
        if (ch2=='y'):
            user_cards.append(pick_a_card())
        y1,y2, user_cards, computer_cards =sumofcards(user_cards, computer_cards)
        print('Your cards are: ', user_cards)
        #print("Computer's Score: ", y2)
        print('Your Score: ', y1)
        f=0
    
    elif(y1<17 and y2>=21):
        y1,y2, user_cards, computer_cards =sumofcards(user_cards, computer_cards)
        print('Your cards are: ', user_cards)
        #print("Computer's Score: ", y2)
        print('Your Score: ', y1)
        f=1
    
    elif(y1>=17 and y1<21 and y2<17):
        ch2=input('Do you want another card?').lower()
        if (ch2=='y'):
            user_cards.append(pick_a_card())
        else:
            computer_cards.append(pick_a_card())
            y1,y2, user_cards, computer_cards =sumofcards(user_cards, computer_cards)
            return f, y1, y2, user_cards, computer_cards
        computer_cards.append(pick_a_card())
        y1,y2, user_cards, computer_cards =sumofcards(user_cards, computer_cards)
        print('Your cards are: ', user_cards)
        #print("Computer's Score: ", y2)
        print('Your Score: ', y1)
        f=0
    
    elif(y1>=21 and y2<17):
        computer_cards.append(pick_a_card())
        y1,y2, user_cards, computer_cards =sumofcards(user_cards, computer_cards)
        print('Your cards are: ', user_cards)
        #print("Computer's Score: ", y2)
        print('Your Score: ', y1)
        f=0

    elif(y1>=17 and y2>=17):
        f=1
    return f, y1, y2, user_cards, computer_cards

def compare (y1, y2):

    if(y1==21 and y2!=21):
        #print("Computer's Score:", y2)
        print('Blackjack! YOU WIN!')

    elif(y1!=21 and y2==21):
        #print("Computer's Score:", y2)
        print('Blackjack! COMPUTER WINS!')

    elif(y1>21 and y2<21):
        #print("Computer's Score:", y2)
        print('COMPUTER WINS!')

    elif(y1<21 and y2>21):
        #print("Computer's Score:", y2)
        print('YOU WIN!')

    elif(y1<21 and y2<21):
        if(y1>y2):
            #print("Computer's Score:", y2)
            print('YOU WIN!')

        elif(y2>y1):
            #print("Computer's Score:", y2)
            print('COMPUTER WINS!')

        else:
            print('DRAW!')

    elif(y1==y2):
        #print("Computer's Score:", y2)
        print('DRAW!')

    elif(y1>21 and y2>21):
        print('Both LOSE!')

def master():
    user_cards=[]
    computer_cards=[]

    for i in range(2):
        user_cards.append(pick_a_card())
        computer_cards.append(pick_a_card())
    
    print('Your cards are: ', user_cards)
    #print('Computer cards are: ', computer_cards)
    y1, y2, user_cards, computer_cards= sumofcards(user_cards, computer_cards)
    print('Your Score: ', y1)

    #CODE FRAGMENT TO pick a new card

    f=0

    #for testing -- print('Begin Loop')
    
    f, sum_u, sum_c, user_cards, computer_cards=add_card(f, y1, y2, user_cards, computer_cards)
    while(f==0):
        f, sum_u, sum_c, user_cards, computer_cards=add_card(f, sum_u, sum_c, user_cards, computer_cards)
    
    #for testing -- print('Exit Loop')
    
    if(f==1):
        print(f"Computer's choice of Cards were {computer_cards} and score was {sum(computer_cards)}")
        compare(sum_u, sum_c)

def main():
    print(logo)
    ch1=input("Would you like to play a round of BlackJack Capstone? Press 'y' for your first 2 cards and any other key to quit.").lower()
    while(ch1=='y'):
        master()
        ch1=input("Would you like to play another round of BlackJack Capstone? Press 'y' for your first 2 cards and any other key to quit.").lower()
    else:
        print('END GAME!')

main()
    