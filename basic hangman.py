#Step 1 
import random
import string
word_list = ["aardvark", "baboon", "camel", "apple", "movie"]
chosen_word=random.choice(word_list)
print(chosen_word)

list_chosen_word=[]
list_chosen_word=[char for char in chosen_word]
#print(list_chosen_word)

for i in chosen_word:
  print('_', end='')
string_of_bs='_'*(len(list_chosen_word))
list_of_bs=[char for char in string_of_bs]
#print(list_of_bs)

counter=len(list_chosen_word)

while(counter>0):
  guess_letter=input('\nGuess a letter')
  counter-=1
  if (guess_letter in list_chosen_word):
    for i in range(len(list_chosen_word)):
      if(list_chosen_word[i]==guess_letter):
        list_of_bs[i]=guess_letter

print(list_of_bs)
if(list_of_bs==list_chosen_word):
  print(chosen_word)
  
  




#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


