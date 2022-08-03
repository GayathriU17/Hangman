import random
import string
word_list = ["chakkara", "baby", "camel", "momo", "sweetie"]
chosen_word=random.choice(word_list)

list_chosen_word=[]
list_chosen_word=[char for char in chosen_word]
#print(list_chosen_word)

for i in chosen_word:
  print('_', end='')
string_of_bs=('_'+'')*(len(list_chosen_word))
list_of_bs=[char for char in string_of_bs]
#print(list_of_bs)

counter=5

while(counter>0):
  guess_letter=input('\nGuess a letter\t')

  if (guess_letter in list_chosen_word):
    for i in range(len(list_chosen_word)):
      if(list_chosen_word[i]==guess_letter):
        
        list_of_bs[i]=guess_letter
    print(list_of_bs)
   
    if(list_of_bs==list_chosen_word):
      print(chosen_word)
      print('CONGRATS! You WIN!!')
      break
    else:
      continue
    
  else:
    print(list_of_bs)
    counter-=1
    print(f"You lost a life. You now have {counter} chances left.")